import collections
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        indegree = collections.defaultdict(int)
        outgoing = collections.defaultdict(list)
        color_matrix = [[0]*26 for _ in range(len(colors))]
        stack = []
        res = 0
        
        for u, v in edges:
            indegree[v] += 1
            outgoing[u].append(v)
        
        for node in range(len(colors)):
            if indegree[node] == 0:
                stack.append(node)
        
        processed = 0
 
        while stack:
            current = stack.pop()
            processed += 1
            color_index = ord(colors[current]) - ord('a')
            color_matrix[current][color_index] += 1
            res = max(res, color_matrix[current][color_index])
            
            for next_node in outgoing[current]:
                color_matrix[next_node] = list(map(max, color_matrix[next_node], color_matrix[current]))
                indegree[next_node] -= 1
                
                if indegree[next_node] == 0:
                    stack.append(next_node)

        return -1 if processed < len(colors) else res
            
        