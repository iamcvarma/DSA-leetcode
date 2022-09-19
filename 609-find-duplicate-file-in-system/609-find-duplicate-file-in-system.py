class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for path in paths:
            arr =  path.split(' ')
            root = arr[0]
            for file in arr[1:]:
                name,content = file.split('(')
                d[content[:-1]].append(root+'/'+name)
        
        return filter(lambda x:len(x)>1,d.values())