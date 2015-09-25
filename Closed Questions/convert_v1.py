__author__ = 'nsrivas3'

# Learning - We cannot append to a list that doesnt even exist yet
# We have to create the list first
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1 or numRows > s.__len__():
            return(s    )
        # 1. To store the number of cycles undergone by the zig-zag pattern
        cycle = 1
        # 2. To count the number of words counter
        wordCount = 0
        zigzag = {}
        for i in range(0,numRows):
            zigzag[i] = []
        i = 0
        s = list(s)
        while(wordCount<s.__len__()):
            if cycle%2!=0:
                zigzag[i].append(s[wordCount])
                i = i + 1
            else:
                zigzag[i].append(s[wordCount])
                i = i - 1
            if i==0 or i==(numRows-1):
                cycle = cycle + 1
            wordCount = wordCount + 1
        s = ""
        for i in range(0,numRows):
            temp = ""
            temp = temp.join(zigzag[i])
            s = s + temp
            # print(temp)
        return(s)

Sol1 = Solution()
# print(Sol1.convert("PAYPALISHIRING",2))
print(Sol1.convert("AB",1))