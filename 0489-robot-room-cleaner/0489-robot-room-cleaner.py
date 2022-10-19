# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = set([(0, 0)])
        def dfs(x, y, d):
            robot.clean()
            
            for i in range(4):
                index = (i+d) % 4
                
                newX = x + directions[index][0]
                newY = y + directions[index][1]
                
                if (newX, newY) not in seen and robot.move():
                    seen.add((newX, newY))
                    dfs(newX, newY, index)
                    
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                
                robot.turnRight()
            
        dfs(0, 0, 0)
                
        