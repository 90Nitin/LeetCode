__author__ = 'nsrivas3'

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        row = 0
        col = 0
        numrow = grid.__len__()
        numcol = grid[0].__len__()
        # 1. Creating a complete grid as according to the specifications of the question
        for row in range(0,numrow):
            grid[row].append('0')
            grid[row].insert(0,'0')
        grid.append(['0']*(numcol+2))
        grid.insert(0,['0']*(numcol+2))
        numrow = grid.__len__()
        numcol = grid[0].__len__()
        countIsl = 0
        for row in range(1,numrow-1):
            for col in range(1,numcol-1):
        # 2. The last logic to detect an Island was wrong


        return(countIsl)



Sol1 = Solution()
print(Sol1.numIslands([['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]))