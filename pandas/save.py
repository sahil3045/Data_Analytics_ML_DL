import pandas as pd 

data = { 
    "Name" : ["Sahil", "Rohan", "Shivam"],
    "Age" : ["21", "21", "21"],
    "City" : ["Mumbai", "Mumbai", "Mumbai"]

}

df = pd.DataFrame(data)
print(df)

#now saving a dataframe to csv file 
df.to_csv("Output.csv", index = False) #index no is removed and file looks clean 

#now for saving it to excel file
#df.to_excel("Output.xlsx")

#now for saving it to json file
#df.to_json("output.json")


