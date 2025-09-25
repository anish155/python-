class tictactoe:
    def __init__(self):
        self.board=[" "]*9
        self.current_player="O"

    def display_board(self):
        print("\n")
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("\n")

    def make_move(self,position):
        if self.board[position]==" ":
            self.board[position]=self.current_player
            return True
        else:
            print("Position already taken.")
            return False
    
    def switch_player(self):
        self.current_player="X" if self.current_player=="O" else "O"
    
    def check_winner(self):
        win_conditions = [
            (0,1,2), (3,4,5), (6,7,8), 
            (0,3,6), (1,4,7), (2,5,8), 
            (0,4,8), (2,4,6)           
        ]

        for a,b,c in win_conditions:
            if self.board[a]==self.board[b]==self.board[c]!=" ":
                return True
        return False
    
    def is_draw(self):
        return " " not in self.board
    
    def play(self):
        while True:
            self.display_board()
            pos=int(input(f"Player {self.current_player}, Enter the position you want to move (0 to 9):"))

            if self.make_move(pos):
                self.display_board()

                if self.check_winner():
                    print(f"🎉 Player {self.current_player} wins!")
                    break
                elif self.is_draw():
                    print("🤝 It's a draw!")
                    break
                self.switch_player()
            
ttt=tictactoe()
ttt.play()

