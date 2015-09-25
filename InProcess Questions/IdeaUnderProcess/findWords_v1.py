__author__ = 'nsrivas3'

def findWords(board, words):
    board = [
    ['t','i','m','a'],
    ['i','i','d','e'],
    ['n','h','k','l'],
    ['o','p','q','r'],
    ['a','b','c','d']
    ]
    words = ["nitim"]
    counter = 0
    def MatLoc(board,words,counter):
        wordList = list(words[counter])
        wordLen = wordList.__len__()
        nRow = board.__len__()
        nCol = board[0].__len__()

        return()

