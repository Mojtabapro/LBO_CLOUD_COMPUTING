from Lib import *
from UseFiles import *

# arr = []
# x = setTasks( arr ,10 )
# x = setNodeClouds( arr ,5)
# x = setNodeFogs( arr ,5)

#x = makeMaxObject(Task ,11)

# maxNumber =10
# maxTasks = makeMaxObject( Task ,maxNumber )
# maxClouds = makeMaxObject( Node ,maxNumber )
# fgh =23
arr = []
xs = setNodeFogs(arr ,10)
x = setInitializeValueForNode(xs)
x = setPowerEfficiencyForNode(x)
x = setCostEfficiencyForNode(x)


for  i in  x:
    printObjectProperties(i)

k1 = getMaxPowerEfficiencyForNode(x)
k2 = getMaxCostEfficiencyForNode(x)


print (k1["value"] , k1["index"])
print (k2["value"] , k2["index"])

x = setCostEfficiencyNormalizationForNode(x , k1["value"])
x = setPowerEfficiencyNormalizationForNode(x , k1["value"])

for i in x :
    printObjectProperties(i)


MaxPowerEfficiencyFogs = getMaxPowerEfficiencyForNode(x)["value"]
MaxPowerEfficiencyClouds = getMaxPowerEfficiencyForNode(x)["value"]
