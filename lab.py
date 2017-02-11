import pandas as pd

a={'col_1':[2,5,1],
        'col_2':[10,3,11],
        'col_3':[8,12,9]}
a=pd.DataFrame.from_dict(a)

b={'col_1':[1,2,3],
        'col_2':[4,5,6],
        'col_3':[7,8,9]}
b=pd.DataFrame.from_dict(b)
print(b)



# x=pd.concat([a,b,b],keys=[1,2,3],axis=1)
# g=x.sort_values(by=x.keys())
# print(g)
# print(x["a"])
# print(x)
# print(a)
# a=a.sort_values(by='col_1')
# print(a)
# print(b)
# print(b.reindex(a.index))

