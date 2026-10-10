# Project Summary

## Objective

Identify the highest-performing New York City schools in this dataset using a transparent composite metric based on SAT performance and SAT participation.

## Dataset overview

- Raw rows: **435**
- Raw columns: **22**
- Schools with complete Math, Reading, and Writing SAT data: **375**

## Key descriptive statistics

- Mean Total SAT Score: **1275.91**
- Median Total SAT Score: **1226**
- Mean Percent Tested: **64.76%**
- Correlation, Total SAT vs Percent Tested: **0.606**

## Composite metric

The project uses:

`Success Score = 0.70 × normalized SAT + 0.30 × normalized SAT participation`

The 70/30 weighting is an analytical choice, not a parameter learned from the data. A sensitivity analysis with 50/50, 80/20, and 90/10 alternatives showed that the top of the ranking remained highly stable.

## Final top 10

|    | School Name                                                           | Borough       |   Total SAT Score |   Percent Tested Numeric |   Success Score 100 |
|---:|:----------------------------------------------------------------------|:--------------|------------------:|-------------------------:|--------------------:|
|  1 | Stuyvesant High School                                                | Manhattan     |              2144 |                     97.4 |               99.04 |
|  2 | Staten Island Technical High School                                   | Staten Island |              2041 |                     99.7 |               93.98 |
|  3 | Bronx High School of Science                                          | Bronx         |              2041 |                     97   |               92.99 |
|  4 | Townsend Harris High School                                           | Queens        |              1981 |                     97.1 |               89.58 |
|  5 | High School of American Studies at Lehman College                     | Bronx         |              2013 |                     91.8 |               89.47 |
|  6 | Queens High School for the Sciences at York College                   | Queens        |              1947 |                     97.9 |               87.92 |
|  7 | Baccalaureate School for Global Education                             | Queens        |              1881 |                     98.5 |               84.36 |
|  8 | Brooklyn Technical High School                                        | Brooklyn      |              1896 |                     95.5 |               84.11 |
|  9 | High School for Mathematics, Science, and Engineering at City College | Manhattan     |              1889 |                     92.6 |               82.64 |
| 10 | New Explorations into Science, Technology and Math High School        | Manhattan     |              1859 |                     91   |               80.33 |

## Interpretation caveat

“Best” is operationalized here as **high SAT performance with strong SAT participation**. This is not a complete measure of school quality. Graduation rates, student growth, college outcomes, resources, admissions selectivity, and other contextual factors are not included. Demographic correlations are descriptive only and should not be interpreted as causal or as statements about individual students.
