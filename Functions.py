from Lib import *
from NodeClass import *
from TaskClass import *
init()

def selectTask(param=""):
    print("\n",Fore.BLUE, "--------------------------------------------------", Fore.GREEN)
    text =param
    numberTasks = int(input(f"{Fore.CYAN}input number tasks for algorithm {text}: "))
    while numberTasks < 0:
        numberTasks = int( input(
            f"{Fore.RED}input number tasks for algorithm again (number task is negative): {Fore.CYAN}"))
    return numberTasks




def showMessageSelection(param=""):
    print("\n",Fore.BLUE, "--------------------------------------------------", Fore.RESET)
    print('[', Fore.GREEN, '1', Fore.RESET, ']: ', Fore.GREEN, "select LadyBug algorithm",
        Fore.RESET)
    print('[', Fore.YELLOW, '2', Fore.RESET, ']: ', Fore.YELLOW, "set Tasks",
        Fore.RESET)
    print('[', Fore.RED, '3', Fore.RESET, ']: ', Fore.RED, "Exit", Fore.RESET)
    print("\n")
    selectNumber = int(input(f"{Fore.CYAN}Select Item Number: "))
    while (selectNumber > 3 or selectNumber < 1) :
        selectNumber =int(
        input(f"{Fore.RED}input Select Item Number again (Item number is not valid): {Fore.CYAN}"))
    return selectNumber


def getRandomInteger():
    return random.randint(0,sys.maxsize - 1)

def setTasks(tasksArray = [], numberTasks = 10) :
    for i in range(1, numberTasks+1 , 1):
        task = Task()
        task.setId(i)
        rand = getRandomInteger()
        if rand % 3 == 0:
            task.setSize(getRandomInteger()% 9901 + 100) #[100,10000] MI
            task.setDeadline(getRandomInteger() % 401 + 100) #[100 , 500] ms
        elif rand % 3 == 1:
            task.setSize(getRandomInteger()% 3253 + 1028) #[1028,4280] MI
            task.setDeadline(getRandomInteger() % 2001 + 500) #[500 , 2500] ms
        elif rand % 3 == 2:
            task.setSize(getRandomInteger()% 4662 + 5123) #[5123,9784] MI
            task.setDeadline(getRandomInteger() % 7501 + 2500) #[2500 , 10000] ms
        task.setMemory(getRandomInteger()%151 + 50)  #[50 , 200] MB
        task.setPenalty(getRandomInteger()%50 + 1)
        task.setQoS((getRandomInteger() % 1000 + 9000) / 100.0 )
        task.setInputFileSize(getRandomInteger() % 9901 + 100) ## [100kB , 10MB]
        task.setOutPutFileSize(getRandomInteger() % 991 + 1) ## [1kB , 1MB]
        tasksArray.append(task)
        #printObjectProperties(task)
    return tasksArray





def printObjectProperties(object):
    properties = vars(object)
    for key, value in properties.items():
        print(Fore.YELLOW , key,Fore.CYAN, ":",Fore.GREEN, value )
    print(Fore.RESET,'\n')



def setNodeClouds(nodeArray = [] , numberNodeClouds = 20):
    delayValue = getRandomInteger() %301 + 200
    for i in range(1, numberNodeClouds + 1 , 1):
        node = Node()
        node.setId(i)
        node.setTypeNode(1)# for CloudNode
        node.setSpeedProcessing(getRandomInteger() % 2001 +300) # [3000 , 5000] MIPS
        node.setMemory(getRandomInteger()% 57345 + 8192) #[8192,65536] MB
        node.setSpeedInternet(getRandomInteger() % 9901 + 100) #[100 , 10000] Mbps
        node.setProcessingFee((getRandomInteger()% 31 + 79) / 100) #[0.7,1] G&ps
        node.setDelay(delayValue) #[200 , 500] ms
        node.setPowerMax(getRandomInteger()% 201 + 200) #[200,400] w
        node.setPowerMin( node.getPowerMax() *0.6) #[40,100] w
        nodeArray.append(node)
        # printObjectProperties(node)
    return nodeArray




def setNodeFogs(fogArray = [] , numberFogs = 5):
    for i in range(1, numberFogs + 1 , 1):
        node = Node()
        node.setId(i)
        node.setTypeNode(2) # for fogNode
        node.setSpeedProcessing(getRandomInteger() % 1001 +500) # [500 , 1500] MIPS
        node.setMemory(getRandomInteger()% 8193 + 512) #[512,8192] MB
        node.setSpeedInternet(getRandomInteger() % 991 + 10) #[10 , 1000] Mbps
        node.setProcessingFee((getRandomInteger()% 31 + 10) / 100) #[0.1,0.4] G&ps
        node.setDelay(getRandomInteger() % 10 + 1) #[1 , 10] ms
        node.setPowerMax(getRandomInteger()% 61 + 40) #[40,100] w
        node.setPowerMin( node.getPowerMax() *0.6) #[40,100] w
        fogArray.append(node)
    # printObjectProperties(node)
    return fogArray



def  makeMaxObject(objectName ,  maxNumberObject):
    maxInstances = [objectName() for i in range(0 ,maxNumberObject)]
    # for i in maxInstances:
    #     printObjectProperties(i)
    return maxInstances


def setInitializeValueForNode(nodeArray):

    for i in range(0,len(nodeArray)):
        nodeArray[i].setAvailableTime(0.0)
        nodeArray[i].setEnergy(0.0)
        nodeArray[i].setProcessCast(0.0)
    return nodeArray

def setPowerEfficiencyForNode(nodeArray):
    for i in range(0 , len(nodeArray)):
        nodeArray[i].setPowerEfficiency(nodeArray[i].getSpeedProcessing() / nodeArray[i].getPowerMax())
    return nodeArray
def setCostEfficiencyForNode(nodeArray):
    for i in range(0 ,len(nodeArray)):
        nodeArray[i].setCostEfficiency(nodeArray[i].getSpeedProcessing() / nodeArray[i].getProcessingFee())
    return nodeArray

def getMaxPowerEfficiencyForNode(nodeArray):
    indexOfMaxPowerEfficiency = 0
    ValueOfMaxPowerEfficiency = 0
    for i in range( 0 , len(nodeArray)):
        if( nodeArray[i].getPowerEfficiency() > ValueOfMaxPowerEfficiency) :
            ValueOfMaxPowerEfficiency = nodeArray[i].getPowerEfficiency()
            indexOfMaxPowerEfficiency = i
    return {'value': ValueOfMaxPowerEfficiency, 'index':indexOfMaxPowerEfficiency}


def getMaxCostEfficiencyForNode(nodeArray):
    indexOfMaxCostEfficiency = 0
    ValueOfMaxCostEfficiency = 0
    for i in range( 0 , len(nodeArray)):
        if( nodeArray[i].getCostEfficiency() > ValueOfMaxCostEfficiency ) :
            ValueOfMaxCostEfficiency = nodeArray[i].getCostEfficiency()
            indexOfMaxCostEfficiency = i
    return {'value': ValueOfMaxCostEfficiency, 'index':indexOfMaxCostEfficiency}



def setPowerEfficiencyNormalizationForNode(nodeArray, MaxValue):
    for i in range( 0 , len(nodeArray)):
        normalPowerEfficiency =nodeArray[i].getPowerEfficiency() / MaxValue
        nodeArray[i].setPowerEfficiency(normalPowerEfficiency)
    return nodeArray
def setCostEfficiencyNormalizationForNode(nodeArray, MaxValue):
    for i in range( 0 , len(nodeArray)):
        normalCostEfficiency =nodeArray[i].getCostEfficiency() / MaxValue
        nodeArray[i].setCostEfficiency(normalCostEfficiency)
    return nodeArray


def compute(Node , Task):

    timeExecute = Task.getSize() / Node.getSpeedProcessing()
    Node.setAvailableTime( Node.getAvailableTime() +( timeExecute *1000 ))
    Task.setResponse (Node.getAvailableTime() + Node.getDelay())
    Task.setIsDone(True)
    Node.setProcessCast (Node.getProcessCast() + timeExecute * Node.getProcessingFee() )

    Computes = {"Node": Node , "Task": Task}

    return Computes

def computeResults(tasks, clouds, fogs , Coefficients  ) :
    violationCost = 0
    PDST = 0
    totalPenalty =0
    sumExe = 0
    avgExe = 0
    minExe = 10000
    for i in tasks:
        temp = 0
        diffResponseAndDelay =  i.getResponse()  - i.getDeadline()
        if  diffResponseAndDelay >  0:
            temp  = diffResponseAndDelay
            totalPenalty += temp
        else : PDST + 1
    tempq = temp * 100/ i.getDeadline() + i.getQoS() - 100
    if tempq > 0 :
        violationCost += (tempq *i.getPenalty())


    Makespan =0
    for i in clouds:
        availableTime = i.getAvailableTime()
        if  availableTime > Makespan:
            Makespan = i.getAvailableTime()
        if availableTime < minExe :
            minExe = availableTime
        sumExe += availableTime

    for i in fogs:
        availableTime = i.getAvailableTime()
        if  availableTime > Makespan:
            Makespan = i.getAvailableTime()
        if availableTime < minExe :
            minExe = availableTime
        sumExe += availableTime

    avgExe = sumExe / (len(fogs) + len(clouds) )


    DI =0
    
    DI = 1.0 * (Makespan - minExe) / avgExe

    engCons = 0
    procCost = 0

    for i in fogs:
        energy = i.getAvailableTime() / 1000 * i.getPowerMax()
        + (Makespan /1000 - i.getAvailableTime()/ 1000 ) * i.getPowerMin()

        i.setEnergy(energy)
        engCons += i.getEnergy()
        procCost += i.getProcessCast()


    for i in clouds :
        energy = i.getAvailableTime() / 1000 * i.getPowerMax()
        + (Makespan /1000 - i.getAvailableTime()/ 1000 ) * i.getPowerMin()

        i.setEnergy(energy)
        engCons += i.getEnergy()
        procCost += i.getProcessCast()

    totalTaskSize = 0
    for i in tasks:
        totalTaskSize += i.getSize()
    totalCPU = 0
    for i in fogs:
        totalCPU += i.getSpeedProcessing()
    for i in clouds:
        totalCPU += i.getSpeedProcessing()

    minMakespan = 1.0 * totalTaskSize / totalCPU

    MaxPowerEfficiencyFogs = getMaxPowerEfficiencyForNode(fogs)["value"]
    MaxPowerEfficiencyClouds = getMaxPowerEfficiencyForNode(clouds)["value"]

    min_engCons =0
    if MaxPowerEfficiencyFogs > MaxPowerEfficiencyClouds :
        index = getMaxPowerEfficiencyForNode(fogs)["index"]
        min_engCons = 1.0 * totalTaskSize/fogs[index].getSpeedProcessing() * fogs[index].getPowerMax()

    else :
        index = getMaxPowerEfficiencyForNode(clouds)["index"]
        min_engCons = 1.0 * totalTaskSize/clouds[index].getSpeedProcessing() * clouds[index].getPowerMax()



    MaxCostEfficiencyFogs= getMaxCostEfficiencyForNode(fogs)["value"]
    MaxCostEfficiencyClouds = getMaxCostEfficiencyForNode(clouds)["value"]
    min_procCost = 0
    if MaxCostEfficiencyFogs > MaxCostEfficiencyClouds :
        index = getMaxCostEfficiencyForNode(fogs)["index"]
        min_procCost = 1.0 * totalTaskSize/fogs[index].getSpeedProcessing() * fogs[index].getProcessingFee()

    else :
        index = getMaxCostEfficiencyForNode(clouds)["index"]
        min_procCost = 1.0 * totalTaskSize/clouds[index].getSpeedProcessing() * clouds[index].getProcessingFee()


    fitValue = 0
    fitValue = (Coefficients['processingFee'] *min_engCons/engCons +
       Coefficients['costEfficiency'] * min_procCost/procCost  +
       Coefficients['makeSpan']   * minMakespan/Makespan * 1000)


    sumMakespan = Makespan/1000
    sumEngConst = engCons
    sumProcessCost = procCost
    sumFitValue = fitValue

    mapResult = { 'Makespan': sumMakespan , 'engCons': sumEngConst ,
    'procCost': sumProcessCost , 'fitValue': sumFitValue ,}


    return mapResult


def printResults(results, Nruns=1.0):
    
    print(Fore.BLUE,"\n\n---------------RESULTS---------------")
    for key, value in results.items():
        print("     "+f"{Fore.CYAN}{key}",Fore.MAGENTA," : ",Fore.GREEN,F"{value/Nruns}")
    print(Fore.BLUE,"---------------RESULTS---------------\n\n")







def sphere(Node, Coefficients = {'processingFee': 0.25,'costEfficiency': 0.25 ,'makeSpan': 0.5, }):
    return (Coefficients['processingFee'] * Node.getProcessingFee()
    + Coefficients['costEfficiency'] * Node.getCostEfficiency()
    + Coefficients['makeSpan'] * Node.getMakeSpan())






def mutate(x, mu, sigma):
    y = {}
    y['position'] = x['position']
    flag = np.random.rand(len(x['position'])) <= mu
    ind = np.argwhere(flag)
    index = [i[0] for i in ind]
    addingValue = [sigma*elmnt for elmnt in
    [i[0] for i in np.random.randn(*ind.shape).tolist()]]
    count=0
    for k in index:
        y['position'][k] += addingValue[count]
        count +=1

    return y['position']

def apply_bound(x, varmin, varmax):
    # print(x.position)
    x['position'] = np.maximum(x['position'], varmin).tolist()
    x['position'] = np.minimum(x['position'], varmax).tolist()
    return x

def roulette_wheel_selection(p):
    c = np.cumsum(p)
    r = sum(p)*np.random.rand()
    ind = np.argwhere(r <= c)
    print(ind[0][0])
    return ind[0][0]

def getNodeForCompute(Nodes,doTaskByNode):
    node = None
    for node in Nodes:
        if node.getId() == doTaskByNode["idNode"] and node.getTypeNode() == doTaskByNode["typeNode"]:
            return node
    return node


def normalizationByMakespan( nodes , minMakespan):
    for i in range(0 , len(nodes)):
        makespan =nodes[i].getMakeSpan()
        nodes[i].setMakeSpan( makespan / minMakespan)

    return nodes


def filterNodesForFetChanges(nodes , targetNode):
    finalNode = []
    for i in nodes :
        if (i.getId() == targetNode.getId()):
            if i.getTypeNode() == targetNode.getTypeNode():
                continue
        finalNode.append(i)
    return finalNode


def addValuesInNruns(finalValues , values) :
    for key  , value in values.items():
        finalValues[key] = finalValues.get(key, 0) + value
    return finalValues