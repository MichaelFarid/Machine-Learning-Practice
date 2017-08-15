import math

data=[]
data.append([1,0,0,0])
data.append([1,0,1,0])
data.append([1,1,1,0])
data.append([1,3,1,0])
data.append([1,4,1,0])
data.append([1,4,0,0])
data.append([1,0,4,1])
data.append([1,0,3,1])
data.append([1,1,3,1])
data.append([1,3,3,1])
data.append([1,4,3,1])
data.append([1,4,4,1])


def updateThetas(thetaValues, data,alpha):
    calcy = []
    tempsum = 0;
    for i in range(0, len(data)):
        for j in range(0, len(thetaValues)):
            tempsum += thetaValues[j] * data[i][j]
        tempsum=1/(1+math.exp(-1*tempsum))
        calcy.append(tempsum)
        tempsum = 0
    newTheta=[]
    for i in range(0, len(thetaValues)):
        tempAdjust=0;
        for j in range(0, len(data)):
            tempAdjust+=(calcy[j]-data[j][len(data[0])-1])*data[j][i]
        adjustedTheta=thetaValues[i]-tempAdjust*alpha/len(data)
        newTheta.append(adjustedTheta)
    return newTheta

thetas=[5,3,4]

for i in range(0,10000):
    thetas=updateThetas(thetas,data,0.5)

print(thetas)
x=99
y=2

print(1/(1+math.exp(-1*(thetas[0]+thetas[1]*x+thetas[2]*y))))