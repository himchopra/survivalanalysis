# survivalanalysis
Survival Analysis on Lung Cancer Trial was done as a project for DSTI

Survival Analysis Project: Students will need to perform a statistical analysis of a dataset of their choice, using any of the methods seen during the class, i.e.:
* nonparametric estimation of survival for one or more groups
* nonparametric comparison of 2 or more groups
* semi-parametric Cox regression

Dataset Chosen: The Veterans’ Administration Lung Cancer Trial. Source of the data is scikit library.
Dataset consists of 137 samples and 6 features
6 features are
a) Age_in_years : Datatype float : Min age 31, Max age 81, no null values
b) Celltype : Datatype category : 4 unique values ['squamous', 'smallcell', 'adeno', 'large']
c) Karnofsky_score : Datatype float
d) Months_from_Diagnosis : Datatype float
e) Prior_therapy : Datatype category: 2 unique values [‘no’,’yes’]
f) Treatment : Datatype category: 2 unique values [‘standard’,’test’]
Death was observed for 128 out of 137 patients (93.43%)
Observations
•	Median Survival days is 80 days

•	Median Survival days may differ on basis of cell type
•	Median of squamous is 118 days
•	Median of smallcell is 51 days
•	Median of adeno is 51 days
•	Median of large is 156 days
 
•	Median Survival days doesn’t differ on basis of Prior therapy
•	Median of no is 80
•	Median of yes is 82
 
•	Median Survival days differ on basis of Treatment
•	Median of standard is 103
•	Median of test is 52
 


Performing Statistical Analysis for various groups
Logrank test : Measures and reports that whether for two event series data generating processes are statistically different. This test-statistic is chi-squared under the null hypothesis. If survival functions cross, the logrank test will give inaccurate assessment.
1.	First log rank test is done for Prior Therapy: As we have observed earlier, the survival functions for “prior_treatment = Yes” and “prior_treatment = No” cross and hence logrank test is not the best evaluator. Nonetheless, trying it
p-value = 0.48 > 0.05 hence we fail to reject the null hypothesis. Hence, survival function of prior_treatment = Yes / No are not different.
As an alternative to logrank test, trying cox regression with only 1 variable, again we got p=0.48 which is revalidation of output from logrank test
Hence, Prior Therapy has not shown ability to predict cancer free survival time
2.	Log rank test for basis for Treatment: p-value of 0.93, hence groups are not statistically different at 95% confidence level. Same results are observed using both logrank_test and CoxPHFitter. Hence, treatment has not shown ability to predict cancer free survival time

3.	CoxPHFitter for Celltype : Following are the p-values for large, smallcell and squamous respectively <0.005, 0.56, 0.005. Hence, not all groups are statistically different. Same is observed through multivariate_logrank_test. Hence, Celltype has not shown ability to predict cancer free survival time

4.	Age_in_years : Again not significant. Hence, Age has not shown ability to predict cancer free survival time

5.	Karnofsky_score : Significant. Hence, karnofsky score has shown ability to predict cancer free survival time

References:
1.	https://lifelines.readthedocs.io/en/latest/index.html
2.	https://scikit-survival.readthedocs.io/en/stable/

