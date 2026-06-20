class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            cur = digits[i]+carry
            carry = 0

            if cur>10:
                cur = cur%10
                carry = cur//10
            
            if cur==10:
                cur = 0
                carry = 1
            
            digits[i] = cur
            if carry == 0:
                return digits

            
        if carry!=0:
            digits = [carry] + digits
        return digits
