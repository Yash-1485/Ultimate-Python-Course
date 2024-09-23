from random import randint as rnd
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def bookTickets(self,fro,to):
        self.fro=fro
        self.to=to
        print("Train - {0} is booked for {1} to {2}.".format(self.trainNo,fro,to))
    def getStatus(self):
        print(f"Train - {self.trainNo} is ready to arrive.")
    def getFareInfo(self):
        print("Train - {0} is booked for {1} to {2} is Rs.{3}.".format(self.trainNo,self.fro,self.to,rnd(1,3000)))
t=Train("135243")
t.bookTickets("Kalupur","Mumbai")
t.getStatus()
t.getFareInfo()