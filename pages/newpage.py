import dash
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
from app import app
import pandas as pd


# def build_banner():
#     return html.Div(
#         id="banner",
#         className="banner",
#         children=[
#             html.Div(
#                 id="banner-text",
#                 children=[
#                     html.H5("Kickstarter Prediction"),
#                 ],
#             ),
#         ],
#     )


# def build_tabs():
#     return html.Div(
#         id="tabs",
#         className="tabs",
#         children=[
#             dcc.Tabs(
#                 id="app-tabs",
#                 value="tab2",
#                 className="custom-tabs",
#                 children=[
#                     dcc.Tab(
#                         id="Kickstarter-Paramters",
#                         label="Kickstarter Parameters",
#                         value="tab1",
#                         className="custom-tab",
#                         selected_className="custom-tab--selected",
#                     ),
#                     dcc.Tab(
#                         id="Kickstarter-Details",
#                         label="Kickstarter Details",
#                         value="tab2",
#                         className="custom-tab",
#                         selected_className="custom-tab--selected",
#                     ),
#                 ],
#             )
#         ],
#     )


# app.layout = html.Div(
#     id="big-app-container",
#     children=[
#         build_banner(),
#         html.Div(
#             id="app-container",
#             children=[
#                 build_tabs(),
#                 # Main app
#                 html.Div(id="app-content"),
#             ],
#         ),
#     ],
# )

app.layout = html.Div([
    dcc.Tabs(
        id="tabs-with-classes",
        value='tab-2',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Tab one',
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab two',
                value='tab-2',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab three, multiline',
                value='tab-3', className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab four',
                value='tab-4',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
        ]),
    html.Div(id='tabs-content-classes')
])


@app.callback(Output('tabs-content-classes', 'children'),
              Input('tabs-with-classes', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])

layout = app.layout