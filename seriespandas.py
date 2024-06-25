import pandas as pd
ser=pd.Series([1,2,3,4,5])
print(ser)

ser3=pd.Series([i for i in range(1,5)],index=['a','b','c','d'])
print(ser3)
print(ser3.c)

print(ser3['d'])

# Using of loc and iloc

print(ser3.loc['b'])
print(ser3.loc[['b','a']])  #it allows multiple values from their keys
print(ser3.iloc[[0,3]])

#slicing in series

print (ser3.loc['a':'c'])
print (ser3.loc[::2])

srr=pd.Series([10,20,30,40,50,60],index=['abc','xyz','jkl','mno','qpr','def'])
print(srr.loc['xyz':'qpr'])

#add and update the value using loc

srr.loc['def']=67
print(srr)

srr.loc['efg']=70
print(srr)


# using of at and iat

print(srr.at['abc'])   # it is faster than loc and iloc
print(srr.iat[3])

#print(srr.iat[['abc','efg']]) it shows error it not acess multiple values as loc and iloc

# another series method

seri=pd.Series((10,20,30,40))   # tuple shows series but set will not
print(seri)

stu={
   "name":"Abhishek",
   "age" : "20",
   "marks":["80","95","89"]
}

ser4=pd.Series(stu)
print(ser4)

seii=pd.Series(stu,index=['name','marks','adress','shoesize'])
print(seii)

print(seii.drop('marks')) # it remove the temporary
print(seii)

seii.drop('marks',inplace=True) # it will remove the permanent 
print(seii)

# change the type of series

ser=pd.Series([10,20,30,40])
ser=ser.astype('float')
print(ser)

# basic number operations

serii=pd.Series([10,33,4,8999,345,2,45])
print(serii.max())

print(serii.min())
print(serii.mean())
print(serii.mode()[0])
print(serii.median())
