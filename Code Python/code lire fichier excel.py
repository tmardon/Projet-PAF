# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:53:13 2017
"""


import matplotlib.pyplot as plt
import numpy as np
import random 
import xlrd
import matplotlib



#ouverture du fichier excel
tab = xlrd.open_workbook('test1_accelero.xlsx')
sh = tab.sheet_by_name(u'Feuil1')

#données
colonneX = sh.col_values(1)
colonneY = sh.col_values(2)
colonneZ = sh.col_values(3)
longueur = len(colonneX)    
T = np.arange(0,(longueur)*0.05,0.05)  #Fe=20Hz

#visualisation des données
pX = plt.plot(T,colonneX, color="green",linewidth=1.5,marker="*",label="X")
pY = plt.plot(T,colonneY, color="red",linewidth=1.5,marker="*",label="Y")
pZ = plt.plot(T,colonneZ, color="blue",linewidth=1.5,marker="*",label="Z")
plt.xlabel("Temps(s)")
plt.ylabel("Acceleration(g)")
plt.title("Acceleromètre")

plt.show()