'''
Python Project - Marvel Mart Project
Dien Vo
March 14,2020
'''

import pandas as pd
import csv 
import numpy as np

# Part 1: Cleaning the data

data= pd.read_csv('DataSamples/Marvel_Mart_Sales_Project_Master.csv',delimiter= ',')

empty1= data['Country'].isnull()
print(empty1.sum())
#check if are empty cells in country columns since no missing value 

data["Country"]= data["Country"].replace("154.06", "NULL")
data["Country"]= data["Country"].replace("437.2", "NULL")
data["Country"]= data["Country"].replace("651.21", "NULL")
data["Country"]= data["Country"].fillna("NULL")

# changing number as string to Null

#Item Type

print(data['Item Type'].isnull().sum())
# check if there are empty cell in Item type

data['Item Type'].fillna("NULL",inplace= True)
#fill those cells with Null string

#Order priority

print(data['Order Priority'].isnull().sum())
# find out if are there any empty cell 

data['Order Priority'].fillna("NULL", inplace= True) 
# fill empty cell with Null String

print(data['Order ID'].isnull().sum())

#try pd.to_numeric(data['Order ID'], errors= 'coerce').fillna(0) (idk why this dont work when save to other csv)
data["Order ID"]= data["Order ID"].replace("Snacks", 0)
data["Order ID"]= data["Order ID"].replace("Meat", 0)
data["Order ID"]= data["Order ID"].replace("Fruits", 0)     
data["Order ID"]= data["Order ID"].replace("Cosmetics", 0)   
# replace  strings with 0

#export to csv file
data.to_csv('DataSamples/Marvel_Mart_Sales_clean.csv', index= False)

  
# Part 2: General Statistics

#1(A)

data2= pd.read_csv('DataSamples/Marvel_Mart_Sales_clean.csv')
#read clean csv

count1= data2.groupby("Country").size()
#group coutry and county number of transaction by counting how many time it repeated 

ranking = count1.nlargest(n=10)
#ranking country by find the largest 10

dat1=pd.DataFrame({"Country":ranking.index,
              "Transactrion":ranking[0:10]})
# but result in tro dataframe


with open("DataSamples/Marvel_Mart_Ranking.txt","w+") as writer:
    writer.writelines("Countries Most Transactions: ")
#open and write first line to txt file
    
dat1.to_csv("DataSamples/Marvel_Mart_Ranking.txt", sep= '\t', index=False)
# export dataframe to txt file

with open("DataSamples/Marvel_Mart_Ranking.txt","a+") as writer:
    writer.writelines("\nThe country we should build our shipping center is Cape Verde because it has more transaction than Maldives where we had already got a shipping center in")
#append the comment 

with open("DataSamples/Marvel_Mart_Ranking.txt","a+") as writer:   
    writer.writelines("\nWe can also build our shipping center in the rest country below Maldives since the gap in transactions is small")
#append comments
    
#1(B)

countOnline= data2[data2["Sales Channel"] == 'Online']
countOffline= data2[data2["Sales Channel"] =='Offline']
# counting online and off line  


with open("DataSamples/Marvel_Mart_Ranking.txt","a+") as writer:  
    writer.write(f"\n {'OnlineSalses':<20}: {len(countOnline)}")
    writer.writelines(f"\n {'OfflineSalses':<20}: {len(countOffline)}")
    writer.writelines("\nBase on the statistic above, the online order is more than offline which we should take more online order than offline.")
    writer.writelines("\nHowever, because the gap is not so big, offline order still be necessary.")
    
#C
data2= pd.read_csv('DataSamples/Marvel_Mart_Sales_clean.csv')
#  read csv file
yearRank=data2['Order Date']
yearRank=yearRank.str.slice(-4,len('Order Date'))
# take year slice to see how many year
yearRank=yearRank.drop_duplicates()

yearRank=yearRank.sort_values(ascending=False)    
'''
for i in yearRank:
    for k in data2['Total Profit']:
        if i== 2015:
           yearRank[i].append(sum(data2['Total Profit']))     
        if i== '2016'
           yearRank[i].append(sum(data2['Total Profit'][k])) 
        if i== '2017' and k == '2017':
           yearRank[i].append(sum(data2['Total Profit'][k]))
        if i== '2014' and k == '2014':
            yearRank[i].append(sum(data2['Total Profit'][k])) 
        if i== '2013' and k == '2013':
            yearRank[i].append(sum(data2['Total Profit'][k])) 
        if i== '2012' and k == '2012':
            yearRank[i].append(sum(data2['Total Profit'][k])) 
        if i== '2011' and k == '2011':
            yearRank[i].append(sum(data2['Total Profit'][k])) 

data2 = data2.groupby([0])[1].sum()
'''
               
#2

data3= pd.read_csv('DataSamples/Marvel_Mart_Sales_clean.csv')
#read csv

#Sum
sumUnitsSold= data3["Units Sold"].sum(axis=0, skipna=True)
sumUnitCost=data3["Unit Cost"].sum(axis=0,skipna= True)
sumTotalRev=data3["Total Revenue"].sum(axis=0,skipna=True)
sumTotalCost=data3["Total Cost"].sum(axis=0,skipna= True)
sumTotalProfit=data3["Total Profit"].sum(axis=0,skipna= True)
# suming data to get the total 

#Avg
avgUnitsSold=data3["Units Sold"].mean(axis=0, skipna=True)
avgUnitCost=data3["Unit Cost"].mean(axis=0, skipna=True)
avgTotalRev=data3["Total Revenue"].mean(axis=0, skipna=True)
avgTotalCost=data3["Total Cost"].mean(axis=0, skipna=True)
avgTotalProfit=data3["Total Profit"].mean(axis=0, skipna=True)

#take average of each column 

#Max
maxUnitsSold=data3["Units Sold"].max(axis=0, skipna=True)
maxUnitsSold=data3["Unit Cost"].max(axis=0, skipna=True)
maxTotalRev=data3["Total Revenue"].max(axis=0, skipna=True)
maxTotalCost=data3["Total Cost"].max(axis=0, skipna=True)
maxTotalProfit=data3["Total Profit"].max(axis=0, skipna=True)
# find max of each column using max function


with open("DataSamples/Marvel_Mart_Calc.txt","w+") as writer:
#open csv with write mode to write a new text file 
    writer.write("Sum: ")
    writer.write(f"\n {'Units Sold':<20}: {(sumUnitsSold)}")
    writer.write(f"\n {'Unit Cost':<20}: {(sumUnitCost)}")
    writer.write(f"\n {'Total Revenue':<20}: {(sumTotalRev)}")
    writer.write(f"\n {'Total Cost':<20}: {(sumTotalCost)}")
    writer.write(f"\n {'Total profit':<20}: {(sumTotalProfit)}")
    writer.write("\n")
    writer.write("\nAverage: ")
    writer.write(f"\n {'Units Sold':<20}: {(avgUnitsSold)}")
    writer.write(f"\n {'Unit Cost':<20}: {(avgUnitCost)}")
    writer.write(f"\n {'Total Revenue':<20}: {(avgTotalRev)}")
    writer.write(f"\n {'Total Cost':<20}: {(avgTotalCost)}")
    writer.write(f"\n {'Total profit':<20}: {(avgTotalProfit)}")
    writer.write("\n")
    writer.write("\nMax: ")
    writer.write(f"\n {'Units Sold':<20}: {(maxUnitsSold)}")
    writer.write(f"\n {'Unit Cost':<20}: {(maxUnitsSold)}")
    writer.write(f"\n {'Total Revenue':<20}: {(maxTotalRev)}")
    writer.write(f"\n {'Total Cost':<20}: {(maxTotalCost)}")
    writer.write(f"\n {'Total Profit':<20}: {(maxTotalProfit)}")
# write line into txt file with data calculated line by line with new line each time
    

#Part 3 Cross Refernce Statistic
 
data4= pd.read_csv('DataSamples/Marvel_Mart_Sales_clean.csv') 
#read csv file

sort= data4.sort_values("Region",axis=0, ascending=False, inplace=True)
#sort csv by region in desc order

region= data4["Region"]
country=data4["Country"]
# create two series from csv

dict1= {"Region":list(region),
        "Country":list(country)}
# convert 2 series to dict

regiondat=pd.DataFrame(dict1)
# put dict into dataframe

regiondat=regiondat.drop_duplicates()
#group dataframe by region

regiondat.set_index("Region",inplace=True)
#setting region as first index
regiondat=regiondat.dropna()

asia= []
midAndNa=[]
na=[]
caatc=[]
subSAfrica=[]
ausAOceania=[]
europe=[]
# create list of each region

reglist= ['Asia','Middle East and North Africa','North America','Central America and the Caribbean','Sub-Saharan Africa','Australia and Oceania','Europe']
# list of all region

for i in regiondat:
    for k,v in regiondat[i].items():
        if (k == "Asia"):
            asia.append(v)   
        if (k == "Middle East and North Africa"):
            midAndNa.append(v)
        if(k=='North America'):
            na.append(v)
        if (k=="Central America and the Caribbean"):
            caatc.append(v)
        if (k== "Sub-Saharan Africa"):
            subSAfrica.append(v)
        if(k== "Australia and Oceania"):
            ausAOceania.append(v)
        if (k== "Europe"):
            europe.append(v)
# append countries into each region by append them to each list if meet condition 
         
#convert to drop duplicated
newList1=set(list(asia))   
asia=list(set(newList1))  

newList2=set(list(midAndNa))   
midAndNa=list(set(newList2))  

newList3=set(list(caatc))   
caatc=list(set(newList3))  

newList4=set(list(subSAfrica))   
subSAfrica=list(set(newList4))  

newList5=set(list(ausAOceania))   
ausAOceania=list(set(newList5)) 

newList6=set(list(europe))   
europe=list(set(newList6))  

newList7=set(list(na))   
na=list(set(newList7))  
# convert to drop dupplicated. Because the set function will auto cut down the same value

'''
#my tries 
finalDat= pd.DataFrame(list(zip[asia,midAndNa,caatc,subSAfrica,ausAOceania,europe],columns =['Asia','Middle East and North Africa','North Africa','Central America and the Caribbean','Sub-Saharan Africa','Australia and Oceania','Europe'],index=0))            


finalDict={"Asia": list(asia),
           "Middle East and North Africa":list(midAndNa),
           "Central America and the Caribbean":list(caatc),
           "North America": list(na),
           "Sub-Saharan Africa":list(subSAfrica),
           "Australia and Oceania":list(ausAOceania),
     "Europe":list(europe)}

finalDict={i:[a,b,c,d,e,f] for i,a,b,c,d,e,f,h in zip(list(reglist),list(asia),list(na),list(midAndNa),list(caatc),list(subSAfrica),list(ausAOceania),list(europe))}

mydict={}
for reg in reglist:
    if(reg == "Asia"):
        mydict[reg]=list(asia)
    if(reg=="Middle East and North Africa"):
       mydict[reg]=list(midAndNa)
    if(reg== "North America"):
       mydict[reg]= list(na)
    if(reg=='Central America and the Caribbean'):
        mydict[reg]=list(caatc)
    if(reg=='Sub-Saharan Africa'):
        mydict[reg]=list(subSAfrica)
    if(reg=='Australia and Oceania'):
        mydict[reg]=list(ausAOceania)
    else:
        mydict[reg]=list(europe)

mydat=pd.DataFrame.from_dict(mydict,orient='index')

mydat.dropna()
myfinaldat=mydat.transpose()

mydat.to_csv("DataSamples/Countries_By_Region2.csv",index=False)

'''
dicta ={"Asia":list(asia)}    
dictb ={"Middle East and North Africa":list(midAndNa)}  
dictc ={"North America":list(na)}  
dictd ={"Central America and the Caribbean":list(caatc)}  
dicte ={"Sub-Saharan Africa":list(subSAfrica)}  
dictf ={"Australia and Oceania":list(ausAOceania)}  
dicth ={"Europe":list(europe)}  
#create dict with the key are region and value are list of country 
# the reason for splitting up is to concat them all as dataframe

data=pd.DataFrame(dicta,index=None)
datb=pd.DataFrame(dictb,index=None)
datc=pd.DataFrame(dictc,index=None)
datd=pd.DataFrame(dictd,index=None)
date=pd.DataFrame(dicte,index=None)
datf=pd.DataFrame(dictf,index=None)
dath=pd.DataFrame(dicth,index=None)
#create datta frame from dict, assign each dict to dataframe 

final_row=pd.concat([data,datb,datc,datd,date,datf,dath],axis=1)
#concat dataframes together and with same column. 
'''
with open ("DataSamples/Countries_By_Region1.csv","w+") as a:
    data.to_csv(a,header=False)
# write to csv file    
with open ("DataSamples/Countries_By_Region1.csv","a+") as a:
    datb.to_csv(a,header=False,)
    datc.to_csv(a,header=False)
    datd.to_csv(a,header=False)
    datf.to_csv(a,header=False)
    dath.to_csv(a,header=False)
''' 
final_row.to_csv("DataSamples/Countries_By_Region.csv",index=False)  
# export to csv using no index 