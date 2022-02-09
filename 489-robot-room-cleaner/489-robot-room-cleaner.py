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
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 0 up 1 right 2 down 3 left
        
        seen = set([(0, 0)])
        
        def dfs(x, y, d):
            
            robot.clean()
            
            
            for i in range(4):
                new_d = (d+i)%4
                new_x, new_y = x + directions[new_d][0], y + directions[new_d][1]
                
                if (new_x, new_y) not in seen and robot.move():
                    seen.add((new_x, new_y))
                    dfs(new_x, new_y, new_d)
                    
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                    
                robot.turnRight()
        
        dfs(0, 0, 0)