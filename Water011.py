""" THis finds the volume of containers via lasers
it sucks """

class Water(object):

    def getArea(self, height: list[int]) -> int:
        top = min(height[0], height[-1])
        total = 0 
        
        for j in range(len(height)-2):
            total += top - height[j+1]
    
        return total

    def maxArea(self, height: list[int]) -> int:
        def getArea(height: list[int]):
            top = min(height[0], height[-1])
            total = 0 
            
            for j in range(len(height)-2):
                total += top - height[j+1]
        
            return total



        lenh = len(height)
        i = 0
        maxa = 0

        while i < lenh:     
            h = height[i]
            find = False
            for j in range(h, -1, -1):
                if find == True:
                    break
                #j is the height countdown
                k = i+1
                #k is positional of next wall
                while k < lenh:         
                    
                    if height[k] >= j:
                        area1 = getArea(height[i:k+1])
                        maxa = max(maxa, area1)
                        print(maxa)
                        i = k-1
                        find = True
                        break
                    k+=1
            i+= 1
        return maxa
                
l1 = [1,1,1,1,12,12,12,12,12,1,1,8,6,3,5,4,7,1,1,1]

w = Water()
l2 = w.maxArea(l1)
print(l2)