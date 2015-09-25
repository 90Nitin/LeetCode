__author__ = 'nsrivas3'

# Simplify the code a little bit

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
        area1 = (C-A)*(D-B)
        area2 = (G-E)*(H-F)
        print("area1: "+str(area1))
        print("area2: "+str(area2))
        if area1==0 or area2==0: return(area1+area2)
        if (E<A and G<A) or (E>C and G>C) or (F<B and H<B) or (F>D and H>D):
            print("the rectangles do not intersect")
            area3 = 0
        else: area3 = (max(max(max(A,E),min(C,G))-min(max(A,E),min(C,G)),0))*(max(max(max(B,F),min(H,D))-min(max(B,F),min(H,D)),0))
        # Just check if the rectangles are not intersecting


        print(area3)
        return(area1+area2-area3)

Sol1 = Solution()
# print(Sol1.computeArea(-2, -2, 2, 2, -3, -3, 3, -1))
print(Sol1.computeArea(-1, -1, 1, 1, -2, -2, 2, 2))

