# Imports from 3rd party libraries
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
from joblib import load
pipeline = load("assets/model.joblib")

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
@app.callback(
    Output('prediction-content', 'children'),
    [Input('usd_goal', 'value'), 
    Input('category', 'value'),
    Input('timeline', 'value'),
    Input('sub_category', 'value'),
#    Input('text', 'value'),
    ],
)
def predict(usd_goal,category,timeline,sub_category,
#,text
):
    df = pd.DataFrame(
        columns=['usd_goal',
        'category',
        'timeline',
        'sub_category',
#        'text',
], 
        data=[[usd_goal, category,timeline,sub_category,
#        text
        ]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred}'


column1 = dbc.Col(
    [
        dcc.Markdown('## Kickstarter Parameters', className='mb-5'), 
        dcc.Markdown('#### How much funding do you need to raise?'), 
        dcc.Slider(
            id='usd_goal', 
            min=1000, 
            max=1000000, 
            step=1, 
            value=800, 
            marks={n: str(n) for n in range(1,22,2)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### How long will your project be open for funding?'), 
        dcc.Slider(
            id='timeline', 
            min=10, 
            max=365, 
            step=30, 
            value=100, 
            marks={n: str(n) for n in range(10,366,30)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### What category is your project?'), 
        dcc.Dropdown(
            id='category',
            className='mb-5',
            options=[
                {'label': 'Art', 'value': 'art'},
                {'label': 'Comics', 'value': 'comics'},
                {'label': 'Crafts', 'value': 'crafts'},
                {'label': 'Dance', 'value': 'dance'},
                {'label': 'Design', 'value': 'design'},
                {'label': 'Fashion', 'value': 'fashion'},
                {'label': 'Film & Video', 'value': 'film_video'},
                {'label': 'Food', 'value': 'food'},
                {'label': 'Games', 'value': 'games'},
                {'label': 'Journalism', 'value': 'journalism'},
                {'label': 'Music', 'value': 'music'},
                {'label': 'Photography', 'value': 'photography'},
                {'label': 'Publishing', 'value': 'publishing'},
                {'label': 'Technology', 'value': 'technology'},
                {'label': 'Theater', 'value': 'theater'},

        ],
        value='NYC'
        ),
 
        dcc.Markdown('#### What is the sub-category?'), 
        dcc.Dropdown(
            id='sub_category',
            className='mb-5',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montreal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC'
        ), 
        # dcc.Markdown('#### Text'), 
        # dcc.Textarea(
        #     id='text',
        #     placeholder='Enter a value...',
        #     value='This is a TextArea component',
        #     style={'width': '100%'},
        #     className='mb-5',
        # ), 
        
        # dcc.Markdown(
        #     """
        
        #     ## Feature Explination

        #     The features on the right are the 7 major contributors to the machine 
        #     learning model. 

        #     ##### Unique ID : 
        #     ToDo
        #     ##### Since Created : 
        #     ToDo
        #     ##### Since Launched : 
        #     ToDo
        #     ##### Since Changed : 
        #     ToDo
        #     ##### USD Pledged : 
        #     ToDo
        #     ##### Text : 
        #     ToDo
        #     ##### State : 
        #     ToDo
        #     """
        # ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Exoplanet Prediction', className='mb-5'),
        html.Div(id='prediction-content', className='lead')
    ],
)

layout = dbc.Row([column1, column2])
