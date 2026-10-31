class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if 'G' not in instructions:
            return True
        
        x, y = 0, 0
        dx, dy = 0, 1
        for i in instructions:
           if i=='G': x+=dx; y+=dy
           elif i=='L': dx,dy = -dy, dx
           else: dx, dy = dy, -dx
        
        return (dx, dy) != (0, 1) or (x==0 and y==0)
