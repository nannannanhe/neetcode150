from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row
        for row in board:
            if self.isValidGroup(row) == False:
                return False
        
        # check column
        for i in range(9):
            column = [row[i] for row in board]
            if self.isValidGroup(column) == False:
                return False
            
        # check 9 group
        list_9 = []
        for i in range(9):
            group3x3 = []
            for j in range(3):
                begin_row = i // 3
                begin_column = 3 * (i % 3)
                group3x3 += board[3*begin_row+j][begin_column:begin_column+3]
            list_9.append(group3x3)
        for group in list_9:
            if self.isValidGroup(group) == False:
                return False
            
        return True



    # check if the 9 elements have multiple numbers
    def isValidGroup(self, group: List[str]) -> bool:
        counter = Counter(group)
        multiple_elements = [k for k, v in counter.items() if v >1]
        if len(multiple_elements) > 1:
            return False
        if len(multiple_elements) and multiple_elements[0] != '.':
            return False
        return True