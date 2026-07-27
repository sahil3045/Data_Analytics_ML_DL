#Pandas is a powerful and popular Python library designed for data manipulation (cleaning, transforming, and structuring data) and data analysis (finding patterns, trends, and insights).
#• It simplifies working with structured datasets like tables, spreadsheets, or time-series data
'''
Series: A Series is a one-dimensional labeled array that can hold any data type: integers, floats, strings, or even Python objects. Each element in the Series has a unique label called an index.
It is often used to track changes or patterns over time, such as daily temperatures, stock prices, or sales revenue.
'''

import pandas as pd 
#read data from a csv file into a dataframe 

df = pd.read_csv("leads-100.csv")
#print(df)

#dfxl = pd.read_excel("file_example_XLS_50.xls")
#print(dfxl)

dfj = pd.read_json("config-package.json")
#print(dfj)




#head(), tail()
#print("displaying top 10 rows ")
#print(df.head(10)) #if you dont mention 10 then it takes by dafult 5


#print("displaying bottom 10 rows ")
#print(df.tail(10))


'''
now for understanding the data 
you should know 
1 - columns, rows
2 - what type of data is present 
3 - missing data 

for this we have info()
method 
1 - no of rows and columns 
2 - column names 
3 - data types presnet 
4 - non null counts 
5 - memory usage of the dataframe 

'''

#now displaying the info of the dataset t
print(df.info())
