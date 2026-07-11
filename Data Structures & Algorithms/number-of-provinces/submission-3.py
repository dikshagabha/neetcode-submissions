class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [ i for i in range(n)]
        connected = []
        ranks = [1]*n
        for i in range(n):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]==1 and i!=j and (i,j) not in connected and (j,i) not in connected:
                    connected.append((i, j))
        
        
        def find(n1):
            res = n1
            while res!=par[res]:
                res = par[res]
            return res

        def union(n1, n2):
            parn1, parn2 = find(n1), find(n2)

            if parn1==parn2:
                return 0
            
            if ranks[parn1]>ranks[parn2]:
                par[parn2]=parn1
                ranks[parn1] += ranks[parn2]
            else:
                par[parn1]=parn2
                ranks[parn2] += ranks[parn1]
            return 1
        res = n
        for e1, e2 in connected:
            res -= union(e1, e2)
        return res
        # for curroot, edges in connected.items():
        #     for j in edges:
        #         roots[j] = roots[curroot]
        # print(connected, roots)


        # counts = [0]*n
        # res=0
        # for i in roots:
        #     if counts[i]==0:
        #         res+=1
        #     counts[i]+=1
        return res