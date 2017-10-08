#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 14:18:32 2017

@author: panin
"""

from brian2 import *

n=3 #1000 neurons
duration = 1*second #simulation 
tau = 10*ms #time constant
#leaky LF without current
eqs = '''
dv/dt = (v0-v)/tau :volt (unless refractory)
v0:volt 
'''
#neuron
group = NeuronGroup(n,eqs,threshold='v>10*mV',reset='v=0*mV', refractory=5*ms,method='linear')
group.v = 0*mV
group.v0 = '20*mV* i /(n-1)'

M = StateMonitor(group,'v',record=True)
monitor = SpikeMonitor(group)

run(duration)
plot(group.v0/mV, monitor.count / duration)
xlabel('v0 (mV)')
ylabel('Firing rate (sp/s)')
show()