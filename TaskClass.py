class Task:
    def __init__(self):
        self.id=None
        self.size=0
        self.memory=0
        self.deadline=0
        self.penalty=0
        self.QoS=0
        self.inputFileSize=None
        self.outPutFileSize=None
        self.responseTime=0
        self.isDone = False
    def getId(self) : return self.id
    def setId(self,id) : self.id=id
    ##########################
    def getSize(self) : return self.size  ##unite is [MI]
    def setSize(self,size) : self.size = size
    ##########################
    def getMemory(self):return self.memory
    def setMemory(self,memory):self.memory=memory
    ##########################
    def getDeadline(self):return self.deadline
    def setDeadline(self,deadline):self.deadline = deadline
    ##########################
    def getPenalty(self):return self.penalty
    def setPenalty(self,penalty):self.penalty = penalty
    ##########################
    def getQoS(self):return self.QoS
    def setQoS(self,qos):self.QoS=qos
    ##########################
    def getResponse(self):return self.response
    def setResponse(self,response):self.response = response
    #########################
    def getInputFileSize(self):return self.inputFileSize
    def setInputFileSize(self,inPutFileSize):self.inputFileSize = inPutFileSize
    #########################
    def getOutPutFileSize(self):return self.outPutFileSize
    def setOutPutFileSize(self,outPutFileSize):self.outPutFileSize = outPutFileSize
    #########################
    def getIsDone(self): return self.isDone
    def setIsDone(self,isDone):self.isDone = isDone



