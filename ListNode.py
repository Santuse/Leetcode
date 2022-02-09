import random

class ListNode(object):
    def __init__(self, x):
        self.val = x
        #print(x)
        self.next = None
        self.prev = None
        self.isHead = False
    


    def populate(self, x):
        if(x > 1):
            ln = ListNode(random.randint(0, 10))
            self.next = ln
            ln.populate(x-1)
        
    def get(self):
        return self.val

    def setHead(self):
        self.isHead = True

    def get_total(self):
        remainder = self.get()
        print("nutz", remainder)
        ln = self.next
        while(ln):
            
            remainder = remainder*10
            remainder += ln.get()
            ln = ln.next

        print(remainder)
        return(remainder)
        

            






class Solution(object):
    def addTwoNumbers(self, l1, l2):

        prev = result = ListNode(None)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2: 
                carry += l2.val
                l2 = l2.next
            
            prev.next = ListNode(carry %10)
            prev = prev.next 
            carry //= 10

        return result


ln = ListNode(1)
ln.setHead()
ln.populate(4)
ln2 = ListNode(1)
ln.setHead()
ln2.populate(4)
ln.get_total()
ln2.get_total()

s = Solution()
k = s.addTwoNumbers(ln, ln2)
print ("hey", k.get_total())