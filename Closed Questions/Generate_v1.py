__author__ = 'nsrivas3'

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows==0: return([[]])
        if numRows==1: return([[1]])
        if numRows==2: return([[1],[1,1]])
        pascalsTr = []
        pascalsTr.append([1])
        pascalsTr.append([1,1])
        iter = 2
        while(iter<numRows):
            temp = []
            for i in range(0,pascalsTr[iter-1].__len__()):
                if i==0: temp.append(1)
                else: temp.append(pascalsTr[iter-1][i]+pascalsTr[iter-1][i-1])
            temp.append(1)
            pascalsTr.append(temp)
            iter = iter + 1

        return(pascalsTr)

Sol1 = Solution()
print(Sol1.generate(1))