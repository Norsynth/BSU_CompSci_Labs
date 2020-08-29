class LogicGate:
    
    def __init__(self,n):
        self.label = n
        self.output = None
        
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    
class BinaryGate(LogicGate):
    
    def __init__(self,n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"--> "))
        else:
            return self.pinA.getFrom().getOutput()
            
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"--> "))
        else:
            return self.pinB.getFrom().getOutput()
        
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("fnBinaryGateError: NO EMPTY PINS")

class UnaryGate(LogicGate):
    
    def __init__(self,n):
        super().__init__(n)
        self.pin = None
        
    def getPin(self):#Should be used to find other sources
        if self.pin == None:
            return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()
    

    def setNextPin(self, source):
      if self.pin == None:
        self.pin = source
      else:
        raise RuntimeError("fnUnaryGateError: NO EMPTY PIN!")

    

class AndGate(BinaryGate):
    
    def __init__(self,n):
        super().__init__(n)
        
    def performGateLogic(self):
        
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
        


class OrGate(BinaryGate):
    
    def __init__(self,n):
        super().__init__(n)
        
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0
        
        
class NotGate(UnaryGate):
    
    def __init__(self,n):
        super().__init__(n)

    def performGateLogic(self):
        pin = self.getPin()
        if pin == 0:
            return 1
        else:
            return 0

class Connector:
    '''memory gates used to connect values'''
    def __init__(self,fgate,tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)
        
    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

class NandGate(AndGate):
    '''Returns true if there is anything except two trues'''
    def performGateLogic(self):
        if super().performGateLogic()==1:
            return 0
        else:
            return 1
        
class NorGate(OrGate):
    '''Returns true if there are two falses'''
    def performGateLogic(self):
        if super().performGateLogic()==1:
            return 0
        else:
            return 1

class XorGate(BinaryGate):
    '''Returns true if there is only one true'''
    def __init__(self,n):
        super().__init__(n)
        
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a == 1 and b == 0) or (a == 0 and b == 1):
            return 1
        else:
            return 0




def main():
    '''Example circuit'''
    g1 = AndGate('And1')
    g2 = AndGate('And2')
    g3 = OrGate('Or3')
    g4 = NotGate('Not4')
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    print(g4.getOutput())

def main2():
    '''Redesigned Circuit'''
    g1 = OrGate('Or1')
    g2 = AndGate('And2')
    g3 = NotGate('Not3')
    g4 = NotGate('Not4')
    g5 = OrGate('Or5')
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g4)
    c3 = Connector(g3,g5)
    c4 = Connector(g4,g5)
    print(g5.getOutput())

def main3():
    '''Circuit using new logic gates'''
    g1 = NorGate('Nor1')
    g2 = NandGate('Nand2')
    g3 = XorGate('Xor3')
    g4 = NotGate('Not4')
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)

    print(g4.getOutput())
    

if __name__ == "__main__":
    main()
    main2()
    main3()

        
