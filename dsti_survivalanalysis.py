# -*- coding: utf-8 -*-
"""dsti_survivalanalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NPCQGlqV-ehiqhfCT1sOVuCjJeEnHgB6
"""

pip install scikit-survival

pip install lifelines

import pandas as pd
from sksurv.datasets import load_veterans_lung_cancer
import matplotlib.pyplot as plt
#from sksurv.nonparametric import kaplan_meier_estimator
import seaborn as sns
from lifelines import KaplanMeierFitter, CoxPHFitter
from lifelines.statistics import logrank_test
from sksurv.preprocessing import OneHotEncoder

df_x = load_veterans_lung_cancer()[0]
df_y = pd.DataFrame(load_veterans_lung_cancer()[1])

df_y.groupby(by='Status')['Survival_in_days'].count()

df_x.info()

df_x.describe()

df_x.isnull().sum()

sns.distplot(df_x['Age_in_years'])

sns.distplot(df_x['Karnofsky_score'])

sns.distplot(df_x['Months_from_Diagnosis'])

print(df_x.Celltype.unique())
print(df_x.Prior_therapy.unique())
print(df_x.Treatment.unique())

# Commented out IPython magic to ensure Python compatibility.
# Survival Function
# %matplotlib inline
kmf = KaplanMeierFitter()
kmf.fit(durations = df_y["Survival_in_days"], event_observed = df_y["Status"])
kmf.survival_function_.plot()
#kmf.plot_survival_function()
plt.ylabel("est. probability of survival $\hat{S}(t)$")
plt.xlabel("time $t$")
plt.title("Median Survival time is %d" %(kmf.median_survival_time_))

# Creating a function to identify survival function on basis of various categories
def plot_survival_function(column):
  kmf = KaplanMeierFitter()
  column_array = df_x[column].unique()
  for val in column_array:
    index = (df_x[column] == val)
    kmf.fit(durations = df_y["Survival_in_days"][index], event_observed = df_y["Status"][index], 
            label = "%s (n=%d)" %(val,index.sum()))
    kmf.plot_survival_function()
    print("Median of %s is %d" %(val,kmf.median_survival_time_))

  plt.ylabel("est. probability of survival $\hat{S}(t)$")
  plt.xlabel("time $t$")
  plt.title("Survival Curves on basis of %s" %(column))

plot_survival_function("Celltype")

plot_survival_function("Prior_therapy")

plot_survival_function("Treatment")

index = (df_x["Prior_therapy"] == 'yes')
results = logrank_test(df_y["Survival_in_days"][index],df_y["Survival_in_days"][~index],df_y["Status"][index],df_y["Status"][~index],alpha=0.95)
results.print_summary()

df_x_numeric = OneHotEncoder().fit_transform(df_x)
df_model = pd.concat([df_x_numeric,df_y],axis=1)
df_model.head()
df_model["Status"] = df_model["Status"].apply(lambda x: 1 if x== True else 0)
df_model.head()

#### Cox Proportional Hazards Model

# Survival Regression

# Cox Model

cph = CoxPHFitter()
cph.fit(df_model[['Prior_therapy=yes','Status','Survival_in_days']],'Survival_in_days',event_col = 'Status')
cph.print_summary()

index = (df_x["Treatment"] == 'test')
results = logrank_test(df_y["Survival_in_days"][index],df_y["Survival_in_days"][~index],
                       df_y["Status"][index],df_y["Status"][~index],
                       alpha=0.95)
results.print_summary()
print(results.p_value)       
print(results.test_statistic)

#### Cox Proportional Hazards Model

# Survival Regression

# Cox Model

cph = CoxPHFitter()
cph.fit(df_model[['Treatment=test','Status','Survival_in_days']],'Survival_in_days',event_col = 'Status')
cph.print_summary()

#### Cox Proportional Hazards Model

# Survival Regression

# Cox Model

cph = CoxPHFitter()
cph.fit(df_model[['Celltype=large','Celltype=smallcell','Celltype=squamous','Status','Survival_in_days']],'Survival_in_days',event_col = 'Status')
cph.print_summary()

#### Cox Proportional Hazards Model
# Survival Regression
# Cox Model

cph = CoxPHFitter()
cph.fit(df_model[['Age_in_years','Status','Survival_in_days']],'Survival_in_days',event_col = 'Status')
cph.print_summary()

df_model.head()

#### Cox Proportional Hazards Model
# Survival Regression
# Cox Model

cph = CoxPHFitter()
cph.fit(df_model[['Karnofsky_score','Status','Survival_in_days']],'Survival_in_days',event_col = 'Status')
cph.print_summary()

#### Cox Proportional Hazards Model
# Survival Regression
# Cox Model

cph = CoxPHFitter()
cph.fit(df_model[['Months_from_Diagnosis','Status','Survival_in_days']],'Survival_in_days',event_col = 'Status')
cph.print_summary()

cph = CoxPHFitter()
cph.fit(df_model,'Survival_in_days',event_col = 'Status')
cph.print_summary()

