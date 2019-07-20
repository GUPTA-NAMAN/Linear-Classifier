import csv
import math
import random

file = open("iris2.csv","r")  ;
csv_file = csv.reader(file) ;



def Zet_fun(input,parameter) :
    sum=parameter[0] ;
    # print("here")
    for i in range(4) :
        # print(input[i])
        sum=sum +   float(input[i])*parameter[i+1]
    return 1/(1+(math.e**(-sum))) ;






input1 = [] ;
output = [] ;
name=[]
answer = 0 ;
nr=0 ;
first=True

for row in csv_file :
    if first==False :
        nr=nr+1
        temp = [] ;
        for i in range(4) :
            temp.append(float(row[i])) ;
        input1.append(temp) ;
        name.append(row[4])
        if (row[4]=="Iris-setosa") :
            output.append(1) ;
            answer=answer + 1
        else :
            output.append(0) ;
    first =False


for i in range(4) :
    sum=0
    for j  in range(len(output)) :
        sum=input1[j][i]+sum
    av=sum/len(output)
    sum=0
    for j in range(len(output)) :
        sum = sum + (input1[j][i]-av)**2
    var=math.sqrt(sum/(len(output)-1))
    for j in range(len(output)) :
        input1[j][i]=(input1[j][i]-av)/var




parameter=[0,0,0,0,0]
temp=[0,0,0,0,0]
learing_rate = 0.01
decay_rate=0.01
size=len(output)





for iteration in range(100) :
    print(parameter)
    hvp=[]
    ls=0
    for i in range(size) :
        hvp.append(Zet_fun(input1[i],parameter) - output[i] )

    for i in range(5) :
        loss=0
        for j in range(size) :
            if i !=0 :
                loss = loss + hvp[j]*input1[j][i-1]
            else :
                loss= loss + hvp[j]

        temp[i]=temp[i] - loss*learing_rate - decay_rate*temp[i]


    for i in range(5) :
        parameter[i] = temp[i]

index=0
for  index in range(size) :
    print(index)
    print(Zet_fun(input1[index],parameter))
    print(output[index])
        

