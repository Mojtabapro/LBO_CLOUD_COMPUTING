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
    parameters =6
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
    workedNodes = []
    population = []
    for i in tasks:
        population = []
        for j in nodes:
            makespanJ = j.getAvailableTime() +i.getSize()/j.getSpeedProcessing()*1000
            if makespanJ < minMakespan:
                minMakespan = makespanJ
            j.setMakeSpan(makespanJ)
            pop = {}
            pop['position'] = np.array([i.getSize(),j.getSpeedProcessing()
            ,j.getAvailableTime(),j.getProcessingFee(), j.getCostEfficiency()
            ,makespanJ]).tolist()
            pop['cost'] = sphere(j) #costfunc(p['position'])
            pop["idTask"] = i.getId()
            pop["idNode"] = j.getId()
            pop["typeNode"] = j.getTypeNode()
            population.append(pop)

        min = inf

        doTaskByNode =None
        chosenPerson = None
        for  i in population:
            if i['cost'] < min:
                chosenPerson = i
        doTaskByNode = {"idTask":chosenPerson['idTask'] ,
                        "idNode":chosenPerson["idNode"] ,
                        "typeNode":chosenPerson["typeNode"]}

        task = tasks[doTaskByNode['idTask']-1]
        tempNode  = getNodeForCompute(nodes,doTaskByNode)
        nodes = filterNodesForFetChanges(nodes , tempNode)


        dictionaryComputeTaskNode=compute(tempNode , task)
        nodes.append(dictionaryComputeTaskNode["Node"])
        doTasks.append(dictionaryComputeTaskNode["Task"])
    #nodes = normalizationByMakespan(nodes,minMakespan)
    finalClouds = list(filter(lambda node:  node.getTypeNode()==1, nodes))
    finalFogs = list(filter(lambda node:  node.getTypeNode()==2, nodes))



    mapResults=computeResults(doTasks, finalClouds, finalFogs , Coefficients)
    return mapResults










#     # plt.plot(out['bestcost'])
#     # plt.xlabel('NFE')
#     # plt.ylabel('Best Cost')
#     # plt.title('LBO algorithm')
#     # plt.grid(True)
#     # plt.show()







#             NFE +=1
#             if pop['cost'] < bestsol['cost']:
#                 bestsol['position'] = pop['position']
#                 bestsol['cost'] = pop['cost']
#                 bestsol["idTask"] = pop['idTask']
#                 bestsol["idNode"] = pop['idNode']
#                 bestsol["typeNode"] = pop["typeNode"]
#             for key, value in pop.items():
#                 print(key, value)

# ############# Start lbo algorithm for computing the best solution########
#     population.sort(key=lambda x: x["cost"] , reverse = True)

# Printing the sorted dictionary


#     Best Cost of Iterations
#     bestcost = []
#     bestcost.append(bestsol['cost'])
#     print(bestsol)

#     it = 0


#     main Loop
#     while NFE < npop:
#     # for it in range(maxit):

#         costs = np.array([x['cost'] for x in population])
#         SoC = sum(costs)
#         avg_cost = np.mean(costs)
#         if avg_cost != 0:
#             costs = costs/avg_cost
#         probs = np.exp(-beta*costs)

#         newSol = []
#         new = {}
#         #for i in range(npop):
#         new = {}
#         new['cost'] = inf
#         # Perform Roulette Wheel Selection
#         j=0

#         while (j<2*numberTasks/10 or j>max_NFE):
#             j=roulette_wheel_selection(probs)
#             print(j)
#         # Perform Crossover
#         if random.random()>0.2:
#             Rnd = np.random.random()-0.5
#             new['position'] = (np.array(population[j]['position'])
#             +np.array((np.random.random(size=(1, nvar))
#             *(np.array(population[j]['position'])-np.array(population[i]['position']))
#             .tolist()).tolist()[0])+np.array(
#             (np.random.random(size=(1, nvar))*
#             (np.array(population[j-1]['position'])-np.array(population[j]['position']))
#             .tolist()).tolist()[0])+
#             np.array(
#                 ([((abs(population[i]['cost']/SoC))**(-it/npop))*(Rnd)* el for el in
#             ([element for element in population[j]['position']])])
#             )
#             ).tolist()

#         else:
#             new['position'] = mutate(population[i], 0.05*nvar, sigma)


# ############# end lbo algorithm for computing the best solution########
