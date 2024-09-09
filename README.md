# Exploratory-Data-Analysis
 Exploratory Data Analysis (EDA) is an essential step in the data 
analysis process that involves examining and summarizing 
datasets to better understand their underlying structure, 
patterns, and relationships. The primary goal of EDA is to gain 
insights into the data, identify potential issues, and develop a 
deeper understanding of the data's characteristics


#code
#importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("F:/carsdata/Toyota (1).csv") #importing data
cars=df.copy()
runfile('F:/data science data sets/project data science/data science.py', wdir='F:/data science data sets/project data science')
      Unnamed: 0  Price   Age     KM  ... Automatic    CC  Doors  Weight
0              0  13500  23.0  46986  ...         0  2000  three    1165
1              1  13750  23.0  72937  ...         0  2000      3    1165
2              2  13950  24.0  41711  ...         0  2000      3    1165
3              3  14950  26.0  48000  ...         0  2000      3    1165
4              4  13750  30.0  38500  ...         0  2000      3    1170
         ...    ...   ...    ...  ...       ...   ...    ...     ...
1431        1431   7500   NaN  20544  ...         0  1300      3    1025
1432        1432  10845  72.0     ??  ...         0  1300      3    1015
1433        1433   8500   NaN  17016  ...         0  1300      3    1015
1434        1434   7250  70.0     ??  ...         0  1300      3    1015
1435        1435   6950  76.0      1  ...         0  1600      5    1114

[1436 rows x 11 columns]
number of duplicate rows:  (0, 8)
Unnamed: 0      0
Price           0
Age           100
KM              0
FuelType      100
HP              0
MetColor      150
Automatic       0
dtype: int64
Unnamed: 0    0
Price         0
Age           0
KM            0
FuelType      0
HP            0
MetColor      0
Automatic     0
dtype: int64

cars.head(5)
Out[5]: 
   Unnamed: 0  Price   Age     KM FuelType  HP  MetColor  Automatic
0           0  13500  23.0  46986   Diesel  90       1.0          0
1           1  13750  23.0  72937   Diesel  90       1.0          0
3           3  14950  26.0  48000   Diesel  90       0.0          0
4           4  13750  30.0  38500   Diesel  90       0.0          0
5           5  12950  32.0  61000   Diesel  90       0.0          0

cars.head(5)
Out[6]: 
   Unnamed: 0  Price   Age     KM FuelType  HP  MetColor  Automatic
0           0  13500  23.0  46986   Diesel  90       1.0          0
1           1  13750  23.0  72937   Diesel  90       1.0          0
3           3  14950  26.0  48000   Diesel  90       0.0          0
4           4  13750  30.0  38500   Diesel  90       0.0          0
5           5  12950  32.0  61000   Diesel  90       0.0          0

cars.tail(5)
Out[7]: 
      Unnamed: 0  Price   Age     KM FuelType   HP  MetColor  Automatic
1425        1425   7950  80.0     ??   Petrol   86       1.0          0
1429        1429   8950  78.0  24000   Petrol   86       1.0          1
1430        1430   8450  80.0  23000   Petrol   86       0.0          0
1432        1432  10845  72.0     ??   Petrol   86       0.0          0
1435        1435   6950  76.0      1   Petrol  110       0.0          0

cars.dtypes
Out[8]: 
Unnamed: 0      int64
Price           int64
Age           float64
KM             object
FuelType       object
HP             object
MetColor      float64
Automatic       int64
dtype: object



cars=cars.drop(['Automatic'], axis=1)

cars.head(5)
Out[11]: 
   Unnamed: 0  Price   Age     KM FuelType  HP  MetColor
0           0  13500  23.0  46986   Diesel  90       1.0
1           1  13750  23.0  72937   Diesel  90       1.0
3           3  14950  26.0  48000   Diesel  90       0.0
4           4  13750  30.0  38500   Diesel  90       0.0
5           5  12950  32.0  61000   Diesel  90       0.0

cars=cars.rename(columns={"Unnamed":"sno"})

cars.head(5)
Out[13]: 
   Unnamed: 0  Price   Age     KM FuelType  HP  MetColor
0           0  13500  23.0  46986   Diesel  90       1.0
1           1  13750  23.0  72937   Diesel  90       1.0
3           3  14950  26.0  48000   Diesel  90       0.0
4           4  13750  30.0  38500   Diesel  90       0.0
5           5  12950  32.0  61000   Diesel  90       0.0


cars=cars.rename(columns={"sno":"Unnamed"})

cars.head(5)
Out[15]: 
   Unnamed: 0  Price   Age     KM FuelType  HP  MetColor
0           0  13500  23.0  46986   Diesel  90       1.0
1           1  13750  23.0  72937   Diesel  90       1.0
3           3  14950  26.0  48000   Diesel  90       0.0
4           4  13750  30.0  38500   Diesel  90       0.0
5           5  12950  32.0  61000   Diesel  90       0.0

cars=cars.rename(columns={"Price":"cost"})

cars.head(5)
Out[17]: 
   Unnamed: 0   cost   Age     KM FuelType  HP  MetColor
0           0  13500  23.0  46986   Diesel  90       1.0
1           1  13750  23.0  72937   Diesel  90       1.0
3           3  14950  26.0  48000   Diesel  90       0.0
4           4  13750  30.0  38500   Diesel  90       0.0
5           5  12950  32.0  61000   Diesel  90       0.0

cars.shape
Out[18]: (1111, 7)




duplicate_rows_cars = cars[cars.duplicated()]
print("number of duplicate rows: ", duplicate_rows_cars.shape)
number of duplicate rows:  (0, 7)

cars.count()
Out[22]: 
Unnamed: 0    1111
cost          1111
Age           1111
KM            1111
FuelType      1111
HP            1111
MetColor      1111
dtype: int64



cars=cars.drop_duplicates()

cars.head(5)
Out[25]: 
   Unnamed: 0   cost   Age     KM FuelType  HP  MetColor
0           0  13500  23.0  46986   Diesel  90       1.0
1           1  13750  23.0  72937   Diesel  90       1.0
3           3  14950  26.0  48000   Diesel  90       0.0
4           4  13750  30.0  38500   Diesel  90       0.0
5           5  12950  32.0  61000   Diesel  90       0.0

cars.count()
Out[26]: 
Unnamed: 0    1111
cost          1111
Age           1111
KM            1111
FuelType      1111
HP            1111
MetColor      1111
dtype: int64

print(cars.isnull().sum())
Unnamed: 0    0
cost          0
Age           0
KM            0
FuelType      0
HP            0
MetColor      0
dtype: int64

cars = cars.dropna() 
cars.count()
Out[28]: 
Unnamed: 0    1111
cost          1111
Age           1111
KM            1111
FuelType      1111
HP            1111
MetColor      1111
dtype: int64

plt.title('scatter plot price vs age')
plt.xlabel('Age(months)')
plt.ylabel('price(euros)')
plt.show()

plt.scatter(cars['Age'], cars['cost'],c='red')
Out[31]: <matplotlib.collections.PathCollection at 0x22fbb7ce890>


plt.title('histogram of kilometer')
plt.xlabel('kilometer')
plt.ylabel('frequency')
plt.show()
plt.hist(cars['KM'],color='green',edgecolor='green',bins=5)
Out[32]: 
(array([260., 220., 215., 214., 202.]),
 array([  0., 198., 396., 594., 792., 990.]),
 <BarContainer object of 5 artists>)

counts=[979,120,12]
FuelType=('petrol','diesel','cng')
index=np.arange(len(FuelType))
plt.bar(index,counts,color=['red','blue','cyan'])
Out[33]: <BarContainer object of 3 artists>
