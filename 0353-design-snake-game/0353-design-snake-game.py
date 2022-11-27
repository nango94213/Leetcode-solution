import collections
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.d = {'L': (0, -1), 'U': (-1, 0), 'R': (0, 1), 'D': (1, 0)}
        self.m = height
        self.n = width
        self.food = food
        self.index = 0
        self.snake = collections.deque([(0, 0)])
        self.body = set([(0, 0)])
        

    def move(self, direction: str) -> int:
        new = (self.snake[-1][0]+self.d[direction][0], self.snake[-1][1]+self.d[direction][1])
        
        if new[0] < 0 or new[0] >= self.m or new[1] < 0 or new[1] >= self.n:
            return -1
        if new in self.body and new != self.snake[0]:
            return -1
        
        f = self.food[self.index] if self.index < len(self.food) else None
        
        if f and (f[0], f[1]) == new:
            self.index += 1
        else:
            tmp = self.snake.popleft()
            self.body.remove(tmp)
        
        self.snake.append(new)
        self.body.add(new)
        return len(self.body)-1
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)