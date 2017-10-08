#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 14:18:32 2017

@author: panin
"""

from brian2 import *

start_scope()
duration=50*ms
tau = 10*ms
#eqs
eqs = '''
dv/dt= (v0-v)/tau : 1 (unless refractory)
v0 : 1
'''

#single neuron
g = NeuronGroup(100, eqs,threshold='v>2',reset='v=0',refractory=5*ms,method='linear')
g.v0='1*i/(n-1)'
#monitor
M = StateMonitor(g,'v',record=0)
S = SpikeMonitor(g)




#run
run(duration)
plot(g.v0,S.count/duration)




#plot(M.t/ms, M.v[0])
#xlabel('Time (ms)')
#ylabel('v');
#show() 