from abc import ABC, abstractmethod
import random
import time
from tqdm import tqdm
import parmap

class Animal(ABC):
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.wait = 0
        self.remain = 10

    @abstractmethod
    def race(self):
        pass

class Rabbit(Animal):
    def __init__(self):
        super().__init__("토끼")

    def race(self):
        self.speed = random.randint(2, 5)
        self.wait = random.randint(1, 6)
        
        while self.remain >= 0:
            action = random.choice(['go', 'wait'])
            print(action)
            if action == 'go':
                self.remain -= self.speed
            else:
                time.sleep(self.wait)
            
            # 토끼 진행 바: 이동해야 할 총 거리, 진행 바에 표시할 이름
            with tqdm(total=10, desc=self.name) as pbar:
                pbar.update(10-self.remain)    # 수동으로 진행상황 표시(총 거리에서 줄어든 리메인 만큼 표시 되게) 

        
class Turtle(Animal):
    def __init__(self):
        super().__init__("거북이")

    def race(self):
        self.speed = random.randint(1, 7)
        self.wait =  random.randint(3, 4)
    
        while self.remain >= 0:
            action = random.choice(['go', 'wait'])
            print(action)
            if action == 'go':
                self.remain -= self.speed
            else:   
                time.sleep(self.wait)
            
            # 거북이 진행바: 이동해야 할 총 거리, 진행 바에 표시할 이름
            with tqdm(total=10, desc=self.name) as pbar:
                pbar.update(10-self.remain)    # 수동으로 진행상황 표시(총 거리에서 줄어든 리메인 만큼 표시 되게) 
      


# 경주 시작
def start_race(animal):
    while animal.remain > 0:
        animal.race()
    
    return animal.name

def main():
    rabbit = Rabbit()
    turtle = Turtle()
        
    # 병렬 실행을 위한 프로세스(parmap.map(실행함수, input data, 진행상황 바, core갯수))         
    result_list = parmap.map(start_race, [rabbit, turtle], pm_pbar=True, pm_processes=2)
    # print(f'{result_list[0]}의 승리임')
    print(result_list)

    # 승자 출력2
    if rabbit.remain <= 0 | turtle.remain <= 0:
        if rabbit.remain < turtle.remain:
            print("토끼 승!!")
        else:
            print("거북이 승!!")
  
if __name__ == "__main__":
    main()
 
