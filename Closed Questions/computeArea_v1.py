__author__ = 'nsrivas3'

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = (max(A,C)-min(A,C))*(max(B,D)-min(B,D))
        area2 = (max(E,G)-min(E,G))*(max(F,H)-min(F,H))
        if area1==0 or area2==0: return(area1+area2)
        # Checking if the rectangles completely overlap each other

        # Writing the intersecting conditions for the rectangles
        if (((min(E,G)>=min(A,C)) and (min(E,G)<max(A,C))) or ((max(E,G)>=min(A,C)) and (max(E,G)<max(A,C)))) or (((min(F,H)>=min(B,D)) and (min(F,H)<max(B,D))) or ((max(F,H)>=min(B,D)) and (max(F,H)<max(B,D)))):
               print("the rectangles intersect")
               area3 = (max(max(max(A,E),min(C,G))-min(max(A,E),min(C,G)),0))*(max(max(max(B,F),min(H,D))-min(max(B,F),min(H,D)),0))
        else: area3 = 0

        print(area3)
        return(area1+area2-area3)

Sol1 = Solution()
print(Sol1.computeArea(-2, -2, 2, 2, -3, -3, 3, -1))
# print(Sol1.computeArea(-1, -1, 1, 1, -2, -2, 2, 2))

