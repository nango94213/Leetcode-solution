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
        
        head = (self.snake[-1][0] + self.d[direction][0], self.snake[-1][1] + self.d[direction][1])
        if head[0] < 0 or head[0] >= self.m or head[1] < 0 or head[1] >= self.n:
            return -1
        
        if head != self.snake[0] and head in self.body:
            return -1
        
        current = self.food[self.index] if self.index < len(self.food) else None
        
        if current and (head[0] == current[0]) and (head[1] == current[1]):
            self.index += 1
        else:
            tail = self.snake.popleft()
            self.body.remove(tail)
        
        self.snake.append(head)
        self.body.add(head)
        print(self.snake)
        return len(self.snake) - 1
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)