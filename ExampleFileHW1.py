
# coding: utf-8

# In[13]:

### Starter File

import os 
## Change the directory to wherever you've stored the HARK files
os.chdir('C:/Users/Jimbo/HARK')
import numpy as np
from HARKutilities import plotFuncs
## On my computer, I have to re-specify the path. Do the same if necessary-- delete otherwise. 
os.chdir('C:/Users/Jimbo/HARK/ConsumptionSaving')

## Import tools for constructing and plotting histories
import pylab as plt 
import matplotlib.pyplot as ply
from scipy import stats
import itertools


from HelpFuncs import *
## The arguments for the two following functions are: 
## (PermanentVariance, TransitoryVariance, Number of Agents, Number of Periods)
## Note, when doing part (b), that the histories are stored such that the first 
## "Number of Agents" rows are the income/consumption of the whole sample in the first
## period. 

FarmerIncome, FarmerConsumption = makeFarmerHist(0.02, 0.06, 20,10)
NonFarmerIncome, NonFarmerConsumption = makeNonFarmerHist(0.02, 0.02, 20, 10)


### 1(a) Plot simulated histories with fitted line






## 1(b) 



# In[ ]:



