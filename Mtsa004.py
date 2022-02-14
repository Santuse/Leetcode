"""New solution not shown online
this tries to splice together the two lists via binary search
then, it checks edge cases
the method will recursively add or subtract 1, 1/2, 1/4 to harmonicsum
This does not check boundary conditions like it should, or average two values. 
"""
class Mtsa004(object):
    def find_mtsa(self, A: list[int], B: list[int]):

        if len(B) > len(A): #A always bigger
            A, B = B, A

        total = len(A) + len(B)

        
        halfa = int(len(A)*.5)
        halfb = int((len(B) + len(A)%2)*.5)
        #if both a and b are truncated, give b an extra
        lenb = len(B)
        k = 1
        harmonicsum = 0
        
        while(2*k*lenb > 1):
            offset = halfb*harmonicsum
            if(A[int(halfa+offset)] > B[halfb-offset]):
                harmonicsum-=k
            if(A[halfa+offset] > B[halfb-offset]):
                harmonicsum+=k  
            else:
                break                
        k = k/2

        return ([A[halfa+offset-1], A[halfa+offset], B[halfb-offset-1 ], B[halfb-offset],])

        #if total % 2 == 0:
            #return (A[halfa+offset]+B[halfb-offset])/2

        #elif 

mtsa = Mtsa004()
print(mtsa.find_mtsa([0,1,2,3,4,5,6,7,8,9,10,11,12], [1,4,5,6,7,8]))


            

            


    











    
mtsa = Mtsa004()
mtsa.find_mtsa([1,2,3,4], [4,9])


