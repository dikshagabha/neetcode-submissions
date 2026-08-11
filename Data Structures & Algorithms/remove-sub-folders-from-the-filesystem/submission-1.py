class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        folder.sort()

        res = [folder[0]]

        for cur in folder[1:]:
            if not cur.startswith(res[-1]+'/'):
                res.append(cur)
        return res
        # print(d)
        # res = []
        # for i in d:
        #     cur = '/'
        #     for j in i:
        #         cur+=j+'/'
                
        #     res.append(cur[:-1])
        # return res