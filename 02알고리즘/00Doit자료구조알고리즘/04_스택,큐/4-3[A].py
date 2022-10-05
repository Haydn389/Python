from typing import Any


class FixedQueue:

    class Empty():
        pass
    class Full():
        pass

    def __init__(self, capacity:int) ->None:
        """큐 초기화"""
        self.no=0                   #현재 데이터 갯수
        self.front=0                #맨 앞 원소 커서
        self.rear=0                 #맨 뛰 원소 커서
        self.capacity=capacity      #큐의 크기
        self.que=[None]*capacity    #큐의 본체

    def __len__(self) ->int:
        """큐에있는 모든데이터 개수를 반환"""
        return self.no

    def is_empty(self) ->bool:
        """큐에있는 모든데이터 개수를 반환"""
        return self.no <=0

    def is_full(self) ->bool:
        """큐에있는 모든데이터 개수를 반환"""
        return self.no >=self.capacity
    def enqueue(self, x:Any)-> None:
        pass
    