from abc import abstractmethod, ABCMeta

class Mobile(metaclass=ABCMeta):
    __mobileName = 'NONAME'
    __batterySize = 0
    __osType = 0

    def __init__(self, mobileName, batterySize, osType):
        self.__mobileName = mobileName
        self.__batterySize = batterySize
        self.__osType = osType

    def getMobileName(self):
        return self.__mobileName
    def getBatterySize(self):
        return self.__batterySize
    def getOsType(self):
        return self.__osType
    def setBatterySize(self, batterySize):
        self.__batterySize = batterySize
    def setOsType(self, osType):
        self.__osType = osType
    @abstractmethod
    def operate(self):
        pass

class IChange(metaclass=ABCMeta):
    @abstractmethod
    def charge(self, time):
        pass

class LTab(Mobile, IChange):
    def __init__(self, mobileName, batterySize, osType):
        Mobile.__init__(self, mobileName, batterySize, osType)
    def charge(self, time):
        chargedAmount = time * 10
        Mobile.setBatterySize(self, Mobile.getBatterySize(self) + chargedAmount)
        return Mobile.getBatterySize(self)
    def operate(self, time):
        usedAmount = time * 10
        Mobile.setBatterySize(self, Mobile.getBatterySize(self) - usedAmount)
        return Mobile.getBatterySize(self)

class OTab(Mobile, IChange):
    def __init__(self, mobileName, batterySize, osType):
        Mobile.__init__(self, mobileName, batterySize, osType)
    def charge(self, time):
        chargedAmount = time * 8
        Mobile.setBatterySize(self, Mobile.getBatterySize(self) + chargedAmount)
        return Mobile.getBatterySize(self)
    def operate(self, time):
        usedAmount = time * 12
        Mobile.setBatterySize(self, Mobile.getBatterySize(self) - usedAmount)
        return Mobile.getBatterySize(self)

if __name__ == '__main__':
    a1 = LTab("LTab", 500, "AP-01")
    a2 = OTab("OTab", 1000, "AND-20")
    print("Mobile", "\t\t", "Battery", "\t\t", "osType", "\n", "-"*30)
    print(a1.getMobileName()+ "\t\t" + str(a1.getBatterySize()) + "\t\t\t" + a1.getOsType())
    print(a2.getMobileName()+ "\t\t" + str(a2.getBatterySize()) + "\t\t" + a2.getOsType())
    print("-" * 30)
    print("10분 충전")
    print("Mobile", "\t\t", "Battery", "\t\t", "osType", "\n", "-" * 30)
    a1.charge(10)
    a2.charge(10)
    print(a1.getMobileName() + "\t\t" + str(a1.getBatterySize()) + "\t\t\t" + a1.getOsType())
    print(a2.getMobileName() + "\t\t" + str(a2.getBatterySize()) + "\t\t" + a2.getOsType())
    print("-" * 30)
    print("5분 통화")
    print("Mobile", "\t\t", "Battery", "\t\t", "osType", "\n", "-" * 30)
    a1.operate(5)
    a2.operate(5)
    print(a1.getMobileName() + "\t\t" + str(a1.getBatterySize()) + "\t\t\t" + a1.getOsType())
    print(a2.getMobileName() + "\t\t" + str(a2.getBatterySize()) + "\t\t" + a2.getOsType())
    print("-" * 30)