class Solution(object):
    def allPathsSourceTarget(self, graph):
        target=len(graph)-1
        result=[]
        path=[]
        def dfs(node):
            path.append(node)
            if node==target:
                result.append(path[:])
            else:
                for nei in graph[node]:
                    dfs(nei)
            path.pop()
        dfs(0)
        return result        