import matplotlib.pyplot as plt 
import pandas as pd



pd.set_option('display.max_rows', 100000)

import sys
import numpy as np 

import csv 
filedat = pd.read_csv("indianEco.csv")
print(filedat)

x=filedat['Year']

gdpt=filedat['GDP (current US$) ']
gdppc=filedat['GDP growth (annual %)']
perc_import_good_gst=[filedat['Imports of goods and services (% of GDP)']]
exportgoods=filedat['Exports of goods and services (% of GDP)']
totalres=filedat[' Total reserves (includes gold, current US$) ']
inflationst=filedat['Inflation, consumer prices (annual %)']
totpop=filedat['Population, total']
popg=filedat['Population growth (annual %)']
lifexp=filedat['Life expectancy at birth, total (years)']




plt.plot(x,gdpt)
plt.xlabel('Year')
plt.ylabel('GDP (current US$) ')
plt.show()




plt.plot(x,gdppc)
plt.xlabel('Year')
plt.ylabel('GDP growth (annual %)')
plt.show()




plt.plot(x,totalres)
plt.xlabel('Year')
plt.ylabel('Total Reserves')
plt.show()



plt.plot(x,exportgoods)
plt.xlabel('Year')
plt.ylabel('G&S ExportT')
plt.show()



plt.plot(x,inflationst)
plt.xlabel('Year')
plt.ylabel('Inflation')
plt.show()


plt.plot(x,totpop)
plt.xlabel('Year')
plt.ylabel('Total Population')
plt.show()



plt.plot(x,popg)
plt.xlabel('Year')
plt.ylabel('Population Growth(annual %)')
plt.show()


plt.plot(x,lifexp)
plt.xlabel('Year')
plt.ylabel('Life Expecatancy at Birth')
plt.show()









