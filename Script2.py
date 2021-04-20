# Code for part 1: Script 2
import pandas as pd
from pyjstat import pyjstat
import openpyxl
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt

# the URLs of the json-stat files to be used
marriage_URL = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/VSA41/JSON-stat/1.0/'
income_URL = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/SIA51/JSON-stat/1.0/'
birth_URL = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/VSA15/JSON-stat/1.0/'

# read from json-stat
marriage = pyjstat.Dataset.read(marriage_URL)
income = pyjstat.Dataset.read(income_URL)
birth = pyjstat.Dataset.read(birth_URL)

# write to dataframe
marriage = marriage.write('dataframe')
income = income.write('dataframe')
birth = birth.write('dataframe')

# limiting data to common years for all datasets
marriage['Year'] = pd.to_numeric(marriage['Year'])
marriage = marriage[marriage.Year.between(2012, 2021)]
income['Year'] = pd.to_numeric(income['Year'])
income = income[income.Year.between(2012, 2021)]
birth['Year'] = pd.to_numeric(birth['Year'])
birth = birth[birth.Year.between(2012, 2021)]

# Changing column name for marriage to match with birth and income
marriage = marriage.rename(columns = {'Region of Cermony': 'Region'}, inplace = False)

# Reformatting the data to have individual statistics as columns
marriage = marriage.pivot(index=["Year", 'Region'], columns="Statistic", values="value")
birth = birth.pivot(index=["Year", 'Region'], columns="Age Group of Mother", values="value")
income = income.pivot(index=["Year", 'Region'], columns="Statistic", values="value")

#  combining the datasets
b_m_data = pd.merge(marriage, birth, how='outer', on=['Year', 'Region'])
full_data = pd.merge(b_m_data, income, how='outer', on=['Year', 'Region'])

# print(full_data[full_data.index.get_level_values('Year').isin([2013])].columns)

# dff = pd.DataFrame(full_data[full_data.index.get_level_values('Region').isin(['Dublin'])]['Average Age of Bride'])
# print(dff.reset_index()['Average Age of Bride'])





# print(full_data.index.get_level_values('Year').unique().values)





#print(full_data.index.get_level_values('Region').unique())
#print(full_data[full_data.index.isin(['Dublin'], level=1)]['Average Age of Bride'])
# print(full_data[full_data.index.get_level_values('Region').isin(['Dublin', 'Midland'])])
# datatoexcel = pd.ExcelWriter('full_data.xlsx')
# # write DataFrame to excel
# full_data.to_excel(datatoexcel)
#
# # save the excel
# datatoexcel.save()
#
#Create the Dash app
app = dash.Dash()

# app.layout = html.Div(children=[
#     html.H1(children='Marriage, Income and Birth Statistics Dashboard'),
#     dcc.Dropdown(id='year-dropdown',
#                  options=[{'label': i, 'value': i}
#                           for i in full_data.index.get_level_values('Year').unique()],
#                  value='2018'),
#     dcc.Graph(id='stats-graph')
# ])
#
# #Set up the callback function
# @app.callback(
#     Output(component_id='stats-graph', component_property='figure'),
#     Input(component_id='year-dropdown', component_property='value')
# )
# def update_graph(selected_year):
#     filtered_year = full_data[full_data.index.get_level_values('Year').isin([selected_year])]
#     line_fig = px.bar(filtered_year,
#                        x=full_data.index.get_level_values('Region').unique(),
#                        y=
#                        full_data[full_data.index.get_level_values('Year').isin([selected_year])],
#                        title=f'Stats in {selected_year}')
#     return line_fig
#
# # Run local server
# if __name__ == '__main__':
#     app.run_server(debug=True)

app.layout = html.Div(children=[

    # the filter div
    html.Div([

        # geo
        html.Div([
            dcc.Dropdown(
                id='region',
                options=[{'label': i, 'value': i} for i in
                         full_data.index.get_level_values('Region').unique()],
                value='Dublin',
                placeholder="Select a Region"),

                dcc.Dropdown(
                    id='statistic',
                    value = 'Average Age of Bride',
                    multi=False),

                html.Hr(),

            ])
        ]),
    dcc.Graph(id='stats-graph')
    ])


@app.callback(
    Output('statistic', 'options'),
    [Input('region', 'value')])
def get_statistic(region_unit):
        return \
            [{'label': i, 'value': i} for i in full_data[full_data.index.get_level_values('Region').isin([region_unit])]
                .columns]

@app.callback(
    Output(component_id='stats-graph', component_property='figure'),
    Input(component_id='region', component_property='value'),
    Input(component_id='statistic', component_property='value')
)
def update_graph(region, statistic):
    dff = full_data[full_data.index.get_level_values('Region').isin([region])][statistic]
    line_fig = px.line(dff,
                       x= dff.reset_index()['Year'],
                       y= dff.reset_index()[statistic],
                       title=f'{statistic} in {region}'
                       )
    line_fig.update_xaxes(title_text = "Year")

    line_fig.update_yaxes(title_text = statistic)

    return line_fig

if __name__ == '__main__':
    app.run_server(debug=True)