#TIC TAC TOE

print("WELCOME TO Tic Tac Toe")
print("Graphic representation of choices : ")
print('')
print("   1   |   2   |   3   ")
print("-- -- -- -- -- -- -- --")
print("   4   |   5   |   6   ")
print("-- -- -- -- -- -- -- --")
print("   7   |   8   |   9   ")
print('')


def beginning():

    election = True

    # CHOOSE THE FIGURE OF FIRST PLAYER

    while election == True:
        player1 = input("Please pick a marker 'X' or 'O': ")
        if player1 == 'X' or player1 =='x':
            player1 = 'X'
            election = False
        elif player1 == 'O' or player1 =='o':
            player1 = 'O'
            election = False
        else:
            election = True

    return player1

player1 = beginning()

# ASSIGNING THE FIGURE OF THE SECOND PLAYER

if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'

def system():
    
    #GRAPHIC REPRESENTATION
    row1 = '\n \n'
    p1 = "       "
    p2= "|       "
    p3= "|       \n"
    row3 = "-- -- -- -- -- -- -- -- --\n"
    p4 = "       "
    p5= "|       "
    p6= "|       \n"
    row5 = "-- -- -- -- -- -- -- -- --\n"
    p7 = "       "
    p8= "|       "
    p9= "|       \n"
    row7 = ' \n'
    
    positions = [1,2,3,4,5,6,7,8,9]
    elec1 = []
    elec2 = []

    for i in range(1,10):
        ephemere = '0'
        
        #INPUT
        while ephemere.isdigit() == False or ephemere not in positions:
            ephemere = input("\nEnter the digit corresponding with the position you want: ")
            
            if ephemere.isdigit() == False:
                print("\nPlease, enter a digit\n")
            else:
                ephemere=int(ephemere)
                if ephemere not in range(1,10):
                    print("\nOUT OF RANGE\n")
                    ephemere=str(ephemere)
                    pass
                elif ephemere not in positions:
                    print("\nYou cannot overwrite!\n")
                    ephemere = str(ephemere)
                    pass
                else:
                    positions.remove(ephemere)
                    ephemere = str(ephemere)
                    break
        # GRAPHIC IN REAL TIME
        if i%2 == 1:
            if player1 == 'X':
                if ephemere=='1':
                    p1 = "   X   "
                elif ephemere=='2':
                    p2 = "|   X   "
                elif ephemere=='3':
                    p3 = "|   X   \n"
                elif ephemere=='4':
                    p4 = "   X   "
                elif ephemere=='5':
                    p5 = "|   X   "
                elif ephemere=='6':
                    p6= "|   X   \n"
                elif ephemere=='7':    
                    p7 = "   X   "
                elif ephemere=='8':
                    p8 = "|   X   "
                elif ephemere=='9':
                    p9 = "|   X   \n"
            else:
                if ephemere=='1':
                    p1 = "   O   "
                elif ephemere=='2':
                    p2 = "|   O   "
                elif ephemere=='3':
                    p3 = "|   O   \n"
                elif ephemere=='4':
                    p4 = "   O   "
                elif ephemere=='5':
                    p5 = "|   O   "
                elif ephemere=='6':
                    p6= "|   O   \n"
                elif ephemere=='7':    
                    p7 = "   O   "
                elif ephemere=='8':
                    p8 = "|   O   "
                elif ephemere=='9':
                    p9 = "|   O   \n"
        else:
            if player2 == 'X':
                if ephemere=='1':
                    p1 = "   X   "
                elif ephemere=='2':
                    p2 = "|   X   "
                elif ephemere=='3':
                    p3 = "| ) X   \n"
                elif ephemere=='4':
                    p4 = "   X   "
                elif ephemere=='5':
                    p5 = "|   X   "
                elif ephemere=='6':
                    p6= "|   X   \n"
                elif ephemere=='7':    
                    p7 = "   X   "
                elif ephemere=='8':
                    p8 = "|   X   "
                elif ephemere=='9':
                    p9 = "|   X   \n"
            else:
                if ephemere=='1':
                    p1 = "   O   "
                elif ephemere=='2':
                    p2 = "|   O   "
                elif ephemere=='3':
                    p3 = "|   O   \n"
                elif ephemere=='4':
                    p4 = "   O   "
                elif ephemere=='5':
                    p5 = "|   O   "
                elif ephemere=='6':
                    p6= "|   O   \n"
                elif ephemere=='7':    
                    p7 = "   O   "
                elif ephemere=='8':
                    p8 = "|   O   "
                elif ephemere=='9':
                    p9 = "|   O   \n"
        print(row1,p1,p2,p3,row3,p4,p5,p6,row5,p7,p8,p9,row7)

        if i%2==1:
            elec1.append(ephemere)
        else:
            elec2.append(ephemere)

    # EVALUATE IF THERE IS A WINNER

        if '1' in elec1:
            if '2' in elec1:
                if '3' in elec1:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
            elif '5' in elec1:
                if '9' in elec1:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
            elif '4' in elec1:
                if '7' in elec1:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
        elif '2' in elec1:
            if '5' in elec1:
                if '8' in elec1:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
        elif '3' in elec1:
            if '6' in elec1:
                if '9' in elec1:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
            elif '5' in elec1:
                if '7' in elec1:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
        elif '4' in elec1:
            if '5' in elec1:
                if '6' in elec1:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
        elif '7' in elec1:
            if'8' in elec1:
                if'9' in elec1:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
        else:
            pass

        if '1' in elec2:
           if '2' in elec2:
                if '3' in elec2:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
           elif '5' in elec2:
               if '9' in elec2:
                   print("YOU ARE THE WINNER, CONGRATULATIONS!")
                   break
           elif '4' in elec2:
                if '7' in elec2:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
        elif '2' in elec2:
            if '5' in elec2:
                if '8' in elec2:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
        elif '3' in elec2:
            if '6' in elec2:
                if '9' in elec2:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
            elif '5' in elec2:
                if '7' in elec2:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
        elif '4' in elec2:
            if '5' in elec2:
                if '6' in elec2:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
        elif '7' in elec2:
            if'8' in elec2:
                if'9' in elec2:
                    print("YOU ARE THE WINNER, CONGRATULATIONS!")
                    break
        else:
            pass

        if i == 9:
            print("The game is DRAW!")
        else:
            pass
        
system()
