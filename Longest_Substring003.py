""" class Longest_Substring003(object):


    def lss(self, s):
        last_seen = {}
        start = 0
        longest = 0
        for i, c in enumerate(s):

            if c in last_seen and last_seen[c] >= start:
                start = last_seen[c] +1
            else:
                longest = max(longest, i-start+1)

                last_seen[c] = i
        
        print(longest-1)
        return longest-1

ls = Longest_Substring003()

ls.lss('aaaaabcdaefghiajklmnopqrsatuvbcdefghijklmnopq') """