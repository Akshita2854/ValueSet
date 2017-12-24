import pandas
import json
from pymongo import MongoClient
import pprint

df=pandas.read_excel("/Users/akshita/Desktop/Valueset2018.xlsx")
df.drop(["Value Set Version","Value Set OID","Definition","Code System OID","Code System Version"],axis=1,inplace=True)

def func1(value_set_name):
    if df['Value Set Name'].str.contains(value_set_name).any():
        print "if"
        df1=df.loc[df['Value Set Name']==value_set_name]
        a2=df1.groupby(['Code System'])['Code'].apply(list)
        df3=pandas.DataFrame({'Code System':a2.index, 'Code':a2.values})
        df3.set_index("Code System",inplace=True)
        df3.to_json("data.json")
        data= json.load(open("data.json"))
        return data
    elif df['Value Set Name'].str.contains(value_set_name.upper()).any():
        print "elif"
        df1=df.loc[df['Value Set Name']==value_set_name.upper()]
        a2=df1.groupby(['Code System'])['Code'].apply(list)
        df3=pandas.DataFrame({'Code System':a2.index, 'Code':a2.values})
        df3.set_index("Code System",inplace=True)
        df3.to_json("data.json")
        data= json.load(open("data.json"))
        return data


    elif (df['Value Set Name'].str.contains(value_set_name.title()).any()):
        print "elif2"
        df1=df.loc[df['Value Set Name']==value_set_name.title()]
        # print df1
        a2=df1.groupby(['Code System'])['Code'].apply(list)
        df3=pandas.DataFrame({'Code System':a2.index, 'Code':a2.values})
        df3.set_index("Code System",inplace=True)
        df3.to_json("data.json")
        data= json.load(open("data.json"))
        return data
