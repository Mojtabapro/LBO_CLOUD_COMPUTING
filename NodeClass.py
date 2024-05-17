

class Node:
    def __init__(self):
        self.id = None
        self.typeNode = None
        self.speedProcessing = 0   # [MIPS] is unit
        self.memory = 0            # [MB] is unit
        self.speedInternet = 0     # [Mbps] is unit
        self.availableTime = 0     # [ms] is unit
        self.delay = 0             # [ms] is unit
        self.powerEfficiency = 0   # [Watt] is unit
        self.costEfficiency = 0    # [MIPS/G&ps] is unit
        self.processingFee = 0      # G$ps is unit
        self.powerMin = 0
        self.powerMax = 0
        self.makeSpan = 0           # [ms] is
        self.energy = 0             # [ws or j] is unit
        self.processCast = 0        #[s/MIPS*G&ps] is unit
        self.fitnessValue = 0       # [probably ms] is unit
    ################################################################
    def getId(self):return self.id
    def setId(self, id):self.id = id
    ################################################################
    def getTypeNode(self):return self.typeNode
    def setTypeNode(self, typeNode):self.typeNode = typeNode
    ################################################################
    def getSpeedProcessing(self):return self.speedProcessing
    def setSpeedProcessing(self,speedProcessing):
        self.speedProcessing = speedProcessing
    ################################################################
    def getMemory(self):return self.memory
    def setMemory(self,memory): self.memory = memory
    ################################################################
    def getSpeedInternet(self): return self.speedInternet
    def setSpeedInternet(self,speedInternet): self.speedInternet = speedInternet
    ################################################################
    def getAvailableTime(self):return self.availableTime
    def setAvailableTime(self,availableTime): self.availableTime = availableTime
    ################################################################
    def getDelay(self):return self.delay
    def setDelay(self,delay): self.delay = delay
    ################################################################
    def getPowerEfficiency(self):return self.powerEfficiency
    def setPowerEfficiency(self,powerEfficiency):
        self.powerEfficiency =powerEfficiency
    ################################################################
    def getCostEfficiency(self): return self.costEfficiency
    def setCostEfficiency(self,costEfficiency):
        self.costEfficiency = costEfficiency
    ################################################################
    def getProcessingFee(self):return self.processingFee
    def setProcessingFee(self,processingFee):
        self.processingFee =processingFee
    ################################################################
    def getPowerMin(self) : return self.powerMin
    def setPowerMin(self,powerMin) : self.powerMin = powerMin
    ################################################################
    def getPowerMax(self) : return self.powerMax
    def setPowerMax(self,powerMax) : self.powerMax = powerMax
    ################################################################
    def getMakeSpan(self) : return self.makeSpan
    def setMakeSpan(self,makeSpan) : self.makeSpan = makeSpan
    ################################################################
    def getEnergy(self) : return self.energy
    def setEnergy(self , energy) : self.energy = energy
    ################################################################
    def getProcessCast(self) : return self.processCast
    def setProcessCast(self , processCast) : self.processCast = processCast
    ################################################################
    def getFitnessValue(self) : return self.fitnessValue
    def setFitnessValue(self , fitnessValue) : self.fitnessValue = fitnessValue
    ################################################################




