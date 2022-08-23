class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.currentIndex = 0
        

    def visit(self, url: str) -> None:
        
        self.stack = self.stack[:self.currentIndex+1]
        self.stack.append(url)
        
        self.currentIndex = len(self.stack) - 1
        

    def back(self, steps: int) -> str:
        
        self.currentIndex = max(self.currentIndex-steps, 0)
        
        return self.stack[self.currentIndex]
        

    def forward(self, steps: int) -> str:
        
        self.currentIndex = min(self.currentIndex+steps, len(self.stack)-1)
        
        return self.stack[self.currentIndex]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)