import collections
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        group_mapping = {}
        for (u, v) in dislikes:                             # Create graph
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        visited = set()
        for i in range(1, N + 1):                           # Iterate each node
            if i in visited: continue                       # No need to revisit, since it's a non-directed graph
            stack = [(i, 0)]                                # Use stack for BFS
            while stack:                                    # You can also use a deque instead of 2 while loop on stack
                tmp_stack = []
                while stack:                                # exhaust current stack before go to next layer (BFS)
                    cur_node, group = stack.pop()
                    if cur_node in group_mapping and group != group_mapping[cur_node]:  # check if it's conflict
                        return False
                    if cur_node in visited: continue        # If visited and no conflict, continue to avoid dead loop
                    group_mapping[cur_node] = group         # Assign group for current node
                    visited.add(cur_node)
                    for child in self.graph[cur_node]:      # Assign contrary group for dislikes of current node
                        tmp_stack.append((child, not group))
                stack = tmp_stack            
        return True  
                
                