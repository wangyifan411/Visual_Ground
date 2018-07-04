# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 18:01:12 2018

@author: wangyf
"""

import sys
import os
import numpy as np
import pandas as pd

# working on all platforms, using cross-platform home path

HomePath = os.path.expanduser('~')
sys.path.append(os.path.join(HomePath,'Documents','GitHub', 'Pdn-Dynamics-Model', 'Generator'))
sys.path.append(os.path.join(HomePath,'Documents','GitHub', 'Pdn-Dynamics-Model', 'Analysis'))
sys.path.append(os.path.join(HomePath,'Documents','GitHub', 'Pdn-Dynamics-Model', 'Generator','user_inputs'))

import process_specnum as pspec
import plot_specnum as dspec
from IO_Pdn import *
from nc import *

fname = 'surf_spec.csv'
csv_dir =  os.path.join(os.getcwd(), fname)


data = pd.read_csv(csv_dir, sep = '\t')

import plotly as py
import plotly.graph_objs as go
import cufflinks as cf


'''
t_vec = data['t']
graphdata = [go.Scatter(x = t_vec, y = data['Pd1*'], name = 'Pd1*'),
             go.Scatter(x = t_vec, y = data['Pd2*'], name = 'Pd2*'),
             go.Scatter(x = t_vec, y = data['Pd3*'], name = 'Pd3*'),
             go.Scatter(x = t_vec, y = data['Pd4*'], name = 'Pd4*'),
             go.Scatter(x = t_vec, y = data['Pd4_3&1*'], name = 'Pd4_3&1*'),
             go.Scatter(x = t_vec, y = data['Pd5*'], name = 'Pd5*'),
             ]
url = py.offline.plot(graphdata, filename = 'spec_test_1')

