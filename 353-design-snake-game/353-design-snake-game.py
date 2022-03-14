import collections
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        
        self.snake = collections.deque([(0, 0)])
        self.snake_set = set([(0, 0)])
        self.food_index = 0
        self.food = food
        self.width = width
        self.height = height
        self.d = {'L': (0, -1), 'U': (-1, 0), 'R': (0, 1), 'D': (1, 0)}

    def move(self, direction: str) -> int:
        
        newHead = (self.snake[-1][0] + self.d[direction][0], self.snake[-1][1]+self.d[direction][1])

        if newHead[0] < 0 or newHead[0] >= self.height or newHead[1] < 0 or newHead[1] >=self.width:
            return -1
        
        if  newHead != self.snake[0] and newHead in self.snake_set:
            return -1
        
        current_food = self.food[self.food_index] if self.food_index < len(self.food) else None
        
        if current_food and (current_food[0] == newHead[0]) and (current_food[1] == newHead[1]):
            self.food_index += 1
        else:
            tail = self.snake.popleft()
            self.snake_set.remove(tail)
        
        self.snake.append(newHead)
        self.snake_set.add(newHead)
        
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)