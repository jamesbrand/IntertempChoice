
# coding: utf-8

# In[2]:

from ConsIndShockModel import IndShockConsumerType
from ConsIndShockModel import PerfForesightConsumerType 
import copy 
import ConsumerParameters as Params
import numpy as np
import itertools

def makeFarmerHist(stdPerm, stdTran, numAgents,numPeriods):
    FarmerParameters = {'BoroCnstArt': 0.0,'CRRA': np.inf, 'CubicBool': True,'DiscFac': 0.5,'IncUnemp': 0.0,
                 'IncUnempRet': 0.0,'LivPrb': [0.98], 'Nagents': 100,'PermGroFac': [1.01],'PermShkCount': 20,
                 'PermShkStd': [stdPerm],'Rfree': 1.0,'T_retire': 0,'T_total': 1,'TranShkCount': numAgents,'TranShkStd': [stdTran],
                 'UnempPrb': 0.0,'UnempPrbRet': 0.00,'aXtraCount': 12,'aXtraExtra': [None],'aXtraMax': 20,'aXtraMin': 0.001,
                 'aXtraNestFac': 3,'tax_rate': 0.0,'vFuncBool': False}
    PerfForFarmer = PerfForesightConsumerType(**FarmerParameters)
    PerfForFarmer.solve()
    Farmer = IndShockConsumerType(**FarmerParameters)
    Farmer.solution = copy.deepcopy(PerfForFarmer.solution)
    Farmer.addToTimeVary('solution')
    Farmer.sim_periods = numPeriods;
    Farmer.initializeSim(sim_prds=Farmer.sim_periods) 
    Farmer.makeIncShkHist()
    Farmer.simConsHistory()
    Farmer.IncHist = np.multiply(Farmer.PermShkHist, Farmer.TranShkHist)
    Farmer.IncHist = np.reshape(Farmer.IncHist,(Farmer.Nagents*Farmer.sim_periods,1))
    Farmer.cHist = np.reshape(Farmer.cHist,(Farmer.Nagents*Farmer.sim_periods,1))
    Farmer.IncHist = list(itertools.chain.from_iterable(Farmer.IncHist))
    Farmer.cHist = list(itertools.chain.from_iterable(Farmer.cHist))
    return (Farmer.IncHist, Farmer.cHist)
    
def makeNonFarmerHist(stdPerm, stdTran, numAgents, numPeriods):
    NonFarmerParams = {'BoroCnstArt': 0.0,'CRRA': np.inf, 'CubicBool': True,'DiscFac': 0.5,'IncUnemp': 0.0,
                 'IncUnempRet': 0.0,'LivPrb': [0.98], 'Nagents': 100,'PermGroFac': [1.01],'PermShkCount': 20,
                 'PermShkStd': [stdPerm],'Rfree': 1.0,'T_retire': 0,'T_total': 1,'TranShkCount': numAgents,'TranShkStd': [stdTran],
                 'UnempPrb': 0.0,'UnempPrbRet': 0.00,'aXtraCount': 12,'aXtraExtra': [None],'aXtraMax': 20,'aXtraMin': 0.001,
                 'aXtraNestFac': 3,'tax_rate': 0.0,'vFuncBool': False}
    PerfForNonFarmer = PerfForesightConsumerType(**NonFarmerParams)
    PerfForNonFarmer.solve()
    NonFarmer = IndShockConsumerType(**NonFarmerParams)
    NonFarmer.solution = copy.deepcopy(PerfForNonFarmer.solution) 
    NonFarmer.addToTimeVary('solution')
    NonFarmer.sim_periods = numPeriods
    NonFarmer.initializeSim(sim_prds=NonFarmer.sim_periods) 
    NonFarmer.makeIncShkHist()
    NonFarmer.simConsHistory()
    NonFarmer.IncHist = np.multiply(NonFarmer.PermShkHist, NonFarmer.TranShkHist)
    NonFarmer.IncHist = np.reshape(NonFarmer.IncHist,(NonFarmer.Nagents*NonFarmer.sim_periods,1))
    NonFarmer.cHist = np.reshape(NonFarmer.cHist,(NonFarmer.Nagents*NonFarmer.sim_periods,1))
    NonFarmer.IncHist = list(itertools.chain.from_iterable(NonFarmer.IncHist))
    NonFarmer.cHist = list(itertools.chain.from_iterable(NonFarmer.cHist))
    return (NonFarmer.IncHist, NonFarmer.cHist)
    


# In[ ]:



