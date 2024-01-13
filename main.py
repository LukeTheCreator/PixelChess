import pygame, sys
from pygame.locals import *
pygame.init()

#constants/global variables
FPS_LIMIT = 60
SCREEN_DIMS = (800, 800)
PIECE_DIMS = (SCREEN_DIMS[0] / 8, SCREEN_DIMS[1] / 8)
pygame.display.set_caption("Chess by Luke")
screen = pygame.display.set_mode(SCREEN_DIMS, 0, 32)
clock = pygame.time.Clock()
blackPieces = {}
whitePieces = {}
moving = False
movingName = ""
movingColor = ""
movingLoc = (0, 0)
EMPTY = 0
PAWN_W = 1
ROOK_W = 2
KNIGHT_W = 3
BISHOP_W = 4
QUEEN_W = 5
KING_W = 6
PAWN_B = 7
ROOK_B = 8
KNIGHT_B = 9
BISHOP_B = 10
QUEEN_B = 11
KING_B = 12
gameboard = [[ROOK_B, KNIGHT_B, BISHOP_B, QUEEN_B, KING_B, BISHOP_B, KNIGHT_B, ROOK_B], 
             [PAWN_B, PAWN_B, PAWN_B, PAWN_B, PAWN_B, PAWN_B, PAWN_B, PAWN_B], 
             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
             [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
             [PAWN_W, PAWN_W, PAWN_W, PAWN_W, PAWN_W, PAWN_W, PAWN_W, PAWN_W], 
             [ROOK_W, KNIGHT_W, BISHOP_W, QUEEN_W, KING_W, BISHOP_W, KNIGHT_W, ROOK_W]]

#importing all images
boardImg = pygame.image.load("imgs/greenboard.png")
validImg = pygame.image.load("imgs/valid.png")
pawnImg_w = pygame.image.load("imgs/whitepawn.png")
rookImg_w = pygame.image.load("imgs/whiterook.png")
knightImg_w = pygame.image.load("imgs/whiteknight.png")
bishopImg_w = pygame.image.load("imgs/whitebishop.png")
queenImg_w = pygame.image.load("imgs/whitequeen.png")
kingImg_w = pygame.image.load("imgs/whiteking.png")
pawnImg_b = pygame.image.load("imgs/blackpawn.png")
rookImg_b = pygame.image.load("imgs/blackrook.png")
knightImg_b = pygame.image.load("imgs/blackknight.png")
bishopImg_b = pygame.image.load("imgs/blackbishop.png")
queenImg_b = pygame.image.load("imgs/blackqueen.png")
kingImg_b = pygame.image.load("imgs/blackking.png")

#scaling them up
boardImg = pygame.transform.scale(boardImg, SCREEN_DIMS)
validImg = pygame.transform.scale(validImg, PIECE_DIMS)
pawnImg_w = pygame.transform.scale(pawnImg_w, PIECE_DIMS)
rookImg_w = pygame.transform.scale(rookImg_w, PIECE_DIMS)
knightImg_w = pygame.transform.scale(knightImg_w, PIECE_DIMS)
bishopImg_w = pygame.transform.scale(bishopImg_w, PIECE_DIMS)
queenImg_w = pygame.transform.scale(queenImg_w, PIECE_DIMS)
kingImg_w = pygame.transform.scale(kingImg_w, PIECE_DIMS)
pawnImg_b = pygame.transform.scale(pawnImg_b, PIECE_DIMS)
rookImg_b = pygame.transform.scale(rookImg_b, PIECE_DIMS)
knightImg_b = pygame.transform.scale(knightImg_b, PIECE_DIMS)
bishopImg_b = pygame.transform.scale(bishopImg_b, PIECE_DIMS)
queenImg_b = pygame.transform.scale(queenImg_b, PIECE_DIMS)
kingImg_b = pygame.transform.scale(kingImg_b, PIECE_DIMS)

#classes
class Piece:
    def __init__(self, name, color, img, position, hitbox, alive):
        self.name = name
        self.color = color
        self.img = img
        self.position = position
        self.hitbox = hitbox
        self.alive = alive

    def IsValidMove(x, y):
        print("this hard")

#functions
def createPiece(name, color, img, position):
    newRect = pygame.Rect(position, PIECE_DIMS)
    p = Piece(name, color, img, position, newRect, True)
    if(color == "b"):
        blackPieces[name] = p
    elif(color == "w"):
        whitePieces[name] = p

def initGameBoard():
    #white
    createPiece("wPawn1", "w", pawnImg_w, (0, 600))
    createPiece("wPawn2", "w", pawnImg_w, (100, 600))
    createPiece("wPawn3", "w", pawnImg_w, (200, 600))
    createPiece("wPawn4", "w", pawnImg_w, (300, 600))
    createPiece("wPawn5", "w", pawnImg_w, (400, 600))
    createPiece("wPawn6", "w", pawnImg_w, (500, 600))
    createPiece("wPawn7", "w", pawnImg_w, (600, 600))
    createPiece("wPawn8", "w", pawnImg_w, (700, 600))
    createPiece("wRook1", "w", rookImg_w, (0, 700))
    createPiece("wKnight1", "w", knightImg_w, (100, 700))
    createPiece("wBishop1", "w", bishopImg_w, (200, 700))
    createPiece("wQueen", "w", queenImg_w, (300, 700))
    createPiece("wKing", "w", kingImg_w, (400, 700))
    createPiece("wBishop2", "w", bishopImg_w, (500, 700))
    createPiece("wKnight2", "w", knightImg_w, (600, 700))
    createPiece("wRook2", "w", rookImg_w, (700, 700))
    #black
    createPiece("bPawn1", "b", pawnImg_b, (0, 100))
    createPiece("bPawn2", "b", pawnImg_b, (100, 100))
    createPiece("bPawn3", "b", pawnImg_b, (200, 100))
    createPiece("bPawn4", "b", pawnImg_b, (300, 100))
    createPiece("bPawn5", "b", pawnImg_b, (400, 100))
    createPiece("bPawn6", "b", pawnImg_b, (500, 100))
    createPiece("bPawn7", "b", pawnImg_b, (600, 100))
    createPiece("bPawn8", "b", pawnImg_b, (700, 100))
    createPiece("bRook1", "b", rookImg_b, (0, 0))
    createPiece("bKnight1", "b", knightImg_b, (100, 0))
    createPiece("bBishop1", "b", bishopImg_b, (200, 0))
    createPiece("bQueen", "b", queenImg_b, (300, 0))
    createPiece("bKing", "b", kingImg_b, (400, 0))
    createPiece("bBishop2", "b", bishopImg_b, (500, 0))
    createPiece("bKnight2", "b", knightImg_b, (600, 0))
    createPiece("bRook2", "b", rookImg_b, (700, 0))

#draws the board to the screen and every piece that is on top of it
def drawGameBoard():
    screen.blit(boardImg, (0, 0))
    for p in blackPieces:
        if blackPieces[p].alive:
            screen.blit(blackPieces[p].img, blackPieces[p].position)
    for p in whitePieces:
        if whitePieces[p].alive:
            screen.blit(whitePieces[p].img, whitePieces[p].position)

#game play
initGameBoard()
while True:
    drawGameBoard()
    mouseLoc = pygame.mouse.get_pos()
    movingLoc = (mouseLoc[0] - PIECE_DIMS[0] / 2, mouseLoc[1] - PIECE_DIMS[1] / 2)

    if moving:
        if movingColor == "b":
            blackPieces[movingName].position = movingLoc
            blackPieces[movingName].hitbox.topleft = movingLoc
        if movingColor == "w":
            whitePieces[movingName].position = movingLoc
            whitePieces[movingName].hitbox.topleft = movingLoc
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if moving:
                    moving = False
                    movingName = ""
                    movingColor = ""
                else:
                    #go through every rectangle to see if they clicked on one
                    for p in blackPieces:
                        if blackPieces[p].hitbox.collidepoint(event.pos):
                            #check what moves they can make
                            print(p)
                            moving = True
                            movingName = p
                            movingColor = "b"
                    for p in whitePieces:
                        if whitePieces[p].hitbox.collidepoint(event.pos):
                            #check what moves they can make
                            print(p)
                            moving = True
                            movingName = p
                            movingColor = "w"

    pygame.display.update()
    clock.tick(FPS_LIMIT)
