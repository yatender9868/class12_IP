import pandas as pd
import numpy as np

#empty series
a=pd.Series()
print(a)

a=pd.Series(["golu","rohan","aawhan"])
a.index.name="No."
print(a)


b=pd.Series(["yatender", "golu", 'mayank'],index=[1,2,3])
print(b)
print(b[0:2])

name=["yatender", "golu", 'mayank']
index=[1,2,3]
name=pd.Series(name,index)
print(name)


dictionary=pd.Series({1:"golu",
                      2:"mayank",
                      3:"anand"})

print(dictionary[1:3])
print(dictionary[1])

# using range and for loop
s1=pd.Series(range(1,11),index=[i for i in "abcdefghij"])
print(s1)

# mathematical functions
s=np.arange(1,11)
index=(s*2)
s=pd.Series(index,s)
print(s)
print(s.index)
print(s.values)
print(s.size)
print(s.empty)
print(s.head(2))
print(s.head(-2))
print(s.tail(4))
print(s.tail(-4))



a=pd.Series([2,4,6],index=[0,1,2])
b=pd.Series([1,3,5],index=[1,2,3])


ab=pd.Series(a+b)
abmul=pd.Series(a*b)
print(ab)
print(abmul)

s=pd.Series([1,3,1])
print(s**3)
print(s*3)

