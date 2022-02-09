class Mtsa004(object):
    def find_mtsa(self, A: list[int], B: list[int]):


        if len(B) > len(A): #A always bigger
            A, B = B, A
        saver = k = len(B)//2
        q = len(A)//2
        total = len(A) + len(B)
    

        while k > 0:
            k+=1
            q = total - saver
            if B[saver] > A[q]:
                saver-=k
                print("B>A -", saver, k)
            elif B[saver] < A[q]:
                saver+=k
                print("B<A +", saver, k)
            else:
                k = 0
            k=k//2

        if saver == 0:

