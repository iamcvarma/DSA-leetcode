class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node,target,seen,ans,res):
            if node in seen:return res
            if node==target:
                res.append(ans[:])
                return res
            seen.add(node)
            for nei in graph[node]:
                ans.append(nei)
                dfs(nei,target,seen,ans,res)
                ans.pop()
            seen.remove(node)
            return res
        
        return dfs(0,len(graph)-1,set(),[0],[])