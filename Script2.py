# Code for part 1: Script 2
import urllib3
import pandas as pd
import pyjstat from pyjstat

EXAMPLE_URL = 'http://json-stat.org/samples/galicia.json'

# read from json-stat
dataset = pyjstat.Dataset.read(EXAMPLE_URL)

# write to dataframe
df = dataset.write('dataframe')
print(df)

