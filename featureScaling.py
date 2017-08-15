def meanScaling(list):
    min=list[0]
    max=list[0]
    sum=0
    for i in list:
        if i>max:
            max=i
        if i<min:
            min=i
        sum+=i
    range=max-min
    avg=sum/len(list)
    result=[]
    for i in list:
        result.append((i-avg)/range)
    return result

mine=[-10000,15,30,15,100000000]
print(meanScaling(mine))
