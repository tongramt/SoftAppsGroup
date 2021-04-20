# Code for part 1: Script 2
import urllib3
import pandas as pd
from pyjstat import pyjstat

girls_URL = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/VSA60/JSON-stat/1.0/'
boys_URL = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/VSA50/JSON-stat/1.0/'
birth_rates_URL = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/VSB14/JSON-stat/1.0/'

# read from json-stat
girls = pyjstat.Dataset.read(girls_URL)
boys = pyjstat.Dataset.read(boys_URL)
birth_rates = pyjstat.Dataset.read(birth_rates_URL)

# write to dataframe
girls = girls.write('dataframe')
boys = boys.write('dataframe')
birth_rates = birth_rates.write('dataframe')

girls.set_index('Years', inplace=True)
boys.set_index('Years', inplace=True)
birth_rates.set_index('Years', inplace=True)
both_genders = pd.merge(girls, boys, on='Year')
print(both_genders.head())




