class TicTacToe(object):

    def start(self):
        xpos = [0,0,0,0,0,0,0,0,0]
        opos = [0,0,0,0,0,0,0,0,0]
        xwin = False
        owin = False
        xturn = True



        def print_board(xpos, opos):
            def p(s):
                print(s, end = "")


            for k in range(3):

                for i in range(3):
                    if(k<2):
                        p("_")
                    if(k == 2):
                        p(" ")
                    if xpos[i+k*3] == True:
                        p("X")
                    elif opos[i+k*3] == True:
                        p("O")
                    elif(k<2):
                        p("_")
                    else:
                        p(" ")
                    if(k < 2):
                        p("_")
                    if(k==2):
                        p(" ")
                    if i < 2:
                        p("|")
                p("\n")

        while(xwin == owin == False):
            val = [int(x) for x in input("xpos, ypos")]
            val1 = val[0]+3*val[1]

            if xturn == True:
                xpos[val1] = 1
            
            else:
                opos[val1] = 1
            
            xturn*=-1
            
            print_board(xpos, opos)




        
        



t = TicTacToe()

t.start()