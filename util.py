def is_winner(player, board):
    for i in range(2, len(board)):
        for j in range(len(board)):
            # Detect Horizontal
            if board[i][j] == player and board[i-1][j] == player and board[i-2][j] == player:
                return True
            # Detect Vertical
            if board[j][i] == player and board[j][i-1] == player and board[j][i-2] == player:
                return True
            # Detect Diagonal
            if j >= 2 and board[i][j] == player and board[i-1][j-1] == player and board[i-2][j-2] == player:
                return True
            if j < len(board)-2 and board[i][j] == player and board[i-1][j+1] == player and board[i-2][j+2] == player:
                return True

    return False


def is_tie(board):
    for i in range(len(board)):
        if None in board[i]:
            return False

    return True
