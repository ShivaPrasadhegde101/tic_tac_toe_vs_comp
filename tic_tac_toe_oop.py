
class Board():
    def __init__(self):
        self.board=[" "," "," "," "," "," "," "," "," "," "]

    def display(self):
        
        print()
        print("%c  | %c |%c"%(self.board[1],self.board[2],self.board[3]))
        print("___|___|___")
        print("%c  | %c |%c"%(self.board[4],self.board[5],self.board[6]))
        print("___|___|___")
        print("%c  | %c |%c"%(self.board[7],self.board[8],self.board[9]))
        print("   |   |   ")
        print()

    def inputchar(self,x,choice):
        global chance
        if(x<1 or x>9):
            print("Please enter the number in range")
        else:
            if(self.board[x]==" "):
                self.board[x]=choice
                chance=chance+1
            else:
                print("Already filled")

    def Winner(self):
        if(self.board[1]==self.board[2] and self.board[2] ==self.board[3] and self.board[2]!=' '):
            return True
        elif(self.board[4]==self.board[5] and self.board[5] ==self.board[6] and self.board[5]!=' '):
            return True
        elif(self.board[7]==self.board[8] and self.board[8] ==self.board[9] and self.board[8]!=' '):
            return True
        elif(self.board[1]==self.board[4] and self.board[4] ==self.board[7] and self.board[1]!=' '):
            return True
        elif(self.board[2]==self.board[5] and self.board[5] ==self.board[8] and self.board[2]!=' '):
            return True
        elif(self.board[3]==self.board[6] and self.board[6] ==self.board[9] and self.board[3]!=' '):
            return True
        elif(self.board[1]==self.board[5] and self.board[5] ==self.board[9] and self.board[5]!=' '):
            return True
        elif(self.board[3]==self.board[5] and self.board[5] ==self.board[7] and self.board[5]!=' '):
            return True
        else:
            return False

    def checktie(self):
        if(self.board[1]!=' ' and self.board[2]!=' ' and self.board[3]!=' ' and self.board[4]!=' ' and self.board[5]!=' ' and self.board[6]!=' ' and self.board[7]!=' ' and self.board[8]!=' ' and self.board[9]!=' '):
            return True
        else:
            return False
        
    def reset(self):
        self.board=[" "," "," "," "," "," "," "," "," "," "]

b=Board()
chance=0
print("Player1-'X',Player2-'O'")
while(True):
    if(chance%2==0):
        print("\nPlayer1's turn")
        x=int(input("Enter the number from(1-9):"))
        b.inputchar(x,"X")
        b.display()
    else:
        print("\nPlayer2's turn")
        x=int(input("Enter the number from(1-9):"))
        b.inputchar(x,"O")
        b.display()

    if(b.Winner()==True):
        if(chance%2==0):
            print("Player2 won\n")
        else:
            print("Player1 won\n")
        re=input("Do you want to continue(Y/N):").upper()
        if(re=="Y"):
            chance=0
            b.reset()
            continue
        else:
            break

    if(b.checktie()==True):
        print("It's a Tie")
        re=input("Do you want to continue(Y/N):").upper()
        if(re=="Y"):
            chance=0
            b.reset()
            continue
        else:
            break
        
