import pandas as pd

# data=pd.DataFrame([1,2,3],index=[1,2,3])
# data.index.name="Index"
# print(data)

# data= [['a',1],['b',2],['c',3],['d',4],]
# df=pd.DataFrame(data,columns=['letter','No'])

# df['to']=[1,2,3,4]

# print(df)




Grade={"Name": ["rashmi", "harsh", 'ganesh', 'priya', 'vivek'], 'Grade': ['A1','A1', 'A1','B1','A1']}

gr=pd.DataFrame(Grade)
gr["percentage"]=[92,89,50,95,68]
gr.columns=["Name","percentage","Grade"]
gr["activity"]=["dancing","singing","sleaping","doing","playing"]
gr.loc[5]=["moni","c1",80,"gaming"]
gr=gr.drop(5,axis=0)
# gr=gr.drop("Grade",axis=1)
print(gr)


