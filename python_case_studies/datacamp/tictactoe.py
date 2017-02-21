# write your code here!
import numpy as np
def create_board():
    return np.zeros((3,3))
board = create_board()
# write your code here!
def place(board, player, position):
    if board[position]  == 0:
        board[position] = player
board = create_board()        
place(board, 1, (0,0))
# write your code here!
def possibilities(board):
   return np.where(board == 0)
possibilities(board)
# write your code here!
def random_place(board, player):
    place(board, player,random.choice(possibilities(board)))
random_place(board, 2)
board = create_board()
for i in range(3):
    for player in [1, 2]:
        # add here!
        random_place(board,player)
print(board)
# write your code here!
def row_win(board, player):
    for i in range(3):
        for j in range(3):
            if board[j][i] != player:
                return False
    return True            
row_win(board,1) 
# write your code here!
def col_win(board, player):
    for i in range(3):
        for j in range(3):
            if board[i][j] != player:
                return False
    return True            
col_win(board,1) 
# write your code here!
def diag_win(board, player):
    for i in range(3):
        if board[i][i] != player:
            return False
    return True            
diag_win(board,1)
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if row_win(board, player):
            winner = player
        elif col_win(board, player):
            winner = player
        elif diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# add your code here.
evaluate(board)
# write your code here!
def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1,2]:
            random_place(board, player)
            winner = evaluate(board)
    return winner        
play_game()
# write your code here!
import time
times = []
winners = []
start_time = time.time()
for i in range(1000):
    winners.append(play_game())
end_time = time.time()
tm = end_time - start_time
print(tm)
plt.hist(winners)
plt.show()
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [1,2]:
            if len(possibilities(board)) == 9:
                place(board, player, (1,1))
            else:
                board = random_place(board, player)
                winner = evaluate(board)
            # use `random_place` to play a game, and store as `board`.
            # use `evaluate(board)`, and store as `winner`.
            if winner != 0:
                break
    return winner

play_strategic_game()  
# write your code here!
import time
winners = []
start_time = time.time()
for i in range(1000):
    winners.append(play_strategic_game())
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
plt.hist(winners)
plt.show()


















        





       





       


























