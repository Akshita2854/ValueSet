import pandas
import json
from pymongo import MongoClient
import pprint

client = MongoClient('localhost:27017')
db = client.Demo
def view_valueset(valueset):
    df=pandas.read_excel("/Users/akshita/Desktop/Valueset2018.xlsx")
    df.drop(["Value Set Version","Value Set OID","Definition","Code System OID","Code System Version"],axis=1,inplace=True)
    df1=df.loc[df['Value Set Name']==valueset]
    a1=df1.groupby(['Value Set Name'])['Code'].apply(list)
    a2=df1.groupby(['Code System'])['Code'].apply(list)
    df2=pandas.DataFrame({'Value Set Name':a1.index, 'Code':a1.values})
    df3=pandas.DataFrame({'Code System':a2.index, 'Code':a2.values})
    df2.set_index("Value Set Name",inplace=True)
    df3.set_index("Code System",inplace=True)
    df3.to_json("data.json")
    make_connection()

def make_connection():
    data= json.load(open("data.json"))

    db.Collection1.insert(data)
    view_codes()
def view_codes():
    for i in db.Collection1.find():
        pprint.pprint(i)
