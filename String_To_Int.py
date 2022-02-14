class String_To_Int(object):
    def myAtoi(self, s):
        s = s.strip()
        if '-' in s:
            negative = True
        digits = ('0123456789')
        
        holder = 0
        for c in s:
            if c in digits:
                print(c)
                holder=holder*10 +  int(c)
        if negative:
            holder = holder*-1
        return holder

sti = String_To_Int()
print(sti.myAtoi('      lksfjdsjfk-kldfjskdfjlsk823723782'))