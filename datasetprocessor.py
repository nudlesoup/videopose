import pandas as pd
x1=pd.read_csv("/home/nudlesoup/Research/datasets/Chadataset/CharadesEgo/CharadesEgo_v1_train_sorted.csv")
print(x1.head())
x2=x1[['id','actions']]
print(x2.head())

x3= x2['actions'].str.split(';',expand=True)
#print(x3)
x4=x2['id']
#print(x4)
result = pd.concat([x4, x3], axis=1, join='inner')
#print(result)
result1=result.values.tolist()
#print(result1)
sub=result1
#
# def qPart( array, low,  high):
#     if (len(str(array[high]).split(" "))) == 3:
#         pivot = float(str(array[high]).split(" ")[1])
#         i = low-1
#         for j in range(low,high):
#             if float(str(array[j]).split(" ")[1]) < pivot:
#              i=i+1
#              if i != j:
#                  array[i], array[j] = array[j], array[i]
#
#         i=i+1
#         array[i], array[high] = array[high], array[i]
#
#         return i
#     else:
#         return
#
# def myQsort( array,low, high) :
#   if low < high :
#     p = qPart(array, low, high)
#     myQsort(array,low, p-1)
#     myQsort(array,p+1, high)
#
#
#
# def sortAllExceptKth( array):
#
#     l = len(array)
#     for i in range(0, l):
#         m = len(array[i])
#         index=i
#         k=m
#         for j in range (0,m):
#             if array[index][j] == "None" or array[index][j]=="nan":
#                 k=j
#                 break
#         z=min(k,m)
#         if z>=2:
#             myQsort(array[i], 1, z-1)
#

#sub=result1
def Sort(sub):
    l = len(sub)
    for i in range(0, l):
        m=len(sub[i])
        for j in range(0, m):
            for k in range(0, m):
             if len(str(sub[i][j]).split(" "))==3 and len(str(sub[i][k]).split(" "))==3:
              n=str(sub[i][k]).split(" ")
              # if(len(n)==3):
              #   print(n)
              o=n[1]
              #print(o)
              count=0
              p=str(sub[i][j]).split(" ")
              q=p[1]
              if (float(o) > float(q)):
                tempo = sub[i][j]
                sub[i][j]= sub[i][k]
                sub[i][k]= tempo
    return sub

subli=Sort(sub)

dfObj = pd.DataFrame(subli)
export_csv = dfObj.to_csv (r'export_dataframe_train.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
#print(subli)
#subli=sortAllExceptKth(sub)
#
# dfObj = pd.DataFrame(subli)
# export_csv = dfObj.to_csv (r'export_dataframe_train.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path