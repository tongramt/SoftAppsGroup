# Code for part 1: Script 2
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

both_genders = pd.concat([girls, boys])
full_data = pd.concat([both_genders, birth_rates])
print(full_data.head())




