import numpy as np
import pandas as pd
# import matplotlib.pylab as plt
import matplotlib as plt
from matplotlib import pyplot

# reading csv into memory  *****************************************************************************************
# filename = "imports-85.data"
# wrong url 403 
# "https://gitlab.com/ibm/skills-network/courses/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/-/raw/master/labs/Data%20files/automobile.csv?inline=false"
# valid url
url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

# headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# read the dataframe from url using headers
df = pd.read_csv(url, names = headers)   # heeader=None    # df.columns = headers

# seeing the dataframe  ********************************************************************************************
# print n first rows
#print(df.head(10))

# list clolumn datatypes
print(df.dtypes)

# get satistical summary per each column
#print(df.describe())

# get satistical summary per each column
# print(df.describe(include="all"))

# You can select the columns of a data frame by indicating the name of each column 
# print(df[['length', 'compression-ratio']].describe())
# print(df[["length", "compression-ratio"]].describe())

# It provide a concise summary of your DataFrame.
# print(df.info)

# Standarizing the unknowns  ***************************************************************************************
# replace "?" to NaN   
df.replace("?", np.nan, inplace = True)
# print(df.head(5))

# making a True False dataframe
# missing_data = df.isnull()
# print(missing_data.head(5))   those with True are missing

# Count missing values in each column
# for column in missing_data.columns.values.tolist():
#     print(column)
#     print (missing_data[column].value_counts())
#     print("") 

# Dealing with missing data   **************************************************************************************
# replacing missing values with mean
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
# print("Average of normalized-losses:", avg_norm_loss)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

# which values are present in a particular column
# print(df['num-of-doors'].value_counts())

# to get the most common value to later replace Nan for this value
# print(df['num-of-doors'].value_counts().idxmax())

# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

# convert data types to proper format
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

# Data Standardization  **************************************************************************************************************
# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]

# Dara Normalization  ****************************************************************************************************************
# replace (original value) by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()

# Binning   **************************************************************************************************************************
print("Binning ...")

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

df[["horsepower"]] = df[["horsepower"]].astype(int)   # copy=True default

plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
plt.pyplot.show()

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins

group_names = ['Low', 'Medium', 'High']

df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)

df["horsepower-binned"].value_counts()

pyplot.bar(group_names, df["horsepower-binned"].value_counts())

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
plt.pyplot.show()

# Bins visualization
a = (0,1,2)

# draw historgram of attribute "horsepower" with bins = 3
plt.pyplot.hist(df["horsepower"], bins = 3)

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
plt.pyplot.show()

# Indicator variable (or dummy variable)  ********************************************************************************************************
# get indicator variables and assign it to data frame "dummy_variable_1"
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
print(dummy_variable_1.head())

# merge data frame "df" and "dummy_variable_1" 
df = pd.concat([df, dummy_variable_1], axis=1)

# drop original column "fuel-type" from "df"
df.drop("fuel-type", axis = 1, inplace=True)
print(df.head())



# Exporting to another files *********************************************************************************************************************
df.to_csv("automobile.csv", index=False)
# df.to_json("automobile.json", index=False)
# df.to_excel("automobile.xlsx", index=False)
# df.to_hdf("automobile.hdf", index=False)
# df.to_sql("automobile.sql", index=False)
