#################################################################################################
#                                                                                               #
#   Routine for covid-19 plot generation for a given municipality in Onondaga County NY         #
#                                                                                               #
# Author:  Michael J. P. Morse                                                                  #
# License: file 'LICENSE.txt'                                                                   #
# Date: 04/04/2020                                                                              #
#                                                                                               #
#################################################################################################

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from datetime import date
from datetime import datetime
import matplotlib.pyplot as plt ## Plotting
import matplotlib.ticker as tck ## modify ticks on plot
import sys


## Load the time series
df_time_series = pd.read_csv('onondaga_time_series.csv',index_col=0)
#df_time_series=pd.DataFrame()


#####
# Plotter
###

municipality = str(sys.argv[1])

ds_cty = df_time_series.sum()
ds_municipality = df_time_series.loc[municipality]


first_case_cty = ds_cty.iloc[0]
first_case_muni = ds_municipality.iloc[0]

## two day doubling
two_day_double_cty =  [first_case_cty, first_case_cty * (2)**((len(ds_cty)//2))]
two_day_double_muni = [first_case_muni, first_case_muni * (2)**(len(ds_municipality)//2)]

## three day doubling
three_day_double_cty = [first_case_cty, first_case_cty * (2)**((len(ds_cty)//3))]
three_day_double_muni =  [first_case_muni, first_case_muni * (2)**(len(ds_municipality)//3)]

## First and last date of reporting
first_last_day_cty = [ds_cty.index[0],ds_cty.index[-1]]
first_last_day_muni = [ds_municipality.index[0],ds_municipality.index[-1]]





fig, ax = plt.subplots(figsize=(20,10))



############
## Cases
############

## marker size
ms = 10

## County Cases
cases_cty, = plt.plot(ds_cty.index,ds_cty.values,
                        marker='o',markersize=ms, color='blue',
                        label = 'Cases (County)')



## Municipality Cases
cases_muni, = plt.plot(ds_municipality.index,ds_municipality.values,
                      marker='o',markersize=ms, color='red',
                      label = 'Cases (%s)' %(municipality))


############
## Bounds
############

## Line width
lw = 4




## County bounds
two_day_cty,= plt.plot(first_last_day_cty,two_day_double_cty,
                       ls='--',  color='red',linewidth = lw,
                       label = 'Two day doubling')
three_day_cty,= plt.plot(first_last_day_cty,three_day_double_cty,
                         ls=':',  color='red', linewidth = lw,
                         label = 'Three day doubling')


## Municipality Bounds
two_day_muni,= plt.plot(first_last_day_muni,two_day_double_muni,
                         ls='--',markersize=ms, color='blue',linewidth = lw,
                         label = 'Two day doubling')
three_day_muni,= plt.plot(first_last_day_muni,three_day_double_muni,
                           ls=':', markersize=ms, color='blue', linewidth = lw,
                           label = 'Three day doubling')


############
## Plot Aesthetics
############
plt.yscale('log')
ax.get_yaxis().set_major_formatter(tck.ScalarFormatter())
ax.yaxis.set_tick_params(labelsize=20)
ax.yaxis.grid(b=True,which='major')
plt.ylabel('Number of Confirmed Cases',fontsize=18)

## make the upper bound of y axis an order higher than latest state confirmed cases

y_up = int(10**(np.floor(np.log10(ds_cty.values[-1]*10))))

plt.ylim((1, y_up))
ax.ticklabel_format(axis='y',style='plain')

#ax.get_yaxis().set_major_formatter(tck.ScalarFormatter())

ax.xaxis.set_tick_params(labelsize=20)
plt.xticks(rotation=45)
plt.xlabel('Date',fontsize=18)

############
## Legends and Title
############

##Font size
fs = 18

case_legend = plt.legend(handles=[cases_cty,cases_muni],
                         loc=(.008,.877),fontsize=fs,markerfirst = False)
for handle in case_legend.legendHandles: handle.set_linestyle("")
plt.gca().add_artist(case_legend)

bound_legend = plt.legend(handles=[two_day_cty,three_day_cty],
                          loc=(0.008,.7),fontsize=fs,markerfirst = False)
for handle in bound_legend.legendHandles:  handle.set_color('black')
plt.gca().add_artist(bound_legend)



plt.title('COVID-19 in Onondaga County / %s' %(municipality),fontsize=fs)



plt.savefig('covid_in_%s.png'%(municipality),dpi=300)


# In[ ]:
