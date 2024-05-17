## ========================================================================
#   Ladybug Beetle Optimization (LBO) algorithm for cloud-fog
#
#   Developed in Python 3.10.11
#
#   Author and programmer: MojtabaBakhtar
#
#   Main paper:
#
#
# =========================================================================

from Lib import *
from UseFiles import *
from LadyBugAlgorithm import *
boolNumTask = True
numberTasks = None
while True:
    if boolNumTask:
        numberTasks = selectTask()
    ItemNumber = showMessageSelection()
    if ItemNumber == 1:
        print ("\n",Style.RESET_ALL,"Starting the code for algorithms...")
        i =1
        nruns =20
        finalValues = {'Makespan': 0 , 'engCons': 0 ,'procCost': 0 , 'fitValue': 0 ,}
        while nruns :
            values = LadyBugAlgorithm(1000,  numberTasks , 20 , 5 )
            finalValues =addValuesInNruns(finalValues , values)
            nruns -= 1
        nruns = 20
        printResults(finalValues,nruns)
        print ("\n",Style.RESET_ALL,"finish the code for algorithms")
        boolNumTask = True

    elif ItemNumber == 2:
        numberTasks = selectTask("again")
        boolNumTask = False

    elif ItemNumber == 3:
        print("\n",Fore.RED," you Exit the Program , GodBoy")
        quit()


