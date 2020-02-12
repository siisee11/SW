import numpy as np

def scan(board):
    bitmap = np.zeros_like(board)
    for r in range(len(board)):
        for c in range(len(board[0])):
            conv(board[r:r+2, c:c+2])
    
def conv(sub):
    print(sub)

def solution(m, n, board):
    answer = 0
    

    board = np.matrix([ list(x) for x in board ])
    scan(board)

    return answer

if __name__ == "__main__":
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"] 
    print(solution(6 ,6 , board))