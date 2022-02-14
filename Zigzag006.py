class Zigzag006(object):
    def to_zig(self, s, numrows):
        if numrows == 1:
            return s

        space = numrows*2-2
        new_s = ""
        for i, char in enumerate(s):
            




