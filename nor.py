import pandas as pd
import numpy as np
data1=pd.read_excel("nor1.xlsx")
df1=pd.DataFrame(data1)

def em1(min,max,newmin,newmax,val,c,f):
    x=[]
    #min=1
    #max=100
    #newmin=1
    #newmax=15
    for v in val:
        u = (v - min)/(max-min) * (newmax-newmin) + newmin
        x.append(np.round(u))
    #print(x)
    df=pd.DataFrame(x,columns=[c])
#print(df)
    df.to_excel(f,index=False,header=True)
em1(1,15,1,100,df1["S1"],"S1",'./nor12.xlsx')
em1(1,10,1,100,df1["S2"],"S2",'./nor13.xlsx')
em1(1,15,1,100,df1["S3"],"S3",'./nor34.xlsx')