# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)
gender_count=data['Gender'].value_counts()
gender_count.plot.bar()


# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
ax=alignment.plot.pie()
ax.set_title('Character Alignment')


# --------------
#Code starts here
sc_df=pd.DataFrame([data.Strength,data.Combat]).transpose()
sc_covariance=sc_df.cov().iloc[0,1]
sc_strength=data['Strength'].std()
sc_combat=data['Combat'].std()
sc_pearson=sc_df.corr().iloc[0,1]
ic_df=pd.DataFrame([data.Intelligence,data.Combat]).transpose()
ic_covariance=ic_df.cov().iloc[0,1]
ic_intelligence=data['Intelligence'].std()
ic_combat=data['Combat'].std()
ic_pearson=ic_df.corr().iloc[0,1]


# --------------
#Code starts here
total_high=data['Total'].quantile(q=0.99)
super_best=data[data['Total']>total_high]
super_best_names=list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3)=plt.subplots(3,sharex=True, sharey=True)
ax_1=plt.boxplot(x=data['Intelligence'])



