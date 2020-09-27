# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 00:47:27 2020

@author: Fady_
"""

import Glassdoor_scraper as gs
import pandas as pd

path= "C:/Users/Fady_/Documents/ds_salary_proj/geckodriver.exe"

df = gs.get_jobs('data scientist' , 1000 , False, path , 15)
df.to_csv('Glassdoor_jobs.csv', index = False)