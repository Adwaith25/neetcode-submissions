from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d=defaultdict(list)
        boxes = defaultdict(list)
        for i in range(len(board)):
            l=[]
            for j in range(len(board[i])):
                if(board[i][j]=='.'):
                    continue
                if(board[i][j] in l):
                    return False
                
                
                if board[i][j] in d[j]:
                    return False
                d[j].append(board[i][j])
                box_key = (i // 3, j // 3)

# If this digit was already seen in this 3x3 square:
                if board[i][j] in boxes[box_key]:
                    return False

                boxes[box_key].append(board[i][j])
                l.append(board[i][j])
        return True
                
                



        