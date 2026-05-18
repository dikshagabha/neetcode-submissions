class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for i in strs:
            key = str(sorted(i))
            print(key)
            if m.get(key)== None :
                m[key]=[]

            m[key].append(i)

        return m.values() 