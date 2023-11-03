from abc import ABC, abstractmethod
import random
import time
from tqdm import tqdm
import parmap
import multiprocessing

# 토끼와 거북이 동시 출발, 주어진 랜덤한 스피드로 직진, time.sleep으로 대기시간도 지정
'''
- 동물 추상 클래스 - 변수(속도, 대기 시간, 남은 거리) 추상 메소드(달리기)
- 동물 클래스를 상속받는 토끼와 거북이 클래스가 있을 때 토끼의 속도는 2~5, 대기시간은 1~6 거북이의 속도는 1~7, 대기 시간은 3~4 각 램덤한 초이다.
- 달리기의 로직은 go와 wait가 있으며 각각 속도와 대기시간이 반영된다. go 일 경우 남은거리가 속도만큼 줄어들고, wait일 경우 대기시간만큼 대기한다. 
- 인스턴스 멤버변수의 남은거리가 0 이하일 경우 경주에서 승리한다.
- 남은거리가 100이고, start 메소드를 이용하여 토끼와 거북이 경주를 진행하고 승자가 누구인지 프린트하는 코드를 제작해보세요
- 멀티프로세싱은 parmap을 사용하여 프로세스바를 표현하십시오
'''
class Animal(ABC):
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.wait = 0
        self.remain: int = 10
        self.total: int = self.remain

    @abstractmethod
    def race(self):
        pass

class Rabbit(Animal):
    def __init__(self):
        super().__init__("토끼")

    def race(self):
        self.speed = random.randint(2, 5)
        self.wait = random.randint(1, 6)
        
        # >= 0이면 0일 때도 경주 계속 되고 있어, > 0으로 수정 
        while self.remain > 0:
            action = random.choice(['go', 'wait'])
            print(action, "토끼 남은거리: ", self.remain)
            if action == 'go':
                self.remain -= self.speed
                print(self.remain)
            else:
                time.sleep(self.wait)
            
            # 토끼 진행 바: 이동해야 할 총 거리, 진행 바에 표시할 이름
            with tqdm(total=self.total, desc=self.name) as pbar:
                pbar.update(self.total - self.remain)    # 수동으로 진행상황 표시(총 거리에서 줄어든 리메인 만큼 표시 되게) 

        
class Turtle(Animal):
    def __init__(self):
        super().__init__("거북이")

    def race(self):
        self.speed = random.randint(1, 7)
        self.wait =  random.randint(3, 4)
    
        while self.remain > 0:
            action = random.choice(['go', 'wait'])
            print(action, "거북이 남은거리: ", self.remain)
            if action == 'go':
                self.remain -= self.speed
            else:   
                time.sleep(self.wait)
            
            # 거북이 진행바: 이동해야 할 총 거리, 진행 바에 표시할 이름
            with tqdm(total=self.total, desc=self.name) as pbar:
                pbar.update(self.total-self.remain)    # 수동으로 진행상황 표시(총 거리에서 줄어든 리메인 만큼 표시 되게) 
      

# 경주 시작
def start_race(animal, final_list):
    animal.race()

    
    # 경주 결과를 final_list에 저장(먼저 끝난 순서대로 append)   
    final_list.append(animal.name)
    print(final_list)
    
    # return animal.name, final_list

def main():
    rabbit = Rabbit()
    turtle = Turtle()

    # multiprocessing.Manager()를 사용하여 공유할 리스트를 만듦
    manager = multiprocessing.Manager()
    final_list = manager.list()

    # 병렬실행(target=함수, args=인자)
    processes = [
        multiprocessing.Process(target=start_race, args=(rabbit, final_list)),
        multiprocessing.Process(target=start_race, args=(turtle, final_list))
    ]
    
    # 프로세스 시작
    for p in processes:
        p.start()

    # 프로세스 종료 될 때까지 대기 
    for p in processes:
        p.join()

    # 승자 출력(경주가 먼저 끝난 동물이 리스트 0번 인덱스로 저장)
    print(final_list)
    print( f'{final_list[0]} 승리!!')
  
if __name__ == "__main__":
    main()
 
