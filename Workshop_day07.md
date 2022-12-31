### 1 . 클래스선언 -> 객체 생성  -> 멤버호출 

#[Step 01:  클래스 선언 ]
class Test: # object의  후손 클래스가 되어 선조의 메소드들을 참조하고 있다.    object <- Test
    def empty(self):
       self.data = []  #리스트 객체를 초기화 

    def add(self, x):
       self.data.append(x)  # x를 리스트 객체에 추가 

if __name__ == '__main__':
<<<<<<< HEAD:TIL_day07.md
#[Step 02:  클래스 객체 생성  ]
    my01 = Test()   # __init__()가 내부 호출되면서 메모리에 Test클래스가 로드되어 생성된다.  
    my02 = Test()

#[Step03 :  멤버 호출]
    my01.empty()  # data객체가 초기화 된다.  
    my02.empty()
    for  i in range(1,6):  # 1~   6-1   
        my01.add(i)   # data객체에  1~ 5까지 추가된다.  
    print(my01.data)    #출력
    print(my02.data)   #빈객체 출력  
    print(my01, my02) # 객체 주소 출력  
    my03= my01    #my01에 있는 주소를 my03에 대입   
    print(my03.data) # my01에서 참조되는 곳을  참조하기 때문에 같은 데이터를 출력하게 된다. 
    print(my01, my03) #동일한 주소가 출력된다.  


### 2. 정적 변수  static 변수   클래스.멤버변수 비교해 보자. 
    - 멤버는 클래스.멤버
    - static 메소드로 선언  -> @staticmethod선언 

#이름 , 주소 , 전화 번호를 관리하는 Address 라는 클래스를 선언해서 변수로 값을 저장해 보자
# 정적 변수  static 변수  ->  클래스.멤버변수
class Address:
    name="Dominica"  # 멤버 
    addr = "seoul"   #멤버 
    tel ="02-0000-000"  #멤버  
    def prn(self):  # 멤버 메소드
        #print(Address.name, Address.addr, Address.tel)  # 클래스.멤버변수  -> static형식 호출!
        print(self.name, self.addr, self.tel) 
if __name__ == '__main__':
    #print(Address.name, Address.addr, Address.tel)
    #Address.name ="1111111111111"
    #print(Address.name, Address.addr, Address.tel)

    a1 = Address() # Dominica 출력되어야 하나  1111111111111이 되는 이유는 static형식으로 사용
    a1.prn()
    
    a2 = Address() # Dominica 출력되어야 하나  1111111111111이 되는 이유는 static형식으로 사용
    a2.prn()

### 3. object클래스에서 상속받은  속성값을 사용해 보자.  
 
 -  class type(object)   =   __class __ 

#__class__ : 인스턴스가 자신을 생성한 클래스 객체를 참조하기 위하여 
 # 파이선에서 제공하는 키워드로 클래스영역(heap)에
# 모든 인스턴스 객체에  있는 데이터를 참조하거나 수정할 때 사용한다.
'''
사원 번호    7월 영업실적
a111          850
b111          750
c111          650
Emp 라는 클래스를 만들어서  변수를 2개 선언한 후  a1,b1,c1의 이름으로 객체를 생성한 다음 값을 전달 후 출력 해 보자.
'''

class Emp:
    empno  =0
    result =0
    
if __name__ == '__main__':
    #non-static 
    a1=Emp()
    a1.empno ='a111'
    a1.result =850
    print(a1.empno, a1.result)

    b1=Emp()
    b1.empno ='b111'   #non-static 
    b1.result = 750   #non-static 
    print(b1.empno , b1.result)

    c1=Emp()
    c1.empno='c111'   #non-static 
    c1.result= 650   #non-static 
    print(c1.empno, c1.result)
    print(Emp.empno, Emp.result) #static 형식

    print(Emp.__name__, type(a1.__class__) , b1.__class__ , c1.__class__)
    print(type(Emp), type(a1), type(b1),type(c1))


### 4. python의 접근제한자와 캡슐화 확인 

# 캡슐화 : 은닉된 멤버 변수에 오픈된 메소드로 값을 전달(setXX)  및  변경하는 구조(getXX return)
# getter & setter
class Test:
    __b=100 #객체 생성후 호출할 수 없고, Test의 멤버만 접근 가능하다.
    def __m(self): #한문자를 리턴하는 private 메소드
        return 'a'
    def k(self):
        print(self.__m(), self.__b)


if __name__ == '__main__':
    my = Test()
    my.k()
    #print(my.__b)오류 ,,!!Test.__b X

### 5. 클래스 캡슐화 확인

# 정수형 변수 a,b 를 관리하는 클래스를 만들어 보자. 단 캡슐화로 구현 해보자.
# 은닉된 멤버 변수에게  setxx으로 값 전달 및 변경하고   getxx return 메소드로 리턴하는 구조  4:00시
class Test:
    __a=0  #주소 히든 private 초기값은 생성자에서 대입
    __b=0
    #name ="abc"   def setName():~~
    def setA(self, a):
        self.__a =a  # 객체 생성후 값을 a 로 전달받아  멤버__a 에게 값전달 및 변경
    def getA(self):
       return self.__a

    def setB(self,b):
        self.__b=b
    def getB(self):
        return self.__b

if __name__ == '__main__':
    t1 = Test()
    t1.setA(100)  # 멤버가 private이기 때문에 직 접근  즉 호출 불가하다. 
    print(t1.getA())
    t1.setB(200)
    print(t1.getB())

### 6. 생성자와 소멸자 확인 

#생성자와 소멸자를 살펴보자.

# 생성자를 명시하지 않으면 자동으로 내부호출되어 생성되고 (선조인 object클래스의 __init__가 호출 )
#  명시하게 되면 명시된 생성자가 호출된다.

# 생성자는 단 한번 객체를 생성할 때 자동 호출되며 해당클래스의 모든 멤버를 동적 할당 메모리로 로드하게 된다.
# 생성자의 목적은 멤버변수 초기화에 있다.

#명시소멸자  : 소멸싯점에서 수행하는 조건구문을 기재할때, 파일처리, DB처리, 백업처리등 

# is ~ a  :  상속관계  
# has ~ a :  포함관계  -> 클래스 안에 또 다른 클래스를 멤버로 갖는 것 
class MyDel:
    def __init__(self, a=100): #명시 생성자  -> 멤버변수초기화  +   값 전달  
        self.a=a
        print("__ init__",a)

    def __del__(self): #명시소멸자   #소멸자 객체가 소멸되는 시점에서 호출 되면서 리소스 해제
        print("나 소거된다. 현재 클래스에서 호출되거나 참조한 다른클래스를 멤버로 가질때  소거한다.  ")

if __name__ == '__main__':
    a1 = MyDel(200)  #MyDel이라는 클래스의 생성자를 호출하면서 전달된 값으로 객체 생성한다.
    print(a1.a)
    MyDel.a=10000   #
    print(MyDel.a, a1.a)

###  7. 간단한  구조의 상속을  구현해 보자.
-  이름과 나이를 관리하는  Person 클래스있다.
-  Student클래스 Person을 상속을 받아 학년만 추가해서  이름, 나이, 학년을 모두 출력하는 클래스를 만들고 싶다.

class Person:
    __b = 10 #강한 private 형식은 멤버만 호출이 가능하다 후손은 호출이 불가능하다.
    def __init__(self, name, age,b): #5. 선조의 객체가 생성되면서 멤버변수에게 값전달
        self.name = name
        self.age = age
        self.__b=b
    def personInfo(self): #멤버변수 출력용 메소드  + 연결연산자는 시퀀스의 같은 객체끼리 연결이 가능하다. 
                          #str+str
        return  self.name  +": (age :" +  str(self.age) +")"

class Student(Person): #2
    def __init__(self,name, age,b, grade):#3
       # Person.__init__(self,name,age) #4 선조의 생성자
        super().__init__(name,age,b)
        self.grade = grade #6. 객체 생성 하면서 grade변수 값전달

    def GetStudent(self):
        #print("b= " ,  self.__b)
        return  self.personInfo() + ",grade :"+ str(self.grade)

if __name__ == '__main__':
    x=Student("Ruri",7,3,5) #1.Student("Ruri",7,3) 
    # 7.생성된 선조의 주소를 리턴 : person() <- Student() 두개짜리가 넘어감
    
    print(x.GetStudent())
    print(x.personInfo())

=======
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
>>>>>>> 6a797bef8fff74a2428c01efe6652fd25b21c971:Workshop_day07.md
