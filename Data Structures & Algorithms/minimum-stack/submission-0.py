import heapq
class MinStack:

    def __init__(self):
        self.__stack = []
        self.__min = []
        heapq.heapify(self.__min)

    def push(self, val: int) -> None:
        self.__stack.append(val)
        if self.__min:
            if self.__min[0] > val:
                heapq.heappush(self.__min, val)
            else:
                heapq.heappush(self.__min, self.__min[0])
        else:
            heapq.heappush(self.__min, val)
        
    def pop(self) -> None:
        self.__stack.pop()
        heapq.heappop(self.__min)

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__min[0]

        
