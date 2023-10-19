from abc import ABCMeta, abstractmethod
import random
import time

# 토끼와 거북이 동시 출발, 주어진 랜덤한 스피드로 직진, time.sleep으로 대기시간도 지정
'''
- 동물 추상 클래스 - 변수(속도, 대기 시간, 남은 거리) 추상 메소드(달리기)
- 동물 클래스를 상속받는 토끼와 거북이 클래스가 있을 때 토끼의 속도는 2~5, 대기시간은 1~6 거북이의 속도는 1~7, 대기 시간은 3~4 각 램덤한 초이다.
- 달리기의 로직은 go와 wait가 있으며 각각 속도와 대기시간이 반영된다. go 일 경우 남은거리가 속도만큼 줄어들고, wait일 경우 대기시간만큼 대기한다. 
- 인스턴스 멤버변수의 남은거리가 0 이하일 경우 경주에서 승리한다.
- 남은거리가 100이고, start 메소드를 이용하여 토끼와 거북이 경주를 진행하고 승자가 누구인지 프린트하는 코드를 제작해보세요
- 멀티프로세싱은 parmap을 사용하여 프로세스바를 표현하십시오
'''

class Animal(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._speed: int = 0
        self._wait: int = 0
        self._remain: int = 100
    
    @abstractmethod
    def race(self):
        pass
        
    @property
    def speed(self):
        return self._speed
    
    @property
    def wait(self):
        return self._wait
    
    @property
    def remain(self):
        return self._remain
    
    @remain.setter
    def remain(self, remain):
        return remain - self._speed
    
class Rabbit(Animal):

    def race(self):
        action = random.choice(['go', 'stop'])
        if action == 'go': 
            self._remain -= self._speed   
        else:
            time.sleep(self._wait)

    def speed(self):
        random.randint(2, 5)
        print(random.randint(2, 5))

    def wait(self):    
        time.sleep(random.randint(1, 6))
        print(time.sleep(random.randint(1, 6)))


class Turtle(Animal):

    def speed(self):
        random.randint(1, 7)
    
    def wait(self):    
        time.sleep(random.randint(3, 4))


a = Rabbit()
a.race()
a.speed()
a.wait()
print(a.remain)
