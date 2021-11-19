import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import editDistance as eD

chains = ''
bitmapRantai =[]
count=0

dummyImage = np.array([ 
                [0,0,0,0,0,0],
                [0,0,255,255,0,0],
                [0,255,0,0,255,0],
                [255,0,0,0,255,0],
                [0,255,0,0,255,0],
                [0,0,255,255,0,0],
                [0,0,0,0,0,0]
            ])

#Arah
# 4   3   2
# 5       1
# 6   7   8

def cariChainKode(img,korX,korY):
    global chains
    global bitmapRantai
    global count
    
    if (img[korX] [korY+1]==255):
        if(bitmapRantai[korX][korY+1]==0):
            chains=chains+'1'
            newKorX = korX
            newKorY = korY+1
            bitmapRantai [korX] [korY+1]=1
            count+=1
            # bitmapRantai [korX] [korY+1]=255
            cariChainKode(img,newKorX,newKorY)

    if (img[korX-1] [korY]==255):
        if (bitmapRantai[korX-1][korY]==0): 
            chains=chains+'3'
            newKorX = korX-1
            newKorY = korY
            bitmapRantai[korX-1][korY]=3
            count+=1
            # bitmapRantai[korX-1][korY]=255
            cariChainKode(img,newKorX,newKorY)

    if (img[korX] [korY-1]==255):
        if (bitmapRantai[korX] [korY-1] == 0):
            chains=chains+'5'
            newKorX = korX
            newKorY = korY-1
            bitmapRantai[korX] [korY-1] = 5
            count+=1
            # bitmapRantai[korX] [korY-1] = 255
            cariChainKode(img,newKorX,newKorY)

    if(img[korX+1] [korY]==255):
        if (bitmapRantai[korX+1] [korY] == 0):
            chains=chains+'7'
            newKorX = korX+1
            newKorY = korY
            bitmapRantai[korX+1] [korY] = 7
            count+=1
            # bitmapRantai[korX+1] [korY] = 255
            cariChainKode(img,newKorX,newKorY)

    if (img[korX-1] [korY+1]==255):
        if(bitmapRantai[korX-1][korY+1]==0):
            chains=chains+'2'
            newKorX = korX-1
            newKorY = korY+1
            bitmapRantai [korX-1] [korY+1] = 2
            count+=1
            # bitmapRantai [korX-1] [korY+1] = 255
            cariChainKode(img,newKorX,newKorY)    

    if (img[korX-1] [korY-1]==255):
        if(bitmapRantai[korX-1] [korY-1] == 0):    
            chains=chains+'4'
            newKorX = korX-1
            newKorY = korY-1
            bitmapRantai[korX-1] [korY-1] = 4
            count+=1
            # bitmapRantai[korX-1] [korY-1] = 255
            cariChainKode(img,newKorX,newKorY)

    if(img[korX+1] [korY-1]==255):
        if(bitmapRantai[korX+1] [korY-1]==0): 
            chains=chains+'6'
            newKorX = korX+1
            newKorY = korY-1
            bitmapRantai[korX+1] [korY-1] =6
            count+=1
            # bitmapRantai[korX+1] [korY-1] =255
            cariChainKode(img,newKorX,newKorY)

    if(img[korX+1] [korY+1]==255):
        if(bitmapRantai[korX+1] [korY+1] == 0):
            chains=chains+'8'
            newKorX = korX+1
            newKorY = korY+1
            bitmapRantai[korX+1] [korY+1]=8
            count+=1
            # bitmapRantai[korX+1] [korY+1]=255
            cariChainKode(img,newKorX,newKorY)

image1 = cv.imread('Image/P square.JPG')
image2 = cv.imread("Image/R square.JPG")

edges1 = cv.Canny(image1,100,200)
edges2 = cv.Canny(image2,100,200)

# concatCanny = cv.hconcat((edges1,edges2))
# cv.imshow("hasil deteksi canny", concatCanny)

#Huruf P
WhitePixels = np.array(np.where(edges1==255))
firstWhitePixels = WhitePixels[:,0]
startingPoint = firstWhitePixels
x = startingPoint[0]
y = startingPoint[1]
bitmapRantai = np.zeros_like(edges1)
#starting point diberi simbol 9
bitmapRantai[x][y] = 9

cariChainKode(edges1,x,y)
chainsForP = chains
imageP = bitmapRantai
print('Jumlah Kode Rantai= '+  str(count))
print('Kode Rantai Untuk Gambar P adalah= '+chainsForP)


chains=''
count=0
#Huruf R
WhitePixelsR = np.array(np.where(edges2==255))
firstWhitePixelsR = WhitePixelsR[:,0]
startingPointR = firstWhitePixelsR
xR = startingPointR[0]
yR = startingPointR[1]
bitmapRantai = np.zeros_like(edges2)
#starting point diberi simbol 9
bitmapRantai[xR][yR] = 9
cariChainKode(edges2,xR,yR)
chainsforR = chains
imageR = bitmapRantai
print('Jumlah Kode Rantai= '+  str(count))
print('Kode Rantai untuk Gambar R adalah= '+ chainsforR)

# cv.imshow("Gambar R",imageR)
# cv.imshow("Gambar P",imageP)

print("Jarak antara kedua citra")
jarak = eD.levenshteinDistance(chainsForP,chainsforR)
print(jarak)

print("Ratio antara kedua citra")
rasio = eD.levenshteinDistance(chainsForP,chainsforR,True)
print(rasio)

cv.waitKey(0)