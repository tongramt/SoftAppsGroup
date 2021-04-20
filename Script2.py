# Code for part 1: Script 2
import pandas as pd
from pyjstat import pyjstat
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

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

marriage['Year'] = pd.to_numeric(marriage['Year'])
marriage = marriage[marriage.Year.between(2012, 2021)]
income['Year'] = pd.to_numeric(income['Year'])
income = income[income.Year.between(2012, 2021)]
birth['Year'] = pd.to_numeric(birth['Year'])
birth = birth[birth.Year.between(2012, 2021)]

marriage = marriage.rename(columns = {'Region of Cermony': 'Region'}, inplace = False)

marriage = marriage.pivot(index=["Year", 'Region'], columns="Statistic", values="value")
birth = birth.pivot(index=["Year", 'Region'], columns="Age Group of Mother", values="value")
income = income.pivot(index=["Year", 'Region'], columns="Statistic", values="value")

b_m_data = pd.merge(marriage, birth, how='outer', on=['Year', 'Region'])
full_data = pd.merge(b_m_data, income, how='outer', on=['Year', 'Region'])

datatoexcel = pd.ExcelWriter('full_data.xlsx')
# write DataFrame to excel
full_data.to_excel(datatoexcel)

# save the excel
datatoexcel.save()

# # Source for code: https://dash.plotly.com/layout
# #  Need to install dash and plotly
# # visit http://127.0.0.1:8050/ in your web browser.
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# # assume you have a "long-form" data frame
# # see https://plotly.com/python/px-arguments/ for more options
df = full_data
#
fig = px.bar(df, x="Names", y="value", barmode="group")
#
app.layout = html.Div(children=[
     html.H1(children='My First Dash'),

     html.Div(children='''
        Dash: A web application framework for Python.   '''),

    dcc.Graph(
         id='example-graph',
         figure=fig
     )
 ])
if __name__ == '__main__':
     app.run_server(debug=True, use_reloader=False)
#
#
#
