# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 10:09:11 2019

@author: atakan
"""
import numpy as np
import math
class magnet():
    def __init__ (self, d,z):
	        self.d = d
	        self.z = z
    def cupe_dipole_moment(self,w,l,b,v):
                d = self.d
                z = self.z        
                mainfun=np.arctan((l*w)/(2*z*np.sqrt(4*z**2+l**2+w**2)))-np.arctan((l*w)/(2*(d+z)*np.sqrt(4*(d+z)**2+l**2+w**2)))
                br=(b*np.pi/mainfun)
                m1=float(br*v/(10000*4*np.pi*10**-7))
                return m1
    def cylindir_dipole_moment(self,r,b,v):
                d = self.d
                z = self.z 
                br=(b*2)/((d+z)/(np.sqrt(r**2+(d+z)**2))-(z/(np.sqrt(r**2+z**2))))
                m2=float((br*v)/(10000*4*np.pi*10**-7))
                return m2

