'''
1 - select specific column 
2 - filter rows
3 - combine multiple confitions 


for selecting specific columns 
col = df["Column 1", "col_2", "col3"]


now for filtering rows based on a single condition 
filtered_r = df[df["col"] > 50000]

now for multiple conditions 
filter_r = df[(df["Salary" > 50000]) & (df["Salary"] < 80000)]


'''
import pandas as pd

data  = { 
    "Name" : ["Sahil", "Manas", "Rohan", "Shivam", "Shoumik", "Shlok"],
    "Salary" : [90000, 80000, 75000, 45000, 55000, 60000]

}

df = pd.DataFrame(data)
print(df)


print(df["Salary"])


filer_r = df[(df["Salary"] > 50000)]
print(filer_r)

high_sal = df[df["Salary"] >= 90000] 
print(high_sal)

med_sal = df[(df["Salary"] > 60000) & (df["Salary"] < 90000)] 
print(med_sal)

# for or condition
or_sal = df[(df["Salary"] > 60000) | (df["Salary"] >=90000)]  
print(or_sal)