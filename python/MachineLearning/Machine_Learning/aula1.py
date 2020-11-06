# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:33:01 2019

@author: Administrador
"""
import pandas as pd


uri = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"
dados = pd.read_csv(uri)

x = dados[['home','how_it_works','contact']]
y = dados ['bought']

from sklearn.svm import LinearSVC

modelo = LinearSVC()
modelo.fit(x,y)