# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy import linalg
from scipy import constants as C
from scipy import special
conductors_equivalent_radius=0.001*np.array([6.18,4.74,9.03,49.65,49.65,7.22,4.055,6.18,4.74,9.03,49.65,49.65,7.22,4.055])
conductors_rho=10**-10*np.array([172.41,0.185,0.29731,2.1121,2.1121,0.029667,0.19264,172.41,0.185,0.29731,2.1121,2.1121,0.029667,0.19264])
f=50
mu=4*np.pi*10**-7 
r=conductors_equivalent_radius
rho=conductors_rho
m=np.sqrt(2*np.pi*f*mu/rho)
print(rho)
print(r)
print(m)
A1=m*r/2
A2=4/(m*r)
B1=special.ber(m*r)
B2=special.bei(m*r)
C1=special.berp(m*r)
C2=special.beip(m*r)
aR=A1*((B1*C2-C1*B2)/(C1**2+C2**2))
aL=A2*((B2*C2-C1*B1)/(C1**2+C2**2))
print(aR)
print(aL)