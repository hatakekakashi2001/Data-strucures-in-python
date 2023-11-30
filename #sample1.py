#sorted function
# a=[[1,6],[2,3],[-1,0],[-1,6]]
# b=sorted(a,key=lambda x:(x[1],x[0]))
# print(b)

#lambda function

# trial=lambda x,y: x*10+y*20 if x!=0 and y!=0 else 0

#map function 
# a=map(lambda x,y: x+y ,[1,2,3],[3,4])
# print(list(a))

#zip function
a=[1,2,3]
b=['a','b','c']
c=['x','y']
for i , j,k in zip(a,b,c):
    print(i,j,k)