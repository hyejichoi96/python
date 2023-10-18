from abc import ABCMeta, abstractmethod

class Human(metaclass=ABCMeta):
    def __init__(self, age: int, hungry: int) -> None: 
        self.age: int = age
        self._hungry: int = hungry    # 외부에서 부를거 _ 붙여줌(protected 변수)
        
    @abstractmethod
    def eat(self):
        pass    # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦

    @abstractmethod
    def sleep(self):
        pass

    @property
    def hungry(self):
        return self._hungry

    # @hungry.setter
    # def hungry(self, hungry):
    #     self._hungry = hungry

# 파생 클래스에서 매서드 구현
class Man(Human):

    def eat(self):
        self._hungry -= 7

    def sleep(self):
        self._hungry += 12

# 객체 생성 
choi = Man(25, 50)
for _ in range(5):
    choi.eat()
    choi.eat()
    choi.sleep()

print("5일 후 배고픔 수치: ", choi.hungry)