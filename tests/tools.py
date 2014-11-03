#!/usr/bin/env python
# coding: UTF-8

#------------------------------------------------------------------------------
# Functions and variables utilised in the unit-tests
#------------------------------------------------------------------------------

from __future__ import division

import numpy as np

norm = np.linalg.norm

xs = np.linspace(-1, 1, 1000)

def map_ab_ui(x, a, b): 
    return (2.0*x-a-b)/(b-a)
    
def map_ui_ab(t, a, b): 
    return 0.5*(b-a)*t + 0.5*(a+b) 

def Identity(x):
    return x

def One(x):
    return np.ones_like(x, dtype=float)

def Zero(x):
    return np.zeros_like(x, dtype=float)

def circle(x):
    return np.array([np.cos(np.pi*x), np.sin(np.pi*x)],).T

def f(x):
    return np.sin(6*x) + np.sin(30*np.exp(x))

def fd(x):
    """
    Derivative of f
    """
    return 6*np.cos(6*x) + np.cos(30*np.exp(x))*30*np.exp(x)

functions = [f]
first_derivs = [fd]
domains = [(1,2),(0,2),(-1,0),(-.2*np.pi,.2*np.e),(-1,1)]

integrals = [
    [ 0.032346217980525,  0.030893429600387, -0.014887469493652,
     -0.033389463703032, -0.016340257873789, ]
]

roots = [
    [
        np.array([
            1.004742754531498, 1.038773298601836, 1.073913103930722,
            1.115303578807479, 1.138876334576409, 1.186037005063195,
            1.200100773491540, 1.251812490296546, 1.257982114030372,
            1.312857486088040, 1.313296484543653, 1.365016316032836,
            1.371027655848883, 1.414708808202124, 1.425447888640173,
            1.462152640981920, 1.476924360913394, 1.507538306301423,
            1.525765627652155, 1.551033406767893, 1.572233571395834,
            1.592786143530423, 1.616552437657155, 1.632928169757349,
            1.658915772490721, 1.671576942342459, 1.699491823230094,
            1.708837673403015, 1.738427795274605, 1.744804960074507,
            1.775853245044121, 1.779564153811983, 1.811882812082608,
            1.813192517312102, 1.845760207165999, 1.846618439572035,
            1.877331112646444, 1.880151194495009, 1.907963575049332,
            1.912562771369236, 1.937711007329229, 1.943926743585850,
            1.966622430081970, 1.974309611716701, 1.994742937003962,
        ]),
    
        np.array([
            0.038699154393837, 0.170621357069026, 0.196642349303247,
            0.335710810755860, 0.360022217617733, 0.459687243605995,
            0.515107092342894, 0.571365105600701, 0.646902333813374,
            0.672854750953472, 0.761751991347867, 0.765783134619707,
            0.851427319155724, 0.863669737544800, 0.930805860269712,
            0.955368374256150,
            1.004742754531498, 1.038773298601836, 1.073913103930722,
            1.115303578807479, 1.138876334576409, 1.186037005063195,
            1.200100773491540, 1.251812490296546, 1.257982114030372,
            1.312857486088040, 1.313296484543653, 1.365016316032836,
            1.371027655848883, 1.414708808202124, 1.425447888640173,
            1.462152640981920, 1.476924360913394, 1.507538306301423,
            1.525765627652155, 1.551033406767893, 1.572233571395834,
            1.592786143530423, 1.616552437657155, 1.632928169757349,
            1.658915772490721, 1.671576942342459, 1.699491823230094,
            1.708837673403015, 1.738427795274605, 1.744804960074507,
            1.775853245044121, 1.779564153811983, 1.811882812082608,
            1.813192517312102, 1.845760207165999, 1.846618439572035,
            1.877331112646444, 1.880151194495009, 1.907963575049332,
            1.912562771369236, 1.937711007329229, 1.943926743585850,
            1.966622430081970, 1.974309611716701, 1.994742937003962,
        ]),
    
        np.array([
            -0.928510879374692, -0.613329324979852, -0.437747415493617,
            -0.357059979912156, -0.143371301774133, -0.075365172766102,       
        ]),
        
        np.array([
            -0.613329324979852, -0.437747415493618, -0.357059979912156,
            -0.143371301774133, -0.075365172766103,  0.038699154393837,
             0.170621357069026,  0.196642349303248,  0.335710810755860,
             0.360022217617734,  0.459687243605995,  0.515107092342894,
        ]),
        
        np.array([
            -0.928510879374692, -0.613329324979852, -0.437747415493617,
            -0.357059979912156, -0.143371301774133, -0.075365172766102,       
             0.038699154393837,  0.170621357069026,  0.196642349303247,
             0.335710810755860,  0.360022217617733,  0.459687243605995,
             0.515107092342894,  0.571365105600701,  0.646902333813374,
             0.672854750953472,  0.761751991347867,  0.765783134619707,
             0.851427319155724,  0.863669737544800,  0.930805860269712,
             0.955368374256150,
        ])
    ]
]
