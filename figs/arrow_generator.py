# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:22:57 2023

@author: byungkiryu
"""



from matplotlib import pyplot as plt
import numpy as np




text1u = 'Solute in bulk'
text1d = 'Segregation'+'\n'+'at surface'
text10 = 'No interaction'

def drawdraw():
    figsize = (1.6, 3.0)
    fig, ax = plt.subplots(figsize=figsize)
    color1, color2 =  'blue', 'red'
    # ax.scatter(2,2)
    ax.set_xlim(-1.5, 6)
    ax.set_ylim(-4,4)
    
    xarrow, yarrow = 0, 2.5
    xarrow2, yarrow2 = 0, 0
    ax.plot([-1,1],[0,0],color='black',linewidth=1)
    
    
    
    # textleftvalue = 0
    ax.text(-1.8,0,'0',va='center')
    ax.text(1.3, 0, text10,ha='left',va='center')
    ax.text(-0.2,+(yarrow)+.5,text1u,color=color1,ha='left',va='bottom')
    ax.text(-0.2,-(yarrow)-.5,text1d,color=color2,ha='left',va='top')      
    ax.annotate('',xy=(xarrow,+yarrow),xytext=(xarrow2,+yarrow2+0.1),
                # arrowprops={'arrowstyle': '-|>','color':color1}, 
                arrowprops={'color':color1,'facecolor':None,'alpha':0.8}, 
                ha='center', va='center',color='grey')
    ax.annotate('',xy=(xarrow,-yarrow),xytext=(xarrow2,-yarrow2-0.1),
                # arrowprops={'arrowstyle': '-|>','color':color2}, 
                arrowprops={'color':color2,'facecolor':None,'alpha':0.8}, 
                ha='center', va='center')
    # plt.tight_layout()
    plt.axis('off')
    
text1u = 'Solute in bulk'
text10 = ''
text1d = 'Segregation\n'+'at surface'
drawdraw()
plt.savefig('arrow_Segregation_energy.pdf')
plt.savefig('arrow_Segregation_energy.png',dpi=300)



text1u = 'Agglomeration'
text10 = 'No'+'\n'+'interaction'
text1d = 'Repulsive\n'+'interaction'
drawdraw()
plt.savefig('arrow_Binding_energy.pdf')
plt.savefig('arrow_Binding_energy.png',dpi=300)
