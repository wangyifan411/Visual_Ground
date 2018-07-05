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

s_df = pd.read_csv(csv_dir, sep = '\t')

ylabel = 'Species count'

dspec.PlotLiveSpec(s_df, xlab = 'Time (s)', ylab = ylabel, 
                   fname =  'live_surf_vs_time.html')


