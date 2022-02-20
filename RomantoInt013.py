class RomantoInt(object):

    def romanToInt(self, s):
        doubles = {'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9, 'IV':4}
        singles = {'M':1000, 'D': 500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

        total = 0
        skipper = False

        for c in range(len(s)):
            if skipper == True:
                skipper = False

            elif s[c:c+2] in doubles:
                total += doubles.get(s[c:c+2])
                skipper = True

            elif s[c] in singles:
                total += singles.get(s[c])
                

        return total

r = RomantoInt()
print(r.romanToInt('MMXIX'))

