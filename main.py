"""
PHYS-213: Alpha decay half-life estimator
A program that estimates the half-life of a particular alpha decay nuclear
reaction

author Diego Guerrero
"""
import numpy as np
from numpy import pi
from scipy.constants import e, c, u, hbar, epsilon_0

k=1.0/(4.0*pi*epsilon_0) #Coulomb constant

print("--- Alpha Decay Estimator ---")
Z = float(input("Enter atomic number of parent: ") or 90)
A = float(input("Enter mass number of parent A: ") or 230)
m_parent_u = float(input("Enter atomic mass of parent [u]: ") or 230.033128)
m_daughter_u = float(input("Enter atomic mass of daughter [u]: ") or 226.025403)
z=2.0
m_alpha_u = 4.002603

m_parent_u = 228.0287397
m_daughter_u = 224.0202104
A = 228
Z=90


Q=(m_parent_u-m_daughter_u-m_alpha_u)*u*c*c
mu_reduced = u*m_daughter_u*m_alpha_u/(m_daughter_u + m_alpha_u) # Reduced mass of system

a=(1.23e-15)*pow(A-4.0,1/3) + (1.23e-15)*pow(4,1/3) # Atomic radius approximation formula



B = k*z*(Z-z)*e*e/a # Coulomb field at surface of atom

V=B

x=Q/B
G=np.sqrt(2.0*mu_reduced/(pow(hbar,2.0)*Q))*(k*z*(Z-z)*e*e)*(np.arccos(np.sqrt(x)) - np.sqrt(x*(1.0-x)))
t=np.log(2.0)*a*(np.sqrt(mu_reduced/(2.0*(V+Q))))*np.exp(2.0*G)

print("------------------------")
print("Mass Number:")
print(A)
print("Q(MeV):")
print(Q/e/1e6)
print("Estimated half life:")
print(t)
