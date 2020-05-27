import pandas as pd
import re # Line 90

#https://www.dataquest.io/blog/pandas-cheat-sheet/

# Should give the path or both the script and file should be in the same location
df = pd.read_csv("pokemon_data_pandas.csv")
# # Retrives all the data
# print(df)
# print(df.head(3)) #Prints the top 3 rows by default it without parameter prints 5 rows
# print(df.tail(4)) #prints the last 4 rows
#
# # Read the xlxs format file
# df_xlsx = pd.read_excel("pokemon_data.xlsx")
# print(df_xlsx)
#
# # Read the tab seperated txt file
# df_tab = pd.read_csv("pokemon_data.txt", delimiter = '\t')
# print(df_tab)


##Read Headers
#print(df.columns) #Gives all the headers

##Read Column
#print(df["Name"]) #Gives all the data in name column
#print(df.Name) #Works the same way as above but donot work for two words
#print(df["Name"][0:5]) #Gives first 5 values
#print(df.Name[0:5]) #Works the same way as above
#print(df[['Name','Type 1','HP']])

##Read Row
#print(df.iloc[1]) #Gives a single row at location 1
#print(df.iloc[1:4]) #Gives rows 1-4


##Read a specific location (R,C)
#print(df.iloc[2,1]) #Prints the element in the 2nd row 1st column
# for index,row in df.iterrows(): #Iterates all the rows with index
#     print(index,row)
# for index,row in df.iterrows():
#     print(index,row['Name']) #Prints index and Name column

#print(df.loc[df["Type 1"]=="Fire"]) #Gives all the rows where Type 1 = "Fire"

#print(df.describe()) #Gives count,mean,std,min,max etc of integer columns

# print(df.sort_values("Name")) #sorts the data based on column "Name"
# print(df.sort_values("Name", ascending = False)) #Sorts in descending order
# print(df.sort_values(["Type 1","HP"])) #Sorting based on two columns
# print(df.sort_values(["Type 1","HP"], ascending = [1,0])) #True and False are represented by 1 and 0


##Calculations on the data
# df['Total'] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]
# print(df.head(5))
# df = df.drop(columns = ["Total"]) #Drops the specified column
# print(df.head())
df['Total'] = df.iloc[:,4:10].sum(axis=1) #Another way of doing total

#Rearranging columns
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(df.head())


# #Copy the data frame to the new file
# df.to_csv('Modified.csv') #Create new csv and copy
# df.to_csv('Modified.csv',index=False) #Not to save the indexes
#df.to_excel('Modified.xlsx',index=False) #To new excel file
#df.to_csv("Modified.txt",index=False,sep="\t") #To new txt file with tab seperated columns




# new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison" ) & (df["HP"] > 70)] ##Logic and on the Data frame
#
# new_df = new_df.reset_index() #Resets the index and saves the index as a new column
# new_df = new_df.reset_index(drop = True)
# print(new_df)
#
# another_df = df.loc[(df["Type 1"] == "Grass") | (df["Type 2"] == "Poison")] ##Logic or on the Data frame
# print(another_df[["Type 1","Type 2","HP"]])


# print(df.loc[df["Name"].str.contains("Mega")]) #Prints all the columns whose names have Mega

# print(df.loc[~df["Name"].str.contains("Mega")]) #Prints all the columns whose names doesn't have Mega

# print(df.loc[df["Type 1"].str.contains("fire|grass",flags = re.I, regex =True)]) #Prints all the columns whose Type 1 are Fire or Grass #regular expression is used for case sensitivity

# print(df.loc[df["Name"].str.contains("^pi[a-z]*",flags = re.I, regex =True)]) #ALl the names that start with pi


## Conditional Changes

# df.loc[df["Type 1"] == "Fire", "Type 1"] = "Flamer"
# print(df)
# df.loc[df["Type 1"] == "Fire", "Legendary"] = True #Compare type 1 column and change Legendary column
# print(df)
# df.loc[df["Total"] > 500, ["Generation","Legendary"]] = "Test Value" #Modify both columns as Test Value
# df.loc[df["Total"] > 500, ["Generation","Legendary"]] = ["Test 1","Test 2"] #Modify each column with separate value
# print(df)


## Aggregate  Statistics (Group by)

# print(df.groupby(["Type 1"]).mean()) #Groups by on column Type 1 and gives aggregate of all the integer columns
# print(df.groupby(["Type 1"]).mean().sort_values("Defense", ascending = False)) #Groupby type 1 column and then sort by defense column
# print(df.groupby(["Type 1"]).sum())
# print(df.groupby(["Type 1"]).count())
# print(df.groupby(["Type 1","Type 2"]).count()["Name"]) #Grouping by two columns and counting on one column



## Working with large datasets
# for df in pd.read_csv("Modified.csv",chunksize = 5):  #Loads the data in chunks
#     print("Chunk Size")
#     print(df)


## Take chunks of data group by and add them to new data frame
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv("Modified.csv",chunksize = 5):
    results = df.groupby(["Type 1"]).count()
    new_df = pd.concat([new_df,results],sort = True)

print(new_df)













