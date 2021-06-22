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
# pipeline = load("assets/model_xgbapp.joblib")

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
@app.callback(
    Output('prediction-content', 'children'),
    [Input('unique_id', 'value'), 
    Input('since_created', 'value'),
    Input('since_launched', 'value'),
    Input('since_changed', 'value'),
    Input('usd_pledged', 'value'),
    Input('text', 'value'),
    Input('state', 'value'),
    ],
)
def predict(unique_id,since_created,
since_launched,since_changed,usd_pledged,
text,state):
    df = pd.DataFrame(
        columns=['unique_id',
        'since_created',
        'since_launched',
        'since_changed',
        'usd_pledged',
        'text',
        'state'], 
        data=[[unique_id, since_created,
        since_launched,since_changed,usd_pledged,
        text,state]]
    )
#     y_pred = pipeline.predict(df)[0]
#     return f'{y_pred}'


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Feature Explination

            The features on the right are the 7 major contributors to the machine 
            learning model. 

            ##### Unique ID : 
            ToDo
            ##### Since Created : 
            ToDo
            ##### Since Launched : 
            ToDo
            ##### Since Changed : 
            ToDo
            ##### USD Pledged : 
            ToDo
            ##### Text : 
            ToDo
            ##### State : 
            ToDo
            """
        ),
        html.H2('Exoplanet Prediction', className='mb-5'),
        html.Div(id='prediction-content', className='lead')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## Prediction Features', className='mb-5'), 
        dcc.Markdown('#### How much funding do you need to raise?'), 
        dcc.Slider(
            id='usd_goal', 
            min=1, 
            max=21, 
            step=2, 
            value=800, 
            marks={n: str(n) for n in range(1,22,2)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### How long will your project be open for funding?'), 
        dcc.Slider(
            id='timeline', 
            min=20, 
            max=200, 
            step=20, 
            value=100, 
            marks={n: str(n) for n in range(20,201,20)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### What category is your project?'), 
        dcc.Slider(
            id='since_launched', 
            min=1, 
            max=101, 
            step=10, 
            value=50, 
            marks={n: str(n) for n in range(1,102,10)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### What is the sub-category?'), 
        dcc.Slider(
            id='since_changed', 
            min=1, 
            max=101, 
            step=10, 
            value=10, 
            marks={n: str(n) for n in range(1,102,10)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Text'), 
        dcc.Textarea(
            id='text',
            placeholder='Enter a value...',
            value='This is a TextArea component',
            style={'width': '100%'},
            className='mb-5',
        ), 
        dcc.Markdown('#### State'), 
        dcc.Slider(
            id='state', 
            min=1, 
            max=101, 
            step=10, 
            value=50, 
            marks={n: str(n) for n in range(1,102,10)}, 
            className='mb-5', 
        ), 
    ],
)

layout = dbc.Row([column1, column2])