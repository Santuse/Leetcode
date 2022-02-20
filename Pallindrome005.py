"""whoops, only works for odd palindromes. Moving on"""
class Pallindrome005(object):
    def find_substring(self, s):

        longest = ""
        for i, n in enumerate(s):
            k = 0
            if i+2 <= len(s)-1 and s[i+2] == s[i]:                
                print("i", i, n)
                    
                while len(s)>i+k+2 and s[i-k] == s[i+k+2]:
                    q = i-k
                    f = i+k+2
                    print("                   ", q)                    
                    longest = max(longest, s[q:f])
                    k = k+1

        
        return longest


s = "cbabbnasussusan"
pd = Pallindrome005()
print(pd.find_substring(s))




