import pandas as pd

# read csv file
df = pd.read_csv('filename.csv')

column1=df['GeneIDs']
print("temp:",column1)

# select the column you want to split
column2 = df['Seq']

# split the column by the newline character
split_column = column2.str.split('\n', expand=True)

# access the first part of the split column
first_part = split_column[0]
print("1stpart:",first_part)

# access the second part of the split column
second_part = split_column[1]


# remove newline characters from the second part
second_part = second_part.str.replace('\n', '')
print("2ndpart:",second_part)

#print(len(column1))

emptylist=[]
mainlist=[]

x=0
for x in range(len(column1)):
  #print(column1[x])

  emptylist.append(column1[x])
  emptylist.append(first_part[x])
  emptylist.append(second_part[x])

  print(emptylist)
  mainlist.append(emptylist)
  emptylist=[]

# Create the pandas DataFrame
df = pd.DataFrame(mainlist, columns=['GeneIDs','Header','Seq'])

# Save dataframe as csv file in the current folder
df.to_csv('filename2nd.csv', index = False, encoding='utf-8')

# print dataframe.
print(df)