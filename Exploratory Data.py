#importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("F:/carsdata/Toyota (1).csv") #importing data
cars=df.copy()


cars.head(5)
      

cars.head(5)
        

cars.tail(5)

cars.dtypes

cars=cars.drop(['Automatic'], axis=1)

cars.head(5)

cars=cars.rename(columns={"Unnamed":"sno"})

cars.head(5)



cars=cars.rename(columns={"Price":"cost"})

cars.head(5)


cars.shape





duplicate_rows_cars = cars[cars.duplicated()]
print("number of duplicate rows: ", duplicate_rows_cars.shape)







cars=cars.drop_duplicates()

cars.head(5)


cars.count()


print(cars.isnull().sum())

cars = cars.dropna() 
cars.count()

plt.title('scatter plot price vs age')
plt.xlabel('Age(months)')
plt.ylabel('price(euros)')
plt.show()

plt.scatter(cars['Age'], cars['cost'],c='red')



plt.title('histogram of kilometer')
plt.xlabel('kilometer')
plt.ylabel('frequency')
plt.show()
plt.hist(cars['KM'],color='green',edgecolor='green',bins=5)
