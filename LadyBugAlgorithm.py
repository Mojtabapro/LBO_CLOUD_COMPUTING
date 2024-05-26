from lib import *
from UseFiles import *

def LadyBugAlgorithm( maxNumber = 1000, numberTasks = 25 , numberFog = 20 , numberClouds = 5 ):
    nRun = 25
    # ## maxTasks = makeMaxObject( Task ,maxNumber )
    # maxClouds = makeMaxObject( Node ,maxNumber )
    # maxFogs = makeMaxObject(Node ,maxNumber )

    arr = []
    tasks = setTasks(arr ,numberTasks)
    # for i in tasks :
    #     printObjectProperties(i)

    # print("tasks-----------------------------------\n")
    arr = []
    fogs = setNodeFogs(arr , numberFog)

    arr = []
    clouds = setNodeClouds(arr , numberClouds)

    for i in range(0,numberTasks):
        tasks[i].setResponse(0.0)

    clouds = setInitializeValueForNode(clouds)
    fogs = setInitializeValueForNode(fogs)

    clouds = setPowerEfficiencyForNode(clouds)
    clouds = setCostEfficiencyForNode(clouds)
    mapMaxPowerEfficiencyForClouds = getMaxPowerEfficiencyForNode(clouds)
    mapCostEfficiencyForClouds= getMaxCostEfficiencyForNode(clouds)

    fogs = setPowerEfficiencyForNode(fogs)
    fogs = setCostEfficiencyForNode(fogs)
    mapMaxPowerEfficiencyForFogs = getMaxPowerEfficiencyForNode(fogs)
    mapCostEfficiencyForFogs= getMaxCostEfficiencyForNode(fogs)

    clouds = setPowerEfficiencyNormalizationForNode(clouds,mapMaxPowerEfficiencyForClouds['value'] )
    clouds = setCostEfficiencyNormalizationForNode(clouds,mapCostEfficiencyForClouds['value'])

    fogs = setPowerEfficiencyNormalizationForNode(fogs,mapMaxPowerEfficiencyForFogs['value'] )
    fogs = setCostEfficiencyNormalizationForNode(fogs,mapCostEfficiencyForFogs['value'])




    Coefficients = {'processingFee': 0.25,'costEfficiency': 0.25 ,'makeSpan': 0.5 }
    # Problem Definition

    #tasks.sort(key=lambda task : task.getSize())
    nodes  = clouds + fogs

# nodes.sort(key=lambda node : node.speedProcessing)
    parameters = 7
    problem = {}
    problem['costfunc'] = sphere
    problem['nvar'] = parameters
    # problem['varmin'] = -100
    # problem['varmax'] =  100

    # GA Parameters
    params = {}
    params['max_NFE'] = numberTasks * len(nodes)
    params['npop'] = numberTasks
    params['beta'] = 8
    params['sigma'] = 0.05

    # Run GA
    NFE=0

    # Problem Information
    costfunc = problem['costfunc']

    nvar = problem['nvar']
    # varmin = problem['varmin']
    # varmax = problem['varmax']

    # Parameters
    max_NFE= params['max_NFE']
    npop = params['npop']
    npop_init = npop
    beta = params['beta']
    sigma = params['sigma']

    # Best Solution Ever Found
    bestsol = {}
    bestsol['position'] = [0] * npop
    bestsol['cost']= np.inf
    bestsol["idTask"] = 0
    bestsol["idNode"] = 0
    bestsol["typeNode"] = 0

    #print (bestsol)
    # Initialize Population
    doTasks = []
    minMakespan = np.inf
    mincost = np.inf
    pop = {}
    population = []


    for i in range(0,len(tasks)):
        for j in range(0, len(nodes)):
            makespanJ = nodes[j].getAvailableTime() + (tasks[i].getSize()/nodes[j].getSpeedProcessing()*1000)
            if makespanJ < minMakespan:
                minMakespan = makespanJ
            nodes[j].setMakeSpan(makespanJ)
            pop['position'] = np.array([tasks[i].getSize(),
                                        nodes[j].getSpeedProcessing(),
                                        nodes[j].getAvailableTime(),
                                        nodes[j].getProcessingFee(),
                                        nodes[j].getPowerEfficiency(),
                                        nodes[j].getCostEfficiency(),
                                        # add makespan
                                        ]).tolist()
            pop["idTask"] = tasks[i].getId()
            pop["idNode"] =  nodes[j].getId()
            pop["typeNode"] =  nodes[j].getTypeNode()
            pop["cost"] = 0
            population.append(pop)
            pop ={}

        nodes = normalizationByMakespan( nodes , minMakespan)
        for i in population:
            getNode = {"idNode":i["idNode"] ,
                        "typeNode":i["typeNode"]}
            nodeforcost  = getNodeForCompute(nodes,getNode)
            i['cost'] =1/sphere(nodeforcost)
            i["position"].append(nodeforcost.getMakeSpan())
            if i['cost'] < mincost:
                    mincost = i['cost']

        min = mincost
        doTaskByNode =None
        chosenPerson = None
        doTaskByNode = None
        for  i in population:
            if i['cost'] <= min:
                chosenPerson = i
                doTaskByNode = {"idTask":chosenPerson['idTask'] ,
                        "idNode":chosenPerson["idNode"] ,
                        "typeNode":chosenPerson["typeNode"]}
        task = tasks[doTaskByNode['idTask']-1]
        tempNode  = getNodeForCompute(nodes,doTaskByNode)
        # nodes = filterNodesForFitChanges(nodes , tempNode)

        dictionaryComputeTaskNode=compute(tempNode , task)
        #nodes.append(dictionaryComputeTaskNode["Node"])
        nodes=filterNodesForFitChanges(nodes , dictionaryComputeTaskNode["Node"])
        tasks =filterTasksForFitChanges(tasks, dictionaryComputeTaskNode["Task"] )

        doTasks.append(dictionaryComputeTaskNode["Task"])

        mincost = np.inf
        population = []
        pop ={}
        minMakespan= np.inf



    #nodes = normalizationByMakespan(nodes,minMakespan)
    finalClouds = list(filter(lambda node:  node.getTypeNode()==1, nodes))
    finalFogs = list(filter(lambda node:  node.getTypeNode()==2, nodes))

    listMaxPE = {
            'indexCloud' : mapMaxPowerEfficiencyForClouds['index'],
            "valueCloud":mapMaxPowerEfficiencyForClouds['value'],
            'indexFog':mapMaxPowerEfficiencyForFogs['index'],
            "valueFog":mapMaxPowerEfficiencyForFogs['value']
    }

    listMaxCE = {
            'indexCloud':mapCostEfficiencyForClouds['index'],
            "valueCloud":mapCostEfficiencyForClouds['value'],
            'indexFog':mapCostEfficiencyForFogs['index'],
            "valueFog":mapCostEfficiencyForFogs['value']
    }

    mapResults=computeResults(doTasks, finalClouds, finalFogs , Coefficients, listMaxPE , listMaxCE)
    return mapResults
