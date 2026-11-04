class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        l,r = 0, len(people)-1
        res = 0
        while r>=l:
            cur = people[r]+people[l]
            if cur<=limit:
                l+=1
            r-=1 
            res+=1
        return res