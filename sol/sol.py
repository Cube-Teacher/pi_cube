import pupil_apriltags as apriltag 
import cv2
import numpy as np
import sys
import time
from PIL import Image, ImageDraw, ImageFont
from pupil_apriltags import Detector

terminal=sys.stdout

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
# cv2.namedWindow('camera', cv2.WINDOW_AUTOSIZE)
detector1 = apriltag.Detector(families='tag36h11')

former=[]
former1=0

file=open("./init.txt","w")
sys.stdout=file
print("")
sys.stdout=terminal
    
start_flag=0

key=0

operation=[]

initial_color_done=[0,0,0,0,0,0]#white blue green orange red white #確認各顏色為中心之面是否完成掃描
initial_color=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]#white blue green orange red white
               ,[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]#各顏色為中心之面的初始顏色

now_color=[0,0,0,0,0,0,0,0,0]#讀取進來之九宮格
top_color=[0,0,0,0,0,0,0,0,0]

color_detect_x=[0,0,0,0,0,0,0,0,0]#tag之x座標
color_detect_y=[0,0,0,0,0,0,0,0,0]#tag之y座標
color_detect_id=[0,0,0,0,0,0,0,0,0]#tag之id

def print_operations(x):
    
    global former1
    global former
    
    length=len(x)
    i=0
    count=0
    toImage = Image.new('RGBA',(800,500))
    fromImge = Image.open('white.png')
    loc = (0,0)
    toImage.paste(fromImge, loc)
    fromImge = Image.open('word.png')
    loc = (0,0)
    toImage.paste(fromImge, loc)
    
    arr=[]
    open('picture.txt', 'w').close()
    
    index=0
  
    while (1):
        
        
        if(i==length or check_str(str(x[i]))==1):
            break
        if(i==0):
            index=x[i]
        count=count+1
        arr.append(str(x[i])+'.png')
        print_op(x[i])
        
        i=i+1
        
    if(len(arr)>=former1):
        former=[]
        former1=0
    pic=[]
    
    for i in former:
        pic.append(i)
    for i in arr:
        pic.append(i)
        
    
    
    if(len(pic)<=8):
        if(len(pic)==1):
            offset=350
        elif(len(pic)==2):
            offset=300
        elif(len(pic)==3):
            offset=250
        elif(len(pic)==4):
            offset=200
        elif(len(pic)==5):
            offset=150
        elif(len(pic)==6):
            offset=100
        elif(len(pic)==7):
            offset=50
        elif(len(pic)==8):
            offset=0
        for i in range(len(pic)):
            fromImge = Image.open(pic[i])
            loc = (offset+i*100,300)
            toImage.paste(fromImge, loc)
    elif(len(pic)>8):
        if(len(pic)-8==1):
            offset=350
        elif(len(pic)-8==2):
            offset=300
        elif(len(pic)-8==3):
            offset=250
        elif(len(pic)-8==4):
            offset=200
        elif(len(pic)-8==5):
            offset=150
        elif(len(pic)-8==6):
            offset=100
        elif(len(pic)-8==7):
            offset=50
        elif(len(pic)-8==8):
            offset=0
        for i in range(len(pic)):
            fromImge = Image.open(pic[i])
            if(i<=7):
                loc = (i*100,300)
            else:
                loc = (offset+(i-8)*100,400)
            toImage.paste(fromImge, loc)
  
        
    toImage.save('image.png')

    image1 = cv2.imread('image.png') 
    cv2.imshow('flow', image1)
    cv2.waitKey(1)
    if(len(arr)>0):
        former.append(str(index)+'-1.png')
    former1=len(arr)
    
        
    return
    
def check_str(x):
    if(x=='1' or x=='2' or x=='3' or x=='4' or x=='5'):
        return 0
    elif(x=='6' or x=='7' or x=='8' or x=='9' or x=='10'):
        return 0
    elif(x=='11' or x=='12' or x=='13' or x=='14' or x=='15'):
        return 0
    elif(x=='16' or x=='17' or x=='18' or x=='19' or x=='20'):
        return 0
    
    return 1
        
def write_file(x):
    file=open("./command.txt","w")
    sys.stdout=file
    print(x)
    sys.stdout=terminal
    
def write__color_file(x):
    file=open("./init.txt","a")
    sys.stdout=file
    
    if(x>=1 and x<=9):
        print("WHITE")
    if(x>=10 and x<=18):
        print("BLUE")
    if(x>=19 and x<=27):
        print("GREEN")
    if(x>=28 and x<=36):
        print("ORANGE")
    if(x>=37 and x<=45):
        print("RED")
    if(x>=46 and x<=54):
        print("YELLOW")
        
    sys.stdout=terminal
    
def swap_four_element(w,x,y,z):
    return x,y,z,w


def check_valid():
    if(top_color[0]==now_color[0] and top_color[1]==now_color[1] and top_color[3]==now_color[3]#右排下轉
   and top_color[4]==now_color[4] and top_color[6]==now_color[6] and top_color[7]==now_color[7]
   and now_color[2]==initial_color[2][6] and now_color[5]==initial_color[2][3] and now_color[8]==initial_color[2][0]):
        initial_color[0][2],initial_color[2][6],initial_color[5][2],initial_color[1][2]=swap_four_element(initial_color[0][2],initial_color[2][6],initial_color[5][2],initial_color[1][2])
        initial_color[0][5],initial_color[2][3],initial_color[5][5],initial_color[1][5]=swap_four_element(initial_color[0][5],initial_color[2][3],initial_color[5][5],initial_color[1][5])
        initial_color[0][8],initial_color[2][0],initial_color[5][8],initial_color[1][8]=swap_four_element(initial_color[0][8],initial_color[2][0],initial_color[5][8],initial_color[1][8])
        initial_color[3][0],initial_color[3][2],initial_color[3][8],initial_color[3][6]=swap_four_element(initial_color[3][0],initial_color[3][2],initial_color[3][8],initial_color[3][6])
        initial_color[3][1],initial_color[3][5],initial_color[3][7],initial_color[3][3]=swap_four_element(initial_color[3][1],initial_color[3][5],initial_color[3][7],initial_color[3][3])
        write_file("left3_Counterclockwise")
        return 1
    
    elif(top_color[0]==now_color[0] and top_color[1]==now_color[1] and top_color[3]==now_color[3]#右排上轉
   and top_color[4]==now_color[4] and top_color[6]==now_color[6] and top_color[7]==now_color[7]
   and now_color[2]==initial_color[1][2] and now_color[5]==initial_color[1][5] and now_color[8]==initial_color[1][8]):
        initial_color[0][2],initial_color[1][2],initial_color[5][2],initial_color[2][6]=swap_four_element(initial_color[0][2],initial_color[1][2],initial_color[5][2],initial_color[2][6])
        initial_color[0][5],initial_color[1][5],initial_color[5][5],initial_color[2][3]=swap_four_element(initial_color[0][5],initial_color[1][5],initial_color[5][5],initial_color[2][3])
        initial_color[0][8],initial_color[1][8],initial_color[5][8],initial_color[2][0]=swap_four_element(initial_color[0][8],initial_color[1][8],initial_color[5][8],initial_color[2][0])
        initial_color[3][0],initial_color[3][6],initial_color[3][8],initial_color[3][2]=swap_four_element(initial_color[3][0],initial_color[3][6],initial_color[3][8],initial_color[3][2])
        initial_color[3][1],initial_color[3][3],initial_color[3][7],initial_color[3][5]=swap_four_element(initial_color[3][1],initial_color[3][3],initial_color[3][7],initial_color[3][5])
        write_file("left3_clockwise")
        return 2
    
    elif(top_color[1]==now_color[1] and top_color[2]==now_color[2] and top_color[4]==now_color[4]#左排下轉
   and top_color[5]==now_color[5] and top_color[7]==now_color[7] and top_color[8]==now_color[8]
   and now_color[0]==initial_color[2][8] and now_color[3]==initial_color[2][5] and now_color[6]==initial_color[2][2]):
        initial_color[0][0],initial_color[2][8],initial_color[5][0],initial_color[1][0]=swap_four_element(initial_color[0][0],initial_color[2][8],initial_color[5][0],initial_color[1][0])
        initial_color[0][3],initial_color[2][5],initial_color[5][3],initial_color[1][3]=swap_four_element(initial_color[0][3],initial_color[2][5],initial_color[5][3],initial_color[1][3])
        initial_color[0][6],initial_color[2][2],initial_color[5][6],initial_color[1][6]=swap_four_element(initial_color[0][6],initial_color[2][2],initial_color[5][6],initial_color[1][6])
        initial_color[4][0],initial_color[4][6],initial_color[4][8],initial_color[4][2]=swap_four_element(initial_color[4][0],initial_color[4][6],initial_color[4][8],initial_color[4][2])
        initial_color[4][1],initial_color[4][3],initial_color[4][7],initial_color[4][5]=swap_four_element(initial_color[4][1],initial_color[4][3],initial_color[4][7],initial_color[4][5])
        write_file("left1_Counterclockwise")
        return 3
    
    elif(top_color[1]==now_color[1] and top_color[2]==now_color[2] and top_color[4]==now_color[4]#左排上轉
   and top_color[5]==now_color[5] and top_color[7]==now_color[7] and top_color[8]==now_color[8]
   and now_color[0]==initial_color[1][0] and now_color[3]==initial_color[1][3] and now_color[6]==initial_color[1][6]):
        initial_color[0][0],initial_color[1][0],initial_color[5][0],initial_color[2][8]=swap_four_element(initial_color[0][0],initial_color[1][0],initial_color[5][0],initial_color[2][8])
        initial_color[0][3],initial_color[1][3],initial_color[5][3],initial_color[2][5]=swap_four_element(initial_color[0][3],initial_color[1][3],initial_color[5][3],initial_color[2][5])
        initial_color[0][6],initial_color[1][6],initial_color[5][6],initial_color[2][2]=swap_four_element(initial_color[0][6],initial_color[1][6],initial_color[5][6],initial_color[2][2])
        initial_color[4][0],initial_color[4][2],initial_color[4][8],initial_color[4][6]=swap_four_element(initial_color[4][0],initial_color[4][2],initial_color[4][8],initial_color[4][6])
        initial_color[4][1],initial_color[4][5],initial_color[4][7],initial_color[4][3]=swap_four_element(initial_color[4][1],initial_color[4][5],initial_color[4][7],initial_color[4][3])
        write_file("left1_clockwise")
        return 4
    
    elif(top_color[3]==now_color[3] and top_color[4]==now_color[4] and top_color[5]==now_color[5]#上排右轉
   and top_color[6]==now_color[6] and top_color[7]==now_color[7] and top_color[8]==now_color[8]
   and now_color[0]==initial_color[4][6] and now_color[1]==initial_color[4][3] and now_color[2]==initial_color[4][0]):
        initial_color[0][0],initial_color[4][6],initial_color[5][8],initial_color[3][2]=swap_four_element(initial_color[0][0],initial_color[4][6],initial_color[5][8],initial_color[3][2])
        initial_color[0][1],initial_color[4][3],initial_color[5][7],initial_color[3][5]=swap_four_element(initial_color[0][1],initial_color[4][3],initial_color[5][7],initial_color[3][5])
        initial_color[0][2],initial_color[4][0],initial_color[5][6],initial_color[3][8]=swap_four_element(initial_color[0][2],initial_color[4][0],initial_color[5][6],initial_color[3][8])
        initial_color[2][0],initial_color[2][2],initial_color[2][8],initial_color[2][6]=swap_four_element(initial_color[2][0],initial_color[2][2],initial_color[2][8],initial_color[2][6])
        initial_color[2][1],initial_color[2][5],initial_color[2][7],initial_color[2][3]=swap_four_element(initial_color[2][1],initial_color[2][5],initial_color[2][7],initial_color[2][3])
        write_file("front3_clockwise")
        return 5
    
    elif(top_color[3]==now_color[3] and top_color[4]==now_color[4] and top_color[5]==now_color[5]#上排左轉
   and top_color[6]==now_color[6] and top_color[7]==now_color[7] and top_color[8]==now_color[8]
   and now_color[0]==initial_color[3][2] and now_color[1]==initial_color[3][5] and now_color[2]==initial_color[3][8]):
        initial_color[0][0],initial_color[3][2],initial_color[5][8],initial_color[4][6]=swap_four_element(initial_color[0][0],initial_color[3][2],initial_color[5][8],initial_color[4][6])
        initial_color[0][1],initial_color[3][5],initial_color[5][7],initial_color[4][3]=swap_four_element(initial_color[0][1],initial_color[3][5],initial_color[5][7],initial_color[4][3])
        initial_color[0][2],initial_color[3][8],initial_color[5][6],initial_color[4][0]=swap_four_element(initial_color[0][2],initial_color[3][8],initial_color[5][6],initial_color[4][0])
        initial_color[2][0],initial_color[2][6],initial_color[2][8],initial_color[2][2]=swap_four_element(initial_color[2][0],initial_color[2][6],initial_color[2][8],initial_color[2][2])
        initial_color[2][1],initial_color[2][3],initial_color[2][7],initial_color[2][5]=swap_four_element(initial_color[2][1],initial_color[2][3],initial_color[2][7],initial_color[2][5])
        write_file("front3_Counterclockwise")
        return 6
    
    elif(top_color[0]==now_color[0] and top_color[1]==now_color[1] and top_color[2]==now_color[2]#下排右轉
   and top_color[3]==now_color[3] and top_color[4]==now_color[4] and top_color[5]==now_color[5]
   and now_color[6]==initial_color[4][8] and now_color[7]==initial_color[4][5] and now_color[8]==initial_color[4][2]):
        initial_color[0][6],initial_color[4][8],initial_color[5][2],initial_color[3][0]=swap_four_element(initial_color[0][6],initial_color[4][8],initial_color[5][2],initial_color[3][0])
        initial_color[0][7],initial_color[4][5],initial_color[5][1],initial_color[3][3]=swap_four_element(initial_color[0][7],initial_color[4][5],initial_color[5][1],initial_color[3][3])
        initial_color[0][8],initial_color[4][2],initial_color[5][0],initial_color[3][6]=swap_four_element(initial_color[0][8],initial_color[4][2],initial_color[5][0],initial_color[3][6])
        initial_color[1][0],initial_color[1][6],initial_color[1][8],initial_color[1][2]=swap_four_element(initial_color[1][0],initial_color[1][6],initial_color[1][8],initial_color[1][2])
        initial_color[1][1],initial_color[1][3],initial_color[1][7],initial_color[1][5]=swap_four_element(initial_color[1][1],initial_color[1][3],initial_color[1][7],initial_color[1][5])
        write_file("front1_clockwise")
        return 7
    
    elif(top_color[0]==now_color[0] and top_color[1]==now_color[1] and top_color[2]==now_color[2]#下排左轉
   and top_color[3]==now_color[3] and top_color[4]==now_color[4] and top_color[5]==now_color[5]
   and now_color[6]==initial_color[3][0] and now_color[7]==initial_color[3][3] and now_color[8]==initial_color[3][6]):
        initial_color[0][6],initial_color[3][0],initial_color[5][2],initial_color[4][8]=swap_four_element(initial_color[0][6],initial_color[3][0],initial_color[5][2],initial_color[4][8])
        initial_color[0][7],initial_color[3][3],initial_color[5][1],initial_color[4][5]=swap_four_element(initial_color[0][7],initial_color[3][3],initial_color[5][1],initial_color[4][5])
        initial_color[0][8],initial_color[3][6],initial_color[5][0],initial_color[4][2]=swap_four_element(initial_color[0][8],initial_color[3][6],initial_color[5][0],initial_color[4][2])
        initial_color[1][0],initial_color[1][2],initial_color[1][8],initial_color[1][6]=swap_four_element(initial_color[1][0],initial_color[1][2],initial_color[1][8],initial_color[1][6])
        initial_color[1][1],initial_color[1][5],initial_color[1][7],initial_color[1][3]=swap_four_element(initial_color[1][1],initial_color[1][5],initial_color[1][7],initial_color[1][3])
        write_file("front1_Counterclockwise")
        return 8
    
    elif(top_color[0]==now_color[0] and top_color[2]==now_color[2] and top_color[3]==now_color[3]#中排下轉
   and top_color[5]==now_color[5] and top_color[6]==now_color[6] and top_color[8]==now_color[8]
   and now_color[1]==initial_color[2][7] and now_color[4]==initial_color[2][4] and now_color[7]==initial_color[2][1]):
        initial_color[0][1],initial_color[2][7],initial_color[5][1],initial_color[1][1]=swap_four_element(initial_color[0][1],initial_color[2][7],initial_color[5][1],initial_color[1][1])
        initial_color[0][4],initial_color[2][4],initial_color[5][4],initial_color[1][4]=swap_four_element(initial_color[0][4],initial_color[2][4],initial_color[5][4],initial_color[1][4])
        initial_color[0][7],initial_color[2][1],initial_color[5][7],initial_color[1][7]=swap_four_element(initial_color[0][7],initial_color[2][1],initial_color[5][7],initial_color[1][7])
        write_file("left2_Counterclockwise")
        return 9
    
    elif(top_color[0]==now_color[0] and top_color[2]==now_color[2] and top_color[3]==now_color[3]#中排上轉
   and top_color[5]==now_color[5] and top_color[6]==now_color[6] and top_color[8]==now_color[8]
   and now_color[1]==initial_color[1][1] and now_color[4]==initial_color[1][4] and now_color[7]==initial_color[1][7]):
        initial_color[0][1],initial_color[1][1],initial_color[5][1],initial_color[2][7]=swap_four_element(initial_color[0][1],initial_color[1][1],initial_color[5][1],initial_color[2][7])
        initial_color[0][4],initial_color[1][4],initial_color[5][4],initial_color[2][4]=swap_four_element(initial_color[0][4],initial_color[1][4],initial_color[5][4],initial_color[2][4])
        initial_color[0][7],initial_color[1][7],initial_color[5][7],initial_color[2][1]=swap_four_element(initial_color[0][7],initial_color[1][7],initial_color[5][7],initial_color[2][1])
        write_file("left2_clockwise")
        return 10
    
    elif(top_color[0]==now_color[0] and top_color[1]==now_color[1] and top_color[2]==now_color[2]#橫排右轉
   and top_color[6]==now_color[6] and top_color[7]==now_color[7] and top_color[8]==now_color[8]
   and now_color[3]==initial_color[4][7] and now_color[4]==initial_color[4][4] and now_color[5]==initial_color[4][1]):
        initial_color[0][3],initial_color[4][7],initial_color[5][5],initial_color[3][1]=swap_four_element(initial_color[0][3],initial_color[4][7],initial_color[5][5],initial_color[3][1])
        initial_color[0][4],initial_color[4][4],initial_color[5][4],initial_color[3][4]=swap_four_element(initial_color[0][4],initial_color[4][4],initial_color[5][4],initial_color[3][4])
        initial_color[0][5],initial_color[4][1],initial_color[5][3],initial_color[3][7]=swap_four_element(initial_color[0][5],initial_color[4][1],initial_color[5][3],initial_color[3][7])
        write_file("front2_clockwise")
        return 11
    
    elif(top_color[0]==now_color[0] and top_color[1]==now_color[1] and top_color[2]==now_color[2]#橫排左轉
   and top_color[6]==now_color[6] and top_color[7]==now_color[7] and top_color[8]==now_color[8]
   and now_color[3]==initial_color[3][1] and now_color[4]==initial_color[3][4] and now_color[5]==initial_color[3][7]):
        initial_color[0][3],initial_color[3][1],initial_color[5][5],initial_color[4][7]=swap_four_element(initial_color[0][3],initial_color[3][1],initial_color[5][5],initial_color[4][7])
        initial_color[0][4],initial_color[3][4],initial_color[5][4],initial_color[4][4]=swap_four_element(initial_color[0][4],initial_color[3][4],initial_color[5][4],initial_color[4][4])
        initial_color[0][5],initial_color[3][7],initial_color[5][3],initial_color[4][1]=swap_four_element(initial_color[0][5],initial_color[3][7],initial_color[5][3],initial_color[4][1])
        write_file("front2_Counterclockwise")
        return 12
    
    elif(top_color[0]==now_color[2] and top_color[1]==now_color[5] and top_color[2]==now_color[8]#右轉
   and top_color[3]==now_color[1] and top_color[4]==now_color[4] and top_color[5]==now_color[7]
   and top_color[6]==now_color[0] and top_color[7]==now_color[3] and top_color[8]==now_color[6] and key==0):
        initial_color[0][0],initial_color[0][6],initial_color[0][8],initial_color[0][2]=swap_four_element(initial_color[0][0],initial_color[0][6],initial_color[0][8],initial_color[0][2])
        initial_color[0][1],initial_color[0][3],initial_color[0][7],initial_color[0][5]=swap_four_element(initial_color[0][1],initial_color[0][3],initial_color[0][7],initial_color[0][5])
        initial_color[1][0],initial_color[3][0],initial_color[2][0],initial_color[4][0]=swap_four_element(initial_color[1][0],initial_color[3][0],initial_color[2][0],initial_color[4][0])
        initial_color[1][1],initial_color[3][1],initial_color[2][1],initial_color[4][1]=swap_four_element(initial_color[1][1],initial_color[3][1],initial_color[2][1],initial_color[4][1])
        initial_color[1][2],initial_color[3][2],initial_color[2][2],initial_color[4][2]=swap_four_element(initial_color[1][2],initial_color[3][2],initial_color[2][2],initial_color[4][2])
        write_file("up1_Counterclockwise")
        return 13
    
    elif(top_color[0]==now_color[6] and top_color[1]==now_color[3] and top_color[2]==now_color[0]#左轉
   and top_color[3]==now_color[7] and top_color[4]==now_color[4] and top_color[5]==now_color[1]
   and top_color[6]==now_color[8] and top_color[7]==now_color[5] and top_color[8]==now_color[2] and key==0):
        initial_color[0][0],initial_color[0][2],initial_color[0][8],initial_color[0][6]=swap_four_element(initial_color[0][0],initial_color[0][2],initial_color[0][8],initial_color[0][6])
        initial_color[0][1],initial_color[0][5],initial_color[0][7],initial_color[0][3]=swap_four_element(initial_color[0][1],initial_color[0][5],initial_color[0][7],initial_color[0][3])
        initial_color[1][0],initial_color[4][0],initial_color[2][0],initial_color[3][0]=swap_four_element(initial_color[1][0],initial_color[4][0],initial_color[2][0],initial_color[3][0])
        initial_color[1][1],initial_color[4][1],initial_color[2][1],initial_color[3][1]=swap_four_element(initial_color[1][1],initial_color[4][1],initial_color[2][1],initial_color[3][1])
        initial_color[1][2],initial_color[4][2],initial_color[2][2],initial_color[3][2]=swap_four_element(initial_color[1][2],initial_color[4][2],initial_color[2][2],initial_color[3][2])
        write_file("up1_clockwise")
        return 14
    
    elif(now_color[0]==initial_color[4][6] and now_color[1]==initial_color[4][3] and now_color[2]==initial_color[4][0]#右翻
   and now_color[3]==initial_color[4][7] and now_color[4]==initial_color[4][4] and now_color[5]==initial_color[4][1]
   and now_color[6]==initial_color[4][8] and now_color[7]==initial_color[4][5] and now_color[8]==initial_color[4][2]):
        initial_color[0][0],initial_color[4][6],initial_color[5][8],initial_color[3][2]=swap_four_element(initial_color[0][0],initial_color[4][6],initial_color[5][8],initial_color[3][2])
        initial_color[0][1],initial_color[4][3],initial_color[5][7],initial_color[3][5]=swap_four_element(initial_color[0][1],initial_color[4][3],initial_color[5][7],initial_color[3][5])
        initial_color[0][2],initial_color[4][0],initial_color[5][6],initial_color[3][8]=swap_four_element(initial_color[0][2],initial_color[4][0],initial_color[5][6],initial_color[3][8])
        initial_color[2][0],initial_color[2][2],initial_color[2][8],initial_color[2][6]=swap_four_element(initial_color[2][0],initial_color[2][2],initial_color[2][8],initial_color[2][6])
        initial_color[2][1],initial_color[2][5],initial_color[2][7],initial_color[2][3]=swap_four_element(initial_color[2][1],initial_color[2][5],initial_color[2][7],initial_color[2][3])
        initial_color[0][6],initial_color[4][8],initial_color[5][2],initial_color[3][0]=swap_four_element(initial_color[0][6],initial_color[4][8],initial_color[5][2],initial_color[3][0])
        initial_color[0][7],initial_color[4][5],initial_color[5][1],initial_color[3][3]=swap_four_element(initial_color[0][7],initial_color[4][5],initial_color[5][1],initial_color[3][3])
        initial_color[0][8],initial_color[4][2],initial_color[5][0],initial_color[3][6]=swap_four_element(initial_color[0][8],initial_color[4][2],initial_color[5][0],initial_color[3][6])
        initial_color[1][0],initial_color[1][6],initial_color[1][8],initial_color[1][2]=swap_four_element(initial_color[1][0],initial_color[1][6],initial_color[1][8],initial_color[1][2])
        initial_color[1][1],initial_color[1][3],initial_color[1][7],initial_color[1][5]=swap_four_element(initial_color[1][1],initial_color[1][3],initial_color[1][7],initial_color[1][5])
        initial_color[0][3],initial_color[4][7],initial_color[5][5],initial_color[3][1]=swap_four_element(initial_color[0][3],initial_color[4][7],initial_color[5][5],initial_color[3][1])
        initial_color[0][4],initial_color[4][4],initial_color[5][4],initial_color[3][4]=swap_four_element(initial_color[0][4],initial_color[4][4],initial_color[5][4],initial_color[3][4])
        initial_color[0][5],initial_color[4][1],initial_color[5][3],initial_color[3][7]=swap_four_element(initial_color[0][5],initial_color[4][1],initial_color[5][3],initial_color[3][7])
        write_file("up_right")
        return 15
    
    elif(now_color[0]==initial_color[3][2] and now_color[1]==initial_color[3][5] and now_color[2]==initial_color[3][8]#左翻
   and now_color[3]==initial_color[3][1] and now_color[4]==initial_color[3][4] and now_color[5]==initial_color[3][7]
   and now_color[6]==initial_color[3][0] and now_color[7]==initial_color[3][3] and now_color[8]==initial_color[3][6]):
        initial_color[0][0],initial_color[3][2],initial_color[5][8],initial_color[4][6]=swap_four_element(initial_color[0][0],initial_color[3][2],initial_color[5][8],initial_color[4][6])
        initial_color[0][1],initial_color[3][5],initial_color[5][7],initial_color[4][3]=swap_four_element(initial_color[0][1],initial_color[3][5],initial_color[5][7],initial_color[4][3])
        initial_color[0][2],initial_color[3][8],initial_color[5][6],initial_color[4][0]=swap_four_element(initial_color[0][2],initial_color[3][8],initial_color[5][6],initial_color[4][0])
        initial_color[2][0],initial_color[2][6],initial_color[2][8],initial_color[2][2]=swap_four_element(initial_color[2][0],initial_color[2][6],initial_color[2][8],initial_color[2][2])
        initial_color[2][1],initial_color[2][3],initial_color[2][7],initial_color[2][5]=swap_four_element(initial_color[2][1],initial_color[2][3],initial_color[2][7],initial_color[2][5])
        initial_color[0][3],initial_color[3][1],initial_color[5][5],initial_color[4][7]=swap_four_element(initial_color[0][3],initial_color[3][1],initial_color[5][5],initial_color[4][7])
        initial_color[0][4],initial_color[3][4],initial_color[5][4],initial_color[4][4]=swap_four_element(initial_color[0][4],initial_color[3][4],initial_color[5][4],initial_color[4][4])
        initial_color[0][5],initial_color[3][7],initial_color[5][3],initial_color[4][1]=swap_four_element(initial_color[0][5],initial_color[3][7],initial_color[5][3],initial_color[4][1])
        initial_color[0][6],initial_color[3][0],initial_color[5][2],initial_color[4][8]=swap_four_element(initial_color[0][6],initial_color[3][0],initial_color[5][2],initial_color[4][8])
        initial_color[0][7],initial_color[3][3],initial_color[5][1],initial_color[4][5]=swap_four_element(initial_color[0][7],initial_color[3][3],initial_color[5][1],initial_color[4][5])
        initial_color[0][8],initial_color[3][6],initial_color[5][0],initial_color[4][2]=swap_four_element(initial_color[0][8],initial_color[3][6],initial_color[5][0],initial_color[4][2])
        initial_color[1][0],initial_color[1][2],initial_color[1][8],initial_color[1][6]=swap_four_element(initial_color[1][0],initial_color[1][2],initial_color[1][8],initial_color[1][6])
        initial_color[1][1],initial_color[1][5],initial_color[1][7],initial_color[1][3]=swap_four_element(initial_color[1][1],initial_color[1][5],initial_color[1][7],initial_color[1][3])
        write_file("up_left")
        return 16
    
    elif(now_color[0]==initial_color[2][8] and now_color[1]==initial_color[2][7] and now_color[2]==initial_color[2][6]#下翻
   and now_color[3]==initial_color[2][5] and now_color[4]==initial_color[2][4] and now_color[5]==initial_color[2][3]
   and now_color[6]==initial_color[2][2] and now_color[7]==initial_color[2][1] and now_color[8]==initial_color[2][0]):
        initial_color[0][2],initial_color[2][6],initial_color[5][2],initial_color[1][2]=swap_four_element(initial_color[0][2],initial_color[2][6],initial_color[5][2],initial_color[1][2])
        initial_color[0][5],initial_color[2][3],initial_color[5][5],initial_color[1][5]=swap_four_element(initial_color[0][5],initial_color[2][3],initial_color[5][5],initial_color[1][5])
        initial_color[0][8],initial_color[2][0],initial_color[5][8],initial_color[1][8]=swap_four_element(initial_color[0][8],initial_color[2][0],initial_color[5][8],initial_color[1][8])
        initial_color[3][0],initial_color[3][2],initial_color[3][8],initial_color[3][6]=swap_four_element(initial_color[3][0],initial_color[3][2],initial_color[3][8],initial_color[3][6])
        initial_color[3][1],initial_color[3][5],initial_color[3][7],initial_color[3][3]=swap_four_element(initial_color[3][1],initial_color[3][5],initial_color[3][7],initial_color[3][3])
        initial_color[0][0],initial_color[2][8],initial_color[5][0],initial_color[1][0]=swap_four_element(initial_color[0][0],initial_color[2][8],initial_color[5][0],initial_color[1][0])
        initial_color[0][3],initial_color[2][5],initial_color[5][3],initial_color[1][3]=swap_four_element(initial_color[0][3],initial_color[2][5],initial_color[5][3],initial_color[1][3])
        initial_color[0][6],initial_color[2][2],initial_color[5][6],initial_color[1][6]=swap_four_element(initial_color[0][6],initial_color[2][2],initial_color[5][6],initial_color[1][6])
        initial_color[4][0],initial_color[4][6],initial_color[4][8],initial_color[4][2]=swap_four_element(initial_color[4][0],initial_color[4][6],initial_color[4][8],initial_color[4][2])
        initial_color[4][1],initial_color[4][3],initial_color[4][7],initial_color[4][5]=swap_four_element(initial_color[4][1],initial_color[4][3],initial_color[4][7],initial_color[4][5])
        initial_color[0][1],initial_color[2][7],initial_color[5][1],initial_color[1][1]=swap_four_element(initial_color[0][1],initial_color[2][7],initial_color[5][1],initial_color[1][1])
        initial_color[0][4],initial_color[2][4],initial_color[5][4],initial_color[1][4]=swap_four_element(initial_color[0][4],initial_color[2][4],initial_color[5][4],initial_color[1][4])
        initial_color[0][7],initial_color[2][1],initial_color[5][7],initial_color[1][7]=swap_four_element(initial_color[0][7],initial_color[2][1],initial_color[5][7],initial_color[1][7])
        write_file("up_front")
        return 17
    
    elif(now_color[0]==initial_color[1][0] and now_color[1]==initial_color[1][1] and now_color[2]==initial_color[1][2]#上翻
   and now_color[3]==initial_color[1][3] and now_color[4]==initial_color[1][4] and now_color[5]==initial_color[1][5]
   and now_color[6]==initial_color[1][6] and now_color[7]==initial_color[1][7] and now_color[8]==initial_color[1][8]):
        initial_color[0][2],initial_color[1][2],initial_color[5][2],initial_color[2][6]=swap_four_element(initial_color[0][2],initial_color[1][2],initial_color[5][2],initial_color[2][6])
        initial_color[0][5],initial_color[1][5],initial_color[5][5],initial_color[2][3]=swap_four_element(initial_color[0][5],initial_color[1][5],initial_color[5][5],initial_color[2][3])
        initial_color[0][8],initial_color[1][8],initial_color[5][8],initial_color[2][0]=swap_four_element(initial_color[0][8],initial_color[1][8],initial_color[5][8],initial_color[2][0])
        initial_color[3][0],initial_color[3][6],initial_color[3][8],initial_color[3][2]=swap_four_element(initial_color[3][0],initial_color[3][6],initial_color[3][8],initial_color[3][2])
        initial_color[3][1],initial_color[3][3],initial_color[3][7],initial_color[3][5]=swap_four_element(initial_color[3][1],initial_color[3][3],initial_color[3][7],initial_color[3][5])
        initial_color[0][0],initial_color[1][0],initial_color[5][0],initial_color[2][8]=swap_four_element(initial_color[0][0],initial_color[1][0],initial_color[5][0],initial_color[2][8])
        initial_color[0][3],initial_color[1][3],initial_color[5][3],initial_color[2][5]=swap_four_element(initial_color[0][3],initial_color[1][3],initial_color[5][3],initial_color[2][5])
        initial_color[0][6],initial_color[1][6],initial_color[5][6],initial_color[2][2]=swap_four_element(initial_color[0][6],initial_color[1][6],initial_color[5][6],initial_color[2][2])
        initial_color[4][0],initial_color[4][2],initial_color[4][8],initial_color[4][6]=swap_four_element(initial_color[4][0],initial_color[4][2],initial_color[4][8],initial_color[4][6])
        initial_color[4][1],initial_color[4][5],initial_color[4][7],initial_color[4][3]=swap_four_element(initial_color[4][1],initial_color[4][5],initial_color[4][7],initial_color[4][3])
        initial_color[0][1],initial_color[1][1],initial_color[5][1],initial_color[2][7]=swap_four_element(initial_color[0][1],initial_color[1][1],initial_color[5][1],initial_color[2][7])
        initial_color[0][4],initial_color[1][4],initial_color[5][4],initial_color[2][4]=swap_four_element(initial_color[0][4],initial_color[1][4],initial_color[5][4],initial_color[2][4])
        initial_color[0][7],initial_color[1][7],initial_color[5][7],initial_color[2][1]=swap_four_element(initial_color[0][7],initial_color[1][7],initial_color[5][7],initial_color[2][1])
        write_file("up_back")
        return 18
    
    elif(top_color[0]==now_color[2] and top_color[1]==now_color[5] and top_color[2]==now_color[8]#右轉翻
   and top_color[3]==now_color[1] and top_color[4]==now_color[4] and top_color[5]==now_color[7]
   and top_color[6]==now_color[0] and top_color[7]==now_color[3] and top_color[8]==now_color[6] and key==1):
        initial_color[0][0],initial_color[0][6],initial_color[0][8],initial_color[0][2]=swap_four_element(initial_color[0][0],initial_color[0][6],initial_color[0][8],initial_color[0][2])
        initial_color[0][1],initial_color[0][3],initial_color[0][7],initial_color[0][5]=swap_four_element(initial_color[0][1],initial_color[0][3],initial_color[0][7],initial_color[0][5])
        initial_color[1][0],initial_color[3][0],initial_color[2][0],initial_color[4][0]=swap_four_element(initial_color[1][0],initial_color[3][0],initial_color[2][0],initial_color[4][0])
        initial_color[1][1],initial_color[3][1],initial_color[2][1],initial_color[4][1]=swap_four_element(initial_color[1][1],initial_color[3][1],initial_color[2][1],initial_color[4][1])
        initial_color[1][2],initial_color[3][2],initial_color[2][2],initial_color[4][2]=swap_four_element(initial_color[1][2],initial_color[3][2],initial_color[2][2],initial_color[4][2])
        initial_color[1][3],initial_color[3][3],initial_color[2][3],initial_color[4][3]=swap_four_element(initial_color[1][3],initial_color[3][3],initial_color[2][3],initial_color[4][3])
        initial_color[1][4],initial_color[3][4],initial_color[2][4],initial_color[4][4]=swap_four_element(initial_color[1][4],initial_color[3][4],initial_color[2][4],initial_color[4][4])
        initial_color[1][5],initial_color[3][5],initial_color[2][5],initial_color[4][5]=swap_four_element(initial_color[1][5],initial_color[3][5],initial_color[2][5],initial_color[4][5])
        initial_color[1][6],initial_color[3][6],initial_color[2][6],initial_color[4][6]=swap_four_element(initial_color[1][6],initial_color[3][6],initial_color[2][6],initial_color[4][6])
        initial_color[1][7],initial_color[3][7],initial_color[2][7],initial_color[4][7]=swap_four_element(initial_color[1][7],initial_color[3][7],initial_color[2][7],initial_color[4][7])
        initial_color[1][8],initial_color[3][8],initial_color[2][8],initial_color[4][8]=swap_four_element(initial_color[1][8],initial_color[3][8],initial_color[2][8],initial_color[4][8])
        initial_color[5][0],initial_color[5][2],initial_color[5][8],initial_color[5][6]=swap_four_element(initial_color[5][0],initial_color[5][2],initial_color[5][8],initial_color[5][6])
        initial_color[5][1],initial_color[5][5],initial_color[5][7],initial_color[5][3]=swap_four_element(initial_color[5][1],initial_color[5][5],initial_color[5][7],initial_color[5][3])
        write_file("up_fix_right")
        return 19
    
    elif(top_color[0]==now_color[6] and top_color[1]==now_color[3] and top_color[2]==now_color[0]#左轉翻
   and top_color[3]==now_color[7] and top_color[4]==now_color[4] and top_color[5]==now_color[1]
   and top_color[6]==now_color[8] and top_color[7]==now_color[5] and top_color[8]==now_color[2] and key==1):
        initial_color[0][0],initial_color[0][2],initial_color[0][8],initial_color[0][6]=swap_four_element(initial_color[0][0],initial_color[0][2],initial_color[0][8],initial_color[0][6])
        initial_color[0][1],initial_color[0][5],initial_color[0][7],initial_color[0][3]=swap_four_element(initial_color[0][1],initial_color[0][5],initial_color[0][7],initial_color[0][3])
        initial_color[1][0],initial_color[4][0],initial_color[2][0],initial_color[3][0]=swap_four_element(initial_color[1][0],initial_color[4][0],initial_color[2][0],initial_color[3][0])
        initial_color[1][1],initial_color[4][1],initial_color[2][1],initial_color[3][1]=swap_four_element(initial_color[1][1],initial_color[4][1],initial_color[2][1],initial_color[3][1])
        initial_color[1][2],initial_color[4][2],initial_color[2][2],initial_color[3][2]=swap_four_element(initial_color[1][2],initial_color[4][2],initial_color[2][2],initial_color[3][2])
        initial_color[1][3],initial_color[4][3],initial_color[2][3],initial_color[3][3]=swap_four_element(initial_color[1][3],initial_color[4][3],initial_color[2][3],initial_color[3][3])
        initial_color[1][4],initial_color[4][4],initial_color[2][4],initial_color[3][4]=swap_four_element(initial_color[1][4],initial_color[4][4],initial_color[2][4],initial_color[3][4])
        initial_color[1][5],initial_color[4][5],initial_color[2][5],initial_color[3][5]=swap_four_element(initial_color[1][5],initial_color[4][5],initial_color[2][5],initial_color[3][5])
        initial_color[1][6],initial_color[4][6],initial_color[2][6],initial_color[3][6]=swap_four_element(initial_color[1][6],initial_color[4][6],initial_color[2][6],initial_color[3][6])
        initial_color[1][7],initial_color[4][7],initial_color[2][7],initial_color[3][7]=swap_four_element(initial_color[1][7],initial_color[4][7],initial_color[2][7],initial_color[3][7])
        initial_color[1][8],initial_color[4][8],initial_color[2][8],initial_color[3][8]=swap_four_element(initial_color[1][8],initial_color[4][8],initial_color[2][8],initial_color[3][8])
        initial_color[5][0],initial_color[5][6],initial_color[5][8],initial_color[5][2]=swap_four_element(initial_color[5][0],initial_color[5][6],initial_color[5][8],initial_color[5][2])
        initial_color[5][1],initial_color[5][3],initial_color[5][7],initial_color[5][5]=swap_four_element(initial_color[5][1],initial_color[5][3],initial_color[5][7],initial_color[5][5])
        write_file("up_fix_left")
        return 20
    
    
    return 0

def check_edge(x,y):#確認兩個tag是否為同一邊塊
    if((x==2 and y==20)or(x==20 and y==2)):#白綠
        return 1
    elif((x==4 and y==38)or(x==38 and y==4)):#白紅
        return 1
    elif((x==6 and y==29)or(x==29 and y==6)):#白橘
        return 1
    elif((x==8 and y==11)or(x==11 and y==8)):#白藍
        return 1
    elif((x==13 and y==42)or(x==42 and y==13)):#藍紅
        return 1
    elif((x==15 and y==31)or(x==31 and y==15)):#藍橘
        return 1
    elif((x==24 and y==40)or(x==40 and y==24)):#綠紅
        return 1
    elif((x==22 and y==33)or(x==33 and y==22)):#綠橘
        return 1
    elif((x==47 and y==17)or(x==17 and y==47)):#黃藍
        return 1
    elif((x==49 and y==44)or(x==44 and y==49)):#黃紅
        return 1
    elif((x==51 and y==35)or(x==35 and y==51)):#黃橘
        return 1
    elif((x==53 and y==26)or(x==26 and y==53)):#黃綠
        return 1
    else :#都不是
        return 0
    
def print_color(x):#把tag id換成顏色
    if(x>=1 and x<=9):
        return'白'
    elif(x>=10 and x<=18):
        return'藍'
    elif(x>=19 and x<=27):
        return'綠'
    elif(x>=28 and x<=36):
        return'橘'
    elif(x>=37 and x<=45):
        return'紅'
    elif(x>=46 and x<=54):
        return'黃'
        
def read_image():
    ret, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    results1 = detector1.detect(gray)
    
    count=0
    
    for tag in results1:
        count=count+1
    
    if(count==9):
        count=0
        for tag in results1:
        
            cv2.circle(image, tuple(tag.corners[0].astype(int)), 4,(255,255,255), 2)
            cv2.circle(image, tuple(tag.corners[1].astype(int)), 4,(255,255,255), 2)
            cv2.circle(image, tuple(tag.corners[2].astype(int)), 4,(255,255,255), 2)
            cv2.circle(image, tuple(tag.corners[3].astype(int)), 4,(255,255,255), 2)
            
            color_detect_x[count]=tag.corners[0].astype(int)[0]
            color_detect_y[count]=tag.corners[0].astype(int)[1]
            color_detect_id[count]=tag.tag_id
            
            count=count+1
    cv2.imshow('camera', image)
    image1 = cv2.imread('image.png') 
    cv2.imshow('flow', image1)
    cv2.waitKey(1)
    
    for i in range(8,0,-1):
        for j in range(0,i):
            if(color_detect_y[j]>color_detect_y[j+1]):
                temp=color_detect_x[j]
                color_detect_x[j]=color_detect_x[j+1]
                color_detect_x[j+1]=temp
                temp=color_detect_y[j]
                color_detect_y[j]=color_detect_y[j+1]
                color_detect_y[j+1]=temp
                temp=color_detect_id[j]
                color_detect_id[j]=color_detect_id[j+1]
                color_detect_id[j+1]=temp

                
    for i in range(2,0,-1):
        for j in range(0,i):
            if(color_detect_x[j]>color_detect_x[j+1]):
                temp=color_detect_x[j]
                color_detect_x[j]=color_detect_x[j+1]
                color_detect_x[j+1]=temp
                temp=color_detect_y[j]
                color_detect_y[j]=color_detect_y[j+1]
                color_detect_y[j+1]=temp
                temp=color_detect_id[j]
                color_detect_id[j]=color_detect_id[j+1]
                color_detect_id[j+1]=temp
    for i in range(5,3,-1):
        for j in range(3,i):
            if(color_detect_x[j]>color_detect_x[j+1]):
                temp=color_detect_x[j]
                color_detect_x[j]=color_detect_x[j+1]
                color_detect_x[j+1]=temp
                temp=color_detect_y[j]
                color_detect_y[j]=color_detect_y[j+1]
                color_detect_y[j+1]=temp
                temp=color_detect_id[j]
                color_detect_id[j]=color_detect_id[j+1]
                color_detect_id[j+1]=temp
    for i in range(8,6,-1):
        for j in range(6,i):
            if(color_detect_x[j]>color_detect_x[j+1]):
                temp=color_detect_x[j]
                color_detect_x[j]=color_detect_x[j+1]
                color_detect_x[j+1]=temp
                temp=color_detect_y[j]
                color_detect_y[j]=color_detect_y[j+1]
                color_detect_y[j+1]=temp
                temp=color_detect_id[j]
                color_detect_id[j]=color_detect_id[j+1]
                color_detect_id[j+1]=temp

    
    for i in range(0,9):
        now_color[i]=color_detect_id[i]
        
    return image

def read_image_and_detect_change():
    
    image=read_image()   
    change_flag=0
    op=0
    
    for i in range(0,9):
        if(top_color[i]!=now_color[i]):
            change_flag=1
    
    if (change_flag!=0):
        op=check_valid()
            
    if (change_flag!=0 and op):
        for i in range(0,9):
            top_color[i]=now_color[i]
            
        print('display:')
        for j in range(0,3):
            print(print_color(top_color[3*j]),
                  print_color(top_color[3*j+1]),
                  print_color(top_color[3*j+2]),'\n')
            
    cv2.imshow('camera', image)
    image1 = cv2.imread('image.png') 
    cv2.imshow('flow', image1)
    cv2.waitKey(1)
    return op

def print_op(op):
    
    if(op==1):
        print('右下')
    elif(op==2):
        print('右上')
    elif(op==3):
        print('左下')
    elif(op==4):
        print('左上')
    elif(op==5):
        print('上右')
    elif(op==6):
        print('上左')
    elif(op==7):
        print('下右')
    elif(op==8):
        print('下左')
    elif(op==9):
        print('中下')
    elif(op==10):
        print('中上')
    elif(op==11):
        print('橫右')
    elif(op==12):
        print('橫左')
    elif(op==13):
        print('右轉')
    elif(op==14):
        print('左轉')
    elif(op==15):
        print('右翻')
    elif(op==16):
        print('左翻')
    elif(op==17):
        print('上翻')
    elif(op==18):
        print('下翻')
    elif(op==19):
        print('右轉翻')
    elif(op==20):
        print('左轉翻')

def check_if_yellow_edge(x):
    if x>=46:
        return 1
    return 0

def check_blue():
    if(initial_color[1][0]==18 and initial_color[1][2]==16):
        return 1
    elif(initial_color[3][0]==18 and initial_color[3][2]==16):
        return 2
    elif(initial_color[2][0]==18 and initial_color[2][2]==16):
        return 3
    elif(initial_color[4][0]==18 and initial_color[4][2]==16):
        return 4
    
    return 0

def check_green():
    if(initial_color[1][0]==27 and initial_color[1][2]==25):
        return 1
    elif(initial_color[3][0]==27 and initial_color[3][2]==25):
        return 2
    elif(initial_color[2][0]==27 and initial_color[2][2]==25):
        return 3
    elif(initial_color[4][0]==27 and initial_color[4][2]==25):
        return 4
    
    return 0

def check_orange():
    if(initial_color[1][0]==36 and initial_color[1][2]==34):
        return 1
    elif(initial_color[3][0]==36 and initial_color[3][2]==34):
        return 2
    elif(initial_color[2][0]==36 and initial_color[2][2]==34):
        return 3
    elif(initial_color[4][0]==36 and initial_color[4][2]==34):
        return 4
    
    return 0

def check_red():
    if(initial_color[1][0]==45 and initial_color[1][2]==43):
        return 1
    elif(initial_color[3][0]==45 and initial_color[3][2]==43):
        return 2
    elif(initial_color[2][0]==45 and initial_color[2][2]==43):
        return 3
    elif(initial_color[4][0]==45 and initial_color[4][2]==43):
        return 4
    
    return 0

def check_edge_and_middle(x,y):
    if(abs(x-y)==3):
        return 1
    
    return 0

toImage = Image.new('RGBA',(800,100))
fromImge = Image.open('white.png')
loc = (0,0)
toImage.paste(fromImge, loc)
font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
draw = ImageDraw.Draw(toImage)
draw.text((20, 40), '白色中心塊朝上 藍色中心塊朝前面 完成後開始教學',font=font, fill=(0,0,0))
toImage.save('word.png')
toImage = Image.new('RGBA',(800,500))
fromImge = Image.open('white.png')
loc = (0,0)
toImage.paste(fromImge, loc)
fromImge = Image.open('word.png')
loc = (0,0)
toImage.paste(fromImge, loc)
fromImge = Image.open('q16.png')
loc = (0,100)
toImage.paste(fromImge, loc)
toImage.save('image.png')
image1 = cv2.imread('image.png') 
cv2.imshow('flow', image1)
    
while (1):
    
    image=read_image()
    
    for i in range(0,9):
        now_color[i]=color_detect_id[i]
        
    if(initial_color_done[int((now_color[4]-5)/9)]==0 and now_color[4]!=0):
        initial_color_done[int((now_color[4]-5)/9)]=1
        for i in range(0,9):
            initial_color[int((now_color[4]-5)/9)][i]=color_detect_id[i]
            

      
    cv2.imshow('camera', image)
    image1 = cv2.imread('image.png') 
    #cv2.imshow('flow', image1)
    cv2.waitKey(1)
    
    if(sum(initial_color_done)==6):
        break

for i in range(1,5):
    for j in range(1,5):
        if j==1:
            index=7
        if j==2:
            index=1
        if j==3 :
            index=5
        if j==4:
            index=3
        for k in range(1,5):
            if(check_edge(initial_color[0][index],initial_color[i][1])==1):
                break
            temp=initial_color[i][1]
            initial_color[i][1]=initial_color[i][3]
            initial_color[i][3]=initial_color[i][7]
            initial_color[i][7]=initial_color[i][5]
            initial_color[i][5]=temp
            temp=initial_color[i][0]
            initial_color[i][0]=initial_color[i][6]
            initial_color[i][6]=initial_color[i][8]
            initial_color[i][8]=initial_color[i][2]
            initial_color[i][2]=temp


while(check_edge(initial_color[1][7],initial_color[5][1])==0):
    temp=initial_color[5][1]
    initial_color[5][1]=initial_color[5][3]
    initial_color[5][3]=initial_color[5][7]
    initial_color[5][7]=initial_color[5][5]
    initial_color[5][5]=temp
    temp=initial_color[5][0]
    initial_color[5][0]=initial_color[5][6]
    initial_color[5][6]=initial_color[5][8]
    initial_color[5][8]=initial_color[5][2]
    initial_color[5][2]=temp        

for i in range(1,5):
    if(check_edge(initial_color[0][7],initial_color[1][1])==1):
        break
    temp=initial_color[0][1]
    initial_color[0][1]=initial_color[0][3]
    initial_color[0][3]=initial_color[0][7]
    initial_color[0][7]=initial_color[0][5]
    initial_color[0][5]=temp
    temp=initial_color[0][0]
    initial_color[0][0]=initial_color[0][6]
    initial_color[0][6]=initial_color[0][8]
    initial_color[0][8]=initial_color[0][2]
    initial_color[0][2]=temp
    
for i in range(0,9):
    top_color[i]=initial_color[0][i]
    
    
print('display:')
for i in range(0,6):
    print('\n')
    for j in range(0,3):
        print(print_color(initial_color[i][3*j]),
              print_color(initial_color[i][3*j+1]),
              print_color(initial_color[i][3*j+2]),'\n')
        write__color_file(initial_color[i][3*j])
        write__color_file(initial_color[i][3*j+1])
        write__color_file(initial_color[i][3*j+2])
        



while(1):

    image=read_image()
    
    
    initial_flag=0
    
    for i in range(0,9):
        if(now_color[i]!=initial_color[0][i]):
            initial_flag=1
            
    if(initial_flag==0):
       print('start!')
       break
   
     
    
    cv2.imshow('camera', image)
    image1 = cv2.imread('image.png') 
    cv2.imshow('flow', image1)
    cv2.waitKey(1)
    
toImage = Image.new('RGBA',(800,100))
fromImge = Image.open('white.png')
loc = (0,0)
toImage.paste(fromImge, loc)
font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
draw = ImageDraw.Draw(toImage)
draw.text((20, 40), '首先完成四個邊塊',font=font, fill=(0,0,0))
toImage.save('word.png')
toImage = Image.new('RGBA',(800,500))
fromImge = Image.open('white.png')
loc = (0,0)
toImage.paste(fromImge, loc)
fromImge = Image.open('word.png')
loc = (0,0)
toImage.paste(fromImge, loc)
fromImge = Image.open('q1.png')
loc = (0,100)
toImage.paste(fromImge, loc)
toImage.save('image.png')
cv2.imshow('flow', image1)
i1=0
while(i1<50):
    image=read_image()
    cv2.imshow('camera', image)
    i1=i1+1

                
            
    
for it in range(0,4):#完成邊塊

    if(it==0):
        color1=8
        color2=11
        string='藍'
    elif(it==1):
        color1=6
        color2=29
        string='橘'
    elif(it==2):
        color1=2
        color2=20
        string='綠'
    elif(it==3):
        color1=4
        color2=38
        string='紅'

    toImage = Image.new('RGBA',(800,100))
    fromImge = Image.open('white.png')
    loc = (0,0)
    toImage.paste(fromImge, loc)
    font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
    draw = ImageDraw.Draw(toImage)
    draw.text((20, 40), '將白'+string+'邊塊轉至 白色中心塊和'+string+'色中心塊之間',font=font, fill=(0,0,0))
    toImage.save('word.png')
    toImage = Image.new('RGBA',(800,500))
    fromImge = Image.open('white.png')
    loc = (0,0)
    toImage.paste(fromImge, loc)
    fromImge = Image.open('word.png')
    loc = (0,0)
    toImage.paste(fromImge, loc)
    fromImge = Image.open('q'+str(it+2)+'.png')
    loc = (0,100)
    toImage.paste(fromImge, loc)
    toImage.save('image.png')
    cv2.imshow('flow', image1)

    ii=0
    while(ii<50):
        image=read_image()
        cv2.imshow('camera', image)
        ii=ii+1
    
    
    
    operation=[]
    print('將白'+string+'邊塊轉至 白色中心塊和'+string+'色中心塊之間')
    
    if(initial_color[0][7]==color1 and initial_color[1][1]==color2):
        operation=['白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[1][1]==color1 and initial_color[0][7]==color2):
        operation=['白'+string+'邊塊在正確位置 但方向錯誤','p8.png',7,14,2,13,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[3][3]==color1 and initial_color[1][5]==color2):
        operation=['白'+string+'邊塊在前面右側','p12.png',8,'白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[1][5]==color1 and initial_color[3][3]==color2):
        operation=['白'+string+'邊塊在前面右側','p12.png',14,2,13,'白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[4][5]==color1 and initial_color[1][3]==color2):
        operation=['白'+string+'邊塊在前面左側','p10.png',7,'白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[1][3]==color1 and initial_color[4][5]==color2):
        operation=['白'+string+'邊塊在前面左側','p10.png',13,4,14,'白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[5][1]==color1 and initial_color[1][7]==color2):
        operation=['白'+string+'邊塊在前面下方','p14.png',7,7,'白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[1][7]==color1 and initial_color[5][1]==color2):
        operation=['白'+string+'邊塊在前面下方','p14.png',7,13,4,14,'白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[0][5]==color1 and initial_color[3][1]==color2):
        operation=['白'+string+'邊塊在上面右側','p6.png',1,14,2,13,'白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[3][1]==color1 and initial_color[0][5]==color2):
        operation=['白'+string+'邊塊在上面右側','p6.png',1,8,'白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[2][3]==color1 and initial_color[3][5]==color2):
        operation=['白'+string+'邊塊在右側面',19,'白'+string+'邊塊在前面右側','p12.png',14,8,13,'回到左側面',20,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[3][5]==color1 and initial_color[2][3]==color2):
        operation=['白'+string+'邊塊在右側面',19,'白'+string+'邊塊在前面右側','p12.png',14,14,2,13,13,'回到左側面',20,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[5][5]==color1 and initial_color[3][7]==color2):
        operation=['白'+string+'邊塊在右側面',19,'白'+string+'邊塊在前面下方','p14.png',14,7,7,13,'回到左側面',20,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[3][7]==color1 and initial_color[5][5]==color2):
        operation=['白'+string+'邊塊在右側面',19,'白'+string+'邊塊在前面下方','p14.png',14,7,13,4,'回到左側面',20,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]        
    elif(initial_color[0][3]==color1 and initial_color[4][1]==color2):
        operation=['白'+string+'邊塊在上面左側','p4.png',14,'白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[4][1]==color1 and initial_color[0][3]==color2):
        operation=['白'+string+'邊塊在上面左側','p4.png',3,7,'白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]       
    elif(initial_color[2][5]==color1 and initial_color[4][3]==color2):
        operation=['白'+string+'邊塊在左側面',20,'白'+string+'邊塊在前面左側','p10.png',13,7,14,'回到右側面',19,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[4][3]==color1 and initial_color[2][5]==color2):
        operation=['白'+string+'邊塊在左側面',20,'白'+string+'邊塊在前面左側','p10.png',13,13,4,14,14,'回到右側面',19,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[5][3]==color1 and initial_color[4][7]==color2):
        operation=['白'+string+'邊塊在左側面',20,'白'+string+'邊塊在前面下方','p14.png',13,7,7,14,'回到右側面',19,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[4][7]==color1 and initial_color[5][3]==color2):
        operation=['白'+string+'邊塊在左側面',20,'白'+string+'邊塊在前面下方','p14.png',13,8,14,2,'回到右側面',19,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]        
    elif(initial_color[0][1]==color1 and initial_color[2][1]==color2):
        operation=['白'+string+'邊塊在上面上方','p2.png',3,13,13,4,'白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[2][1]==color1 and initial_color[0][1]==color2):
        operation=['白'+string+'邊塊在後面',20,20,'白'+string+'邊塊在前面上方','p8.png',7,13,2,14,'回到前面',19,19,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]        
    elif(initial_color[5][7]==color1 and initial_color[2][7]==color2):
        operation=['白'+string+'邊塊在後面',20,20,'白'+string+'邊塊在前面下方','p14.png',14,14,7,7,14,14,'回到前面',19,19,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
    elif(initial_color[2][7]==color1 and initial_color[5][7]==color2):
        operation=['白'+string+'邊塊在後面',20,20,'白'+string+'邊塊在前面下方','p14.png',14,14,7,13,4,13,'回到前面',19,19,
                   '白'+string+'邊塊已在正確位置 往右進行下一步','p8.png',19]
        
    
    print_op(operation[0])
    
    if(operation[0]==13 or operation[0]==14):
        key=0
    elif(operation[0]==19 or operation[0]==20):
        key=1
    
    while(len(operation)!=0):
        change_flag=read_image_and_detect_change()
        
        if(change_flag==operation[0] and len(operation)==1):
            operation=[]
            break
        elif(change_flag==operation[0]):
            operation=operation[1:]
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
        elif(check_str(str(operation[0]))==1):
            print(operation[0])
            toImage = Image.new('RGBA',(800,300))
            fromImge = Image.open('white.png')
            loc = (0,0)
            toImage.paste(fromImge, loc)
            font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
            draw = ImageDraw.Draw(toImage)
            draw.text((20, 40), operation[0],font=font, fill=(0,0,0))
            
            operation=operation[1:]
            
            if(check_str(str(operation[0]))==1):
                fromImge = Image.open(operation[0])
                loc = (0,100)
                toImage.paste(fromImge, loc)
                operation=operation[1:]
                
            toImage.save('word.png')
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
     

toImage = Image.new('RGBA',(800,100))
fromImge = Image.open('white.png')
loc = (0,0)
toImage.paste(fromImge, loc)
font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
draw = ImageDraw.Draw(toImage)
draw.text((20, 40), '接下來完成四個角塊',font=font, fill=(0,0,0))
toImage.save('word.png')
toImage = Image.new('RGBA',(800,500))
fromImge = Image.open('white.png')
loc = (0,0)
toImage.paste(fromImge, loc)
fromImge = Image.open('word.png')
loc = (0,0)
toImage.paste(fromImge, loc)
fromImge = Image.open('q6.png')
loc = (0,100)
toImage.paste(fromImge, loc)
toImage.save('image.png')
cv2.imshow('flow', image1)
i1=0
while(i1<50):
    image=read_image()
    cv2.imshow('camera', image)
    i1=i1+1
                  
    
for it in range(0,4):#完成角塊
    
    if(it==0):
        color1=9
        string1='藍'
        string2='橘'
    elif(it==1):
        color1=3
        string1='橘'
        string2='綠'
    elif(it==2):
        color1=1
        string1='綠'
        string2='紅'
    elif(it==3):
        color1=7
        string1='紅'
        string2='藍'
        
    toImage = Image.new('RGBA',(800,100))
    fromImge = Image.open('white.png')
    loc = (0,0)
    toImage.paste(fromImge, loc)
    font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
    draw = ImageDraw.Draw(toImage)
    draw.text((20, 40), '將白'+string1+string2+'角塊轉至 白'+string1+'邊塊和白'+string2+'邊塊之間',font=font, fill=(0,0,0))
    toImage.save('word.png')
    toImage = Image.new('RGBA',(800,500))
    fromImge = Image.open('white.png')
    loc = (0,0)
    toImage.paste(fromImge, loc)
    fromImge = Image.open('word.png')
    loc = (0,0)
    toImage.paste(fromImge, loc)
    fromImge = Image.open('q'+str(it+7)+'.png')
    loc = (0,100)
    toImage.paste(fromImge, loc)
    toImage.save('image.png')
    cv2.imshow('flow', image1)

    ii=0
    while(ii<50):
        image=read_image()
        cv2.imshow('camera', image)
        ii=ii+1
    
    operation=[]
    print('將白'+string1+string2+'角塊轉至 白'+string1+'邊塊和白'+string2+'邊塊之間')
    
    if(initial_color[0][8]==color1):
        operation=['白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[1][2]==color1):
        operation=['白'+string1+string2+'角塊在右上角 用角塊右四步法 將白'+string1+string2+'角塊轉至右下角','j2.png',
                   2,8,1,7,'白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[3][0]==color1):
        operation=['白'+string1+string2+'角塊在右側面',19,'白'+string1+string2+'角塊在左上角 用角塊左四步法 將白'+string1+string2+'角塊轉至左下角','j5.png',
                   4,7,3,8,'白'+string1+string2+'角塊在左下角 用角塊左四步法 將白'+string1+string2+'角塊轉至正確位置','j6.png',
                   4,7,3,8,'回到左側面',20,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
        
    elif(initial_color[1][8]==color1):
        operation=['白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[5][2]==color1):
        operation=['白'+string1+string2+'角塊在底面右邊 用角塊右四步法 將白'+string1+string2+'角塊轉至右上角','j1.png',
                   2,8,1,7,'白'+string1+string2+'角塊在右上角 用角塊右四步法 將白'+string1+string2+'角塊轉至右下角','j2.png',
                   2,8,1,7,'白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[3][6]==color1):
        operation=['白'+string1+string2+'角塊在右側面',19,'白'+string1+string2+'角塊在左下角 用角塊左四步法 將白'+string1+string2+'角塊轉至正確位置','j6.png',
                   4,7,3,8,'回到左側面',20,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
        
    elif(initial_color[0][6]==color1):
        operation=['白'+string1+string2+'角塊在上面左邊(位置錯誤) 用角塊左四步法 將白'+string1+string2+'角塊轉下來','j8.png',
                   4,7,3,8,'白'+string1+string2+'角塊在左側面',20,'右轉對齊',13,
                   '白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'左轉歸位',14,'回到右側面',19,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[1][0]==color1):
        operation=['白'+string1+string2+'角塊在左上角 用角塊左四步法 將白'+string1+string2+'角塊轉至左下角','j5.png',
                   4,7,3,8,'右轉對齊',13,'白'+string1+string2+'角塊在左下角 用角塊左四步法 將白'+string1+string2+'角塊轉至正確位置','j6.png',
                   4,7,3,8,'左轉歸位',14,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[4][2]==color1):
        operation=['白'+string1+string2+'角塊在左側面',20,'白'+string1+string2+'角塊在右上角 用角塊右四步法 將白'+string1+string2+'角塊轉至右下角','j2.png',
                   2,8,1,7,'右轉對齊',13,'白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'左轉歸位',14,'回到右側面',19,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
        
    elif(initial_color[1][6]==color1):
        operation=['右轉對齊',13,'白'+string1+string2+'角塊在左下角 用角塊左四步法 將白'+string1+string2+'角塊轉至正確位置','j6.png',
                   4,7,3,8,'左轉歸位',14,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[5][0]==color1):
        operation=['右轉對齊',13,'白'+string1+string2+'角塊在底面左邊 用角塊右四步法 將白'+string1+string2+'角塊轉至左上角','j4.png',
                   4,7,3,8,'白'+string1+string2+'角塊在左上角 用角塊左四步法 將白'+string1+string2+'角塊轉至左下角','j5.png',
                   4,7,3,8,'白'+string1+string2+'角塊在左下角 用角塊左四步法 將白'+string1+string2+'角塊轉至正確位置','j6.png',
                   4,7,3,8,'左轉歸位',14,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[4][8]==color1):
        operation=['白'+string1+string2+'角塊在左側面',20,'右轉對齊',13,'白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'左轉歸位',14,'回到右側面',19,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]#
        
    elif(initial_color[0][0]==color1):
        operation=['白'+string1+string2+'角塊在後面',20,20,
                   '白'+string1+string2+'角塊在上面右邊(位置錯誤) 用角塊右四步法 將白'+string1+string2+'角塊轉下來','j7.png',
                   2,8,1,7,'白'+string1+string2+'角塊在右側面',19,'右轉對齊',13,13,
                   '白'+string1+string2+'角塊在左下角 用角塊左四步法 將白'+string1+string2+'角塊轉至正確位置','j6.png',
                   4,7,3,8,'左轉歸位',14,14,'回到右側面',19,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[2][2]==color1):
        operation=['白'+string1+string2+'角塊在後面',20,20,
                   '白'+string1+string2+'角塊在右上角 用角塊右四步法 將白'+string1+string2+'角塊轉至右下角','j2.png',
                   2,8,1,7,'右轉對齊',13,13,'白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'左轉歸位',14,14,'回到前面',19,19,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[4][0]==color1):
        operation=['白'+string1+string2+'角塊在左側面',20,
                   '白'+string1+string2+'角塊在左上角 用角塊左四步法 將白'+string1+string2+'角塊轉至左下角','j5.png',
                   4,7,3,8,'右轉對齊',13,13,'白'+string1+string2+'角塊在左下角 用角塊左四步法 將白'+string1+string2+'角塊轉至正確位置','j6.png',
                   4,7,3,8,'左轉歸位',14,14,'回到右側面',19,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
        
    elif(initial_color[2][8]==color1):
        operation=['白'+string1+string2+'角塊在後面',20,20,'右轉對齊',13,13,
                   '白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'左轉歸位',14,14,'回到前面',19,19,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[5][6]==color1):
        operation=['白'+string1+string2+'角塊在後面',20,20,'右轉對齊',13,13,
                   '白'+string1+string2+'角塊在底面右邊 用角塊右四步法 將白'+string1+string2+'角塊轉至右上角','j1.png',
                   2,8,1,7,'白'+string1+string2+'角塊在右上角 用角塊右四步法 將白'+string1+string2+'角塊轉至右下角','j2.png',
                   2,8,1,7,'白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'左轉歸位',14,14,'回到前面',19,19,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[4][6]==color1):
        operation=['白'+string1+string2+'角塊在左側面',20,'右轉對齊',13,13,
                   '白'+string1+string2+'角塊在左下角 用角塊左四步法 將白'+string1+string2+'角塊轉至正確位置','j6.png',
                   4,7,3,8,'左轉歸位',14,14,'回到右側面',19,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
        
    elif(initial_color[0][2]==color1):
        operation=['白'+string1+string2+'角塊在後面',19,19,
                   '白'+string1+string2+'角塊在上面左邊(位置錯誤) 用角塊左四步法 將白'+string1+string2+'角塊轉下來','j8.png',
                   4,7,3,8,'白'+string1+string2+'角塊在左側面',20,'左轉對齊',14,
                   '白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'右轉歸位',13,'回到左側面',20,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[2][0]==color1):
        operation=['白'+string1+string2+'角塊在後面',19,19,
                   '白'+string1+string2+'角塊在左上角 用角塊左四步法 將白'+string1+string2+'角塊轉至左下角','j5.png',
                   4,7,3,8,'左轉對齊',14,
                   '白'+string1+string2+'角塊在左下角 用角塊左四步法 將白'+string1+string2+'角塊轉至正確位置','j6.png',
                   4,7,3,8,'右轉歸位',13,'回到前面',20,20,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[3][2]==color1):
        operation=['白'+string1+string2+'角塊在右側面',19,
                   '白'+string1+string2+'角塊在右上角 用角塊右四步法 將白'+string1+string2+'角塊轉至右下角','j2.png',
                   2,8,1,7,'左轉對齊',14,
                   '白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'右轉歸位',13,'回到左側面',20,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
        
    elif(initial_color[2][6]==color1):
        operation=['白'+string1+string2+'角塊在後面',19,19,'左轉對齊',14,
                   '白'+string1+string2+'角塊在左下角 用角塊左四步法 將白'+string1+string2+'角塊轉至正確位置','j6.png',
                   4,7,3,8,'右轉歸位',13,'回到前面',20,20,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[5][8]==color1):
        operation=['白'+string1+string2+'角塊在後面',19,19,'左轉對齊',14,
                   '白'+string1+string2+'角塊在底面左邊 用角塊右四步法 將白'+string1+string2+'角塊轉至左上角','j4.png',
                   4,7,3,8, '白'+string1+string2+'角塊在左上角 用角塊左四步法 將白'+string1+string2+'角塊轉至左下角','j5.png',
                   4,7,3,8, '白'+string1+string2+'角塊在左下角 用角塊左四步法 將白'+string1+string2+'角塊轉至正確位置','j6.png',
                   4,7,3,8,'右轉歸位',13,'回到前面',20,20,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    elif(initial_color[3][8]==color1):
        operation=['白'+string1+string2+'角塊在右側面',19,'左轉對齊',14,
                   '白'+string1+string2+'角塊在右下角 用角塊右四步法 將白'+string1+string2+'角塊轉至正確位置','j3.png',
                   2,8,1,7,'右轉歸位',13,'回到左側面',20,'白'+string1+string2+'角塊已在正確位置 往右進行下一步','p9.png',19]
    
        
    print_op(operation[0])
    
    if(operation[0]==13 or operation[0]==14):
        key=0
    elif(operation[0]==19 or operation[0]==20):
        key=1
    
    while(len(operation)!=0):
        change_flag=read_image_and_detect_change()
        
        if(change_flag==operation[0] and len(operation)==1):
            operation=[]
            break
        elif(change_flag==operation[0]):
            operation=operation[1:]
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
        elif(check_str(str(operation[0]))==1):
            print(operation[0])
            toImage = Image.new('RGBA',(800,300))
            fromImge = Image.open('white.png')
            loc = (0,0)
            toImage.paste(fromImge, loc)
            font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
            draw = ImageDraw.Draw(toImage)
            draw.text((20, 40), operation[0],font=font, fill=(0,0,0))
            
            operation=operation[1:]
            
            if(check_str(str(operation[0]))==1):
                fromImge = Image.open(operation[0])
                loc = (0,100)
                toImage.paste(fromImge, loc)
                operation=operation[1:]
                
            toImage.save('word.png')
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
                
toImage = Image.new('RGBA',(800,100))
fromImge = Image.open('white.png')
loc = (0,0)
toImage.paste(fromImge, loc)
font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
draw = ImageDraw.Draw(toImage)
draw.text((20, 40), '接下來完成第二層',font=font, fill=(0,0,0))
toImage.save('word.png')
toImage = Image.new('RGBA',(800,500))
fromImge = Image.open('white.png')
loc = (0,0)
toImage.paste(fromImge, loc)
fromImge = Image.open('word.png')
loc = (0,0)
toImage.paste(fromImge, loc)
fromImge = Image.open('q11.png')
loc = (0,100)
toImage.paste(fromImge, loc)
toImage.save('image.png')
cv2.imshow('flow', image1)
i1=0
while(i1<50):
    image=read_image()
    cv2.imshow('camera', image)
    i1=i1+1               


while (1):#翻到底部
    
    print('第一層已完成')
    operation=['翻至底部準備',15,15]
           
    print_op(operation[0])
    
    if(operation[0]==13 or operation[0]==14):
        key=0
    elif(operation[0]==19 or operation[0]==20):
        key=1
    
    while(len(operation)!=0):
        change_flag=read_image_and_detect_change()
        
        if(change_flag==operation[0] and len(operation)==1):
            operation=[]
            break
        elif(change_flag==operation[0]):
            operation=operation[1:]
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
        elif(check_str(str(operation[0]))==1):
            print(operation[0])
            toImage = Image.new('RGBA',(800,300))
            fromImge = Image.open('white.png')
            loc = (0,0)
            toImage.paste(fromImge, loc)
            font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
            draw = ImageDraw.Draw(toImage)
            draw.text((20, 40), operation[0],font=font, fill=(0,0,0))
            
            operation=operation[1:]
            
            if(check_str(str(operation[0]))==1):
                fromImge = Image.open(operation[0])
                loc = (0,100)
                toImage.paste(fromImge, loc)
                operation=operation[1:]
                
            toImage.save('word.png')
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
    break


for it in range(0,4):
    
    if(it==0):
        color1=13
        string1='藍'
        string2='紅'
    elif(it==1):
        color1=40
        string1='紅'
        string2='綠'
    elif(it==2):
        color1=22
        string1='綠'
        string2='橘'
    elif(it==3):
        color1=31
        string1='橘'
        string2='藍'
        
    toImage = Image.new('RGBA',(800,100))
    fromImge = Image.open('white.png')
    loc = (0,0)
    toImage.paste(fromImge, loc)
    font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
    draw = ImageDraw.Draw(toImage)
    draw.text((20, 40), '將'+string1+string2+'邊塊轉至正確位置',font=font, fill=(0,0,0))
    toImage.save('word.png')
    toImage = Image.new('RGBA',(800,500))
    fromImge = Image.open('white.png')
    loc = (0,0)
    toImage.paste(fromImge, loc)
    fromImge = Image.open('word.png')
    loc = (0,0)
    toImage.paste(fromImge, loc)
    fromImge = Image.open('q'+str(it+12)+'.png')
    loc = (0,100)
    toImage.paste(fromImge, loc)
    toImage.save('image.png')
    cv2.imshow('flow', image1)

    ii=0
    while(ii<50):
        image=read_image()
        cv2.imshow('camera', image)
        ii=ii+1
    
    print('將'+string1+string2+'邊塊轉至正確位置')
    operation=[]
    
    if(initial_color[1][1]==color1):
        operation=['用右邊塊八步法 將'+string1+string2+'轉至正確位置','m1.png',13,2,14,1,14,8,13,7,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[4][1]==color1):
        operation=[string1+string2+'邊塊在左方','p4.png',14,'用右邊塊八步法 將'+string1+string2+'轉至正確位置','m1.png',
                   13,2,14,1,14,8,13,7,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[2][1]==color1):
        operation=[string1+string2+'邊塊在後方','p2.png',14,14,'用右邊塊八步法 將'+string1+string2+'轉至正確位置','m1.png',
                   13,2,14,1,14,8,13,7,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[3][1]==color1):
        operation=[string1+string2+'邊塊在右方','p6.png',13,'用右邊塊八步法 將'+string1+string2+'轉至正確位置','m1.png',
                   13,2,14,1,14,8,13,7,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
        
    elif(initial_color[0][7]==color1):
        operation=['翻至右側面準備',19,string1+string2+'邊塊在左方','p4.png',14,'用左邊塊八步法 將'+string1+string2+'轉至正確位置','m2.png',
                   14,4,13,3,13,7,14,8,'回到左側面',20,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[0][5]==color1):
        operation=['翻至右側面準備',19,'用左邊塊八步法 將'+string1+string2+'轉至正確位置','m2.png',
                   14,4,13,3,13,7,14,8,'回到左側面',20,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[0][1]==color1):
        operation=['翻至右側面準備',19,string1+string2+'邊塊在右方','p6.png',13,'用左邊塊八步法 將'+string1+string2+'轉至正確位置','m2.png',
                   14,4,13,3,13,7,14,8,'回到左側面',20,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[0][3]==color1):
        operation=['翻至右側面準備',19,string1+string2+'邊塊在後方','p2.png',13,13,'用左邊塊八步法 將'+string1+string2+'轉至正確位置','m2.png',
                   14,4,13,3,13,7,14,8,'回到左側面',20,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
        
    elif(initial_color[1][5]==color1):
        operation=[string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[3][5]==color1):
        operation=[string1+string2+'邊塊在右側面',19,string1+string2+'邊塊在錯誤位置 用右邊塊八步法將其轉出來','m3.png',
                   13,2,14,1,14,8,13,7,string1+string2+'邊塊在後方','p2.png',13,13,
                   '用左邊塊八步法 將'+string1+string2+'轉至正確位置','m2.png',
                   14,4,13,3,13,7,14,8,'回到左側面',20,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[2][5]==color1):
        operation=[string1+string2+'邊塊在後面',19,19,string1+string2+'邊塊在錯誤位置 用右邊塊八步法將其轉出來','m3.png',
                   13,2,14,1,14,8,13,7,'翻至左側面準備',20,string1+string2+'邊塊在左方','p4.png',14,
                   '用左邊塊八步法 將'+string1+string2+'轉至正確位置','m2.png',
                   14,4,13,3,13,7,14,8,'回到左側面',20,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[4][5]==color1):
        operation=[string1+string2+'邊塊在左側面',20,string1+string2+'邊塊在錯誤位置 用右邊塊八步法將其轉出來','m3.png',
                   13,2,14,1,14,8,13,7,'翻至後面準備',19,19,
                   '用左邊塊八步法 將'+string1+string2+'轉至正確位置','m2.png',
                   14,4,13,3,13,7,14,8,'回到左側面',20,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
        
    elif(initial_color[3][3]==color1):
        operation=[string1+string2+'邊塊在正確位置 但方向錯誤 用右邊塊八步法將其轉出來','m3.png',
                   13,2,14,1,14,8,13,7,string1+string2+'邊塊在後方','p2.png',13,13,
                   '用右邊塊八步法 將'+string1+string2+'轉至正確位置','m1.png',
                   13,2,14,1,14,8,13,7,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[2][3]==color1):
        operation=[string1+string2+'邊塊在右側面',19,string1+string2+'邊塊在錯誤位置 用右邊塊八步法將其轉出來','m3.png',
                   13,2,14,1,14,8,13,7,'翻至左側面準備',20,string1+string2+'邊塊在左方','p4.png',14,
                   '用右邊塊八步法 將'+string1+string2+'轉至正確位置','m1.png',
                   13,2,14,1,14,8,13,7,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[4][3]==color1):
        operation=[string1+string2+'邊塊在後面',19,19,string1+string2+'邊塊在錯誤位置 用右邊塊八步法將其轉出來','m3.png',
                   13,2,14,1,14,8,13,7,'翻至後面準備',20,20,
                   '用右邊塊八步法 將'+string1+string2+'轉至正確位置','m1.png',
                   13,2,14,1,14,8,13,7,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    elif(initial_color[1][3]==color1):
        operation=[string1+string2+'邊塊在左側面',20,string1+string2+'邊塊在錯誤位置 用右邊塊八步法將其轉出來','m3.png',
                   13,2,14,1,14,8,13,7,'翻至右側面準備',19,'邊塊在右方','p6.png',13,
                   '用右邊塊八步法 將'+string1+string2+'轉至正確位置','m1.png',
                   13,2,14,1,14,8,13,7,string1+string2+'邊塊已在正確位置 往右進行下一步','p12.png',19]
    
    
        
    print_op(operation[0])
    
    if(operation[0]==13 or operation[0]==14):
        key=0
    elif(operation[0]==19 or operation[0]==20):
        key=1
    
    while(len(operation)!=0):
        change_flag=read_image_and_detect_change()
        
        if(change_flag==operation[0] and len(operation)==1):
            operation=[]
            break
        elif(change_flag==operation[0]):
            operation=operation[1:]
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
        elif(check_str(str(operation[0]))==1):
            print(operation[0])
            toImage = Image.new('RGBA',(800,300))
            fromImge = Image.open('white.png')
            loc = (0,0)
            toImage.paste(fromImge, loc)
            font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
            draw = ImageDraw.Draw(toImage)
            draw.text((20, 40), operation[0],font=font, fill=(0,0,0))
            
            operation=operation[1:]
            
            if(check_str(str(operation[0]))==1):
                fromImge = Image.open(operation[0])
                loc = (0,100)
                toImage.paste(fromImge, loc)
                operation=operation[1:]
                
            toImage.save('word.png')
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1

print('完成第二層')

while (1):#頂面角塊都不是黃色
    
    operation=[]
    
    check_yellow_flag=0
    
    if(check_if_yellow_edge(initial_color[0][1])==0 and check_if_yellow_edge(initial_color[0][3])==0
      and check_if_yellow_edge(initial_color[0][5])==0 and check_if_yellow_edge(initial_color[0][7])==0):
        check_yellow_flag=1
        print('頂面角塊沒有黃色')
    
    if check_yellow_flag==0:
        break
    
    operation=['頂面角塊沒有黃色 使用六步法 讓頂面角塊出現兩個黃色','u1.png',1,14,8,13,7,2]
    
    
        
    print_op(operation[0])
    
    if(operation[0]==13 or operation[0]==14):
        key=0
    elif(operation[0]==19 or operation[0]==20):
        key=1
    
    while(len(operation)!=0):
        change_flag=read_image_and_detect_change()
        
        if(change_flag==operation[0] and len(operation)==1):
            operation=[]
            break
        elif(change_flag==operation[0]):
            operation=operation[1:]
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
        elif(check_str(str(operation[0]))==1):
            print(operation[0])
            toImage = Image.new('RGBA',(800,300))
            fromImge = Image.open('white.png')
            loc = (0,0)
            toImage.paste(fromImge, loc)
            font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
            draw = ImageDraw.Draw(toImage)
            draw.text((20, 40), operation[0],font=font, fill=(0,0,0))
            
            operation=operation[1:]
            
            if(check_str(str(operation[0]))==1):
                fromImge = Image.open(operation[0])
                loc = (0,100)
                toImage.paste(fromImge, loc)
                operation=operation[1:]
                
            toImage.save('word.png')
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1

while (1):#頂面角塊兩個黃色
    
    operation=[]
    
    check_yellow_flag=0
    
    if(check_if_yellow_edge(initial_color[0][1])==1 and check_if_yellow_edge(initial_color[0][3])==0
      and check_if_yellow_edge(initial_color[0][5])==0 and check_if_yellow_edge(initial_color[0][7])==1):#直線
        check_yellow_flag=1
        operation=['直線型 使用六步法 將黃色角塊變成倒L型','u2.png',1,14,8,13,7,2]
    elif(check_if_yellow_edge(initial_color[0][1])==0 and check_if_yellow_edge(initial_color[0][3])==1
      and check_if_yellow_edge(initial_color[0][5])==1 and check_if_yellow_edge(initial_color[0][7])==0):#橫線
        check_yellow_flag=1
        operation=['右轉讓黃色角塊變成一直線','u3.png',13]
    elif(check_if_yellow_edge(initial_color[0][1])==1 and check_if_yellow_edge(initial_color[0][3])==0
      and check_if_yellow_edge(initial_color[0][5])==1 and check_if_yellow_edge(initial_color[0][7])==0):#上右
        check_yellow_flag=1
        operation=['左轉將黃色角塊變成倒L型','u4.png',14]
    elif(check_if_yellow_edge(initial_color[0][1])==1 and check_if_yellow_edge(initial_color[0][3])==1
      and check_if_yellow_edge(initial_color[0][5])==0 and check_if_yellow_edge(initial_color[0][7])==0):#上左
        check_yellow_flag=1
        operation=['倒L型 使用六步法 讓頂面角塊出現四個黃色','u5.png',1,14,8,13,7,2]
    elif(check_if_yellow_edge(initial_color[0][1])==0 and check_if_yellow_edge(initial_color[0][3])==0
      and check_if_yellow_edge(initial_color[0][5])==1 and check_if_yellow_edge(initial_color[0][7])==1):#下右
        check_yellow_flag=1
        operation=['右轉將黃色角塊變成倒L型','u6.png',13,13]
    elif(check_if_yellow_edge(initial_color[0][1])==0 and check_if_yellow_edge(initial_color[0][3])==1
      and check_if_yellow_edge(initial_color[0][5])==0 and check_if_yellow_edge(initial_color[0][7])==1):#下左
        check_yellow_flag=1
        operation=['右轉將黃色角塊變成倒L型','u7.png',13]
    
    if check_yellow_flag==0:
        break
        
    print_op(operation[0])
    
    if(operation[0]==13 or operation[0]==14):
        key=0
    elif(operation[0]==19 or operation[0]==20):
        key=1
    
    while(len(operation)!=0):
        change_flag=read_image_and_detect_change()
        
        if(change_flag==operation[0] and len(operation)==1):
            operation=[]
            break
        elif(change_flag==operation[0]):
            operation=operation[1:]
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
        elif(check_str(str(operation[0]))==1):
            print(operation[0])
            toImage = Image.new('RGBA',(800,300))
            fromImge = Image.open('white.png')
            loc = (0,0)
            toImage.paste(fromImge, loc)
            font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
            draw = ImageDraw.Draw(toImage)
            draw.text((20, 40), operation[0],font=font, fill=(0,0,0))
            
            operation=operation[1:]
            
            if(check_str(str(operation[0]))==1):
                fromImge = Image.open(operation[0])
                loc = (0,100)
                toImage.paste(fromImge, loc)
                operation=operation[1:]
                
            toImage.save('word.png')
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
                
while (1):#頂面邊塊都是黃色
    
    operation=[]
    
    check_yellow_flag=0
    
    if(check_if_yellow_edge(initial_color[1][0])==1 and check_if_yellow_edge(initial_color[1][2])==1
      and check_if_yellow_edge(initial_color[2][0])==1 and check_if_yellow_edge(initial_color[2][2])==1):#十字
        check_yellow_flag=1
        operation=['右轉使開口面向自己','a1.png',13]
    elif(check_if_yellow_edge(initial_color[3][0])==1 and check_if_yellow_edge(initial_color[3][2])==1
      and check_if_yellow_edge(initial_color[4][0])==1 and check_if_yellow_edge(initial_color[4][2])==1):#十字
        check_yellow_flag=1
        operation=['十字型 利用七步法 出現魚型','a2.png',2,14,4,13,1,14,3]
    elif(check_if_yellow_edge(initial_color[1][0])==1 and check_if_yellow_edge(initial_color[1][2])==1
      and check_if_yellow_edge(initial_color[3][2])==1 and check_if_yellow_edge(initial_color[4][0])==1):#十字
        check_yellow_flag=1
        operation=['右轉使開口面向自己','a3.png',13,13]
    elif(check_if_yellow_edge(initial_color[1][2])==1 and check_if_yellow_edge(initial_color[2][0])==1
      and check_if_yellow_edge(initial_color[4][0])==1 and check_if_yellow_edge(initial_color[4][2])==1):#十字
        check_yellow_flag=1
        operation=['右轉使開口面向自己','a4.png',13]
    elif(check_if_yellow_edge(initial_color[3][0])==1 and check_if_yellow_edge(initial_color[3][2])==1
      and check_if_yellow_edge(initial_color[1][0])==1 and check_if_yellow_edge(initial_color[2][2])==1):#十字
        check_yellow_flag=1
        operation=['左轉使開口面向自己','a5.png',14]
    elif(check_if_yellow_edge(initial_color[2][0])==1 and check_if_yellow_edge(initial_color[2][2])==1
      and check_if_yellow_edge(initial_color[3][0])==1 and check_if_yellow_edge(initial_color[4][2])==1):#十字
        check_yellow_flag=1
        operation=['十字型 利用七步法 出現魚型','a6.png',2,14,4,13,1,14,3]
        
    elif(check_if_yellow_edge(initial_color[0][0])==1 and check_if_yellow_edge(initial_color[0][8])==1
      and check_if_yellow_edge(initial_color[1][0])==1 and check_if_yellow_edge(initial_color[3][2])==1):#對角
        check_yellow_flag=1
        operation=['對角型 利用七步法 出現魚型','a7.png',2,14,4,13,1,14,3]
    elif(check_if_yellow_edge(initial_color[0][2])==1 and check_if_yellow_edge(initial_color[0][6])==1
      and check_if_yellow_edge(initial_color[1][2])==1 and check_if_yellow_edge(initial_color[4][0])==1):#對角
        check_yellow_flag=1
        operation=['左轉使開口朝右下','a8.png',14]
    elif(check_if_yellow_edge(initial_color[0][0])==1 and check_if_yellow_edge(initial_color[0][8])==1
      and check_if_yellow_edge(initial_color[2][0])==1 and check_if_yellow_edge(initial_color[4][2])==1):#對角
        check_yellow_flag=1
        operation=['左轉使開口朝右下','a9.png',14,14]
    elif(check_if_yellow_edge(initial_color[0][2])==1 and check_if_yellow_edge(initial_color[0][6])==1
      and check_if_yellow_edge(initial_color[2][2])==1 and check_if_yellow_edge(initial_color[3][0])==1):#對角
        check_yellow_flag=1
        operation=['右轉使開口朝右下','a10.png',13]
        
    elif(check_if_yellow_edge(initial_color[0][0])==1 and check_if_yellow_edge(initial_color[0][2])==1
      and check_if_yellow_edge(initial_color[1][0])==1 and check_if_yellow_edge(initial_color[1][2])==1):#凸型1
        check_yellow_flag=1
        operation=['凸型(兩角塊在一起) 利用七步法 出現魚型','a11.png',2,14,4,13,1,14,3]
    elif(check_if_yellow_edge(initial_color[0][2])==1 and check_if_yellow_edge(initial_color[0][8])==1
      and check_if_yellow_edge(initial_color[4][0])==1 and check_if_yellow_edge(initial_color[4][2])==1):#凸型1
        check_yellow_flag=1
        operation=['左轉使凸型頂部面向自己','a12.png',14]
    elif(check_if_yellow_edge(initial_color[0][6])==1 and check_if_yellow_edge(initial_color[0][8])==1
      and check_if_yellow_edge(initial_color[2][0])==1 and check_if_yellow_edge(initial_color[2][2])==1):#凸型1
        check_yellow_flag=1
        operation=['左轉使凸型頂部面向自己','a13.png',14,14]
    elif(check_if_yellow_edge(initial_color[0][0])==1 and check_if_yellow_edge(initial_color[0][6])==1
      and check_if_yellow_edge(initial_color[3][0])==1 and check_if_yellow_edge(initial_color[3][2])==1):#凸型1
        check_yellow_flag=1
        operation=['右轉使凸型頂部面向自己','a14.png',13]
        
    elif(check_if_yellow_edge(initial_color[0][0])==1 and check_if_yellow_edge(initial_color[0][2])==1
      and check_if_yellow_edge(initial_color[3][0])==1 and check_if_yellow_edge(initial_color[4][2])==1):#凸型2
        check_yellow_flag=1
        operation=['右轉使凸型頂部朝左','a15.png',13]
    elif(check_if_yellow_edge(initial_color[0][2])==1 and check_if_yellow_edge(initial_color[0][8])==1
      and check_if_yellow_edge(initial_color[1][0])==1 and check_if_yellow_edge(initial_color[2][2])==1):#凸型2
        check_yellow_flag=1
        operation=['凸型(兩角塊分開) 利用七步法 出現魚型','a16.png',2,14,4,13,1,14,3]
    elif(check_if_yellow_edge(initial_color[0][6])==1 and check_if_yellow_edge(initial_color[0][8])==1
      and check_if_yellow_edge(initial_color[3][2])==1 and check_if_yellow_edge(initial_color[4][0])==1):#凸型2
        check_yellow_flag=1
        operation=['左轉使凸型頂部朝左','a17.png',14]
    elif(check_if_yellow_edge(initial_color[0][0])==1 and check_if_yellow_edge(initial_color[0][6])==1
      and check_if_yellow_edge(initial_color[1][2])==1 and check_if_yellow_edge(initial_color[2][0])==1):#凸型2
        check_yellow_flag=1
        operation=['右轉使凸型頂部朝左','a18.png',13,13]
        
    elif(check_if_yellow_edge(initial_color[0][6])==1 and check_if_yellow_edge(initial_color[2][0])==1
      and check_if_yellow_edge(initial_color[3][0])==1 and check_if_yellow_edge(initial_color[4][0])==1):#右魚1
        check_yellow_flag=1
        operation=['假魚型(前方右上不是黃色) 利用七步法 出現真魚型','a19.png',2,14,4,13,1,14,3]
    elif(check_if_yellow_edge(initial_color[0][8])==1 and check_if_yellow_edge(initial_color[1][0])==1
      and check_if_yellow_edge(initial_color[2][0])==1 and check_if_yellow_edge(initial_color[4][0])==1):#右魚1
        check_yellow_flag=1
        operation=['右轉使魚頭朝左下','a20.png',13]
    elif(check_if_yellow_edge(initial_color[0][2])==1 and check_if_yellow_edge(initial_color[1][0])==1
      and check_if_yellow_edge(initial_color[3][0])==1 and check_if_yellow_edge(initial_color[4][0])==1):#右魚1
        check_yellow_flag=1
        operation=['左轉使魚頭朝左下','a21.png',14,14]
    elif(check_if_yellow_edge(initial_color[0][0])==1 and check_if_yellow_edge(initial_color[1][0])==1
      and check_if_yellow_edge(initial_color[2][0])==1 and check_if_yellow_edge(initial_color[3][0])==1):#右魚1
        check_yellow_flag=1
        operation=['左轉使魚頭朝左下','a22.png',14]
        
    elif(check_if_yellow_edge(initial_color[0][6])==1 and check_if_yellow_edge(initial_color[1][2])==1
      and check_if_yellow_edge(initial_color[2][2])==1 and check_if_yellow_edge(initial_color[3][2])==1):#右魚
        check_yellow_flag=1
        operation=['真魚型(前方右上是黃色) 利用七步法 完成第二面','a23.png',2,14,4,13,1,14,3]
    elif(check_if_yellow_edge(initial_color[0][8])==1 and check_if_yellow_edge(initial_color[2][2])==1
      and check_if_yellow_edge(initial_color[3][2])==1 and check_if_yellow_edge(initial_color[4][2])==1):#右魚
        check_yellow_flag=1
        operation=['右轉使魚頭朝左下','a20.png',13]
    elif(check_if_yellow_edge(initial_color[0][2])==1 and check_if_yellow_edge(initial_color[1][2])==1
      and check_if_yellow_edge(initial_color[2][2])==1 and check_if_yellow_edge(initial_color[4][2])==1):#右魚
        check_yellow_flag=1
        operation=['左轉使魚頭朝左下','a21.png',14,14]
    elif(check_if_yellow_edge(initial_color[0][0])==1 and check_if_yellow_edge(initial_color[1][2])==1
      and check_if_yellow_edge(initial_color[3][2])==1 and check_if_yellow_edge(initial_color[4][2])==1):#右魚
        check_yellow_flag=1
        operation=['左轉使魚頭朝左下','a22.png',14]
        
    if check_yellow_flag==0:
        break

    
    print_op(operation[0])
    
    if(operation[0]==13 or operation[0]==14):
        key=0
    elif(operation[0]==19 or operation[0]==20):
        key=1
    
    while(len(operation)!=0):
        change_flag=read_image_and_detect_change()
        
        if(change_flag==operation[0] and len(operation)==1):
            operation=[]
            break
        elif(change_flag==operation[0]):
            operation=operation[1:]
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
        elif(check_str(str(operation[0]))==1):
            print(operation[0])
            toImage = Image.new('RGBA',(800,300))
            fromImge = Image.open('white.png')
            loc = (0,0)
            toImage.paste(fromImge, loc)
            font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
            draw = ImageDraw.Draw(toImage)
            draw.text((20, 40), operation[0],font=font, fill=(0,0,0))
            
            operation=operation[1:]
            
            if(check_str(str(operation[0]))==1):
                fromImge = Image.open(operation[0])
                loc = (0,100)
                toImage.paste(fromImge, loc)
                operation=operation[1:]
                
            toImage.save('word.png')
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
     
while (1):#
    
    operation=[]
    
    check_yellow_flag=0
    
    if(check_blue()==0 and check_green()==0 and check_orange()==0 and check_red()==0):
        check_yellow_flag=1
        operation=['利用十三步法 讓右側兩邊塊對調 使同顏色角塊在同一面','b1.png',2,14,14,1,14,2,14,14,4,13,1,14,3]
        
    elif(check_blue()+check_green()+check_orange()+check_red()==10):
        check_yellow_flag=1
        if(initial_color[1][4]==initial_color[1][0]-4):
            check_yellow_flag=0
        elif(initial_color[1][4]==initial_color[2][0]-4):
            check_yellow_flag=1
            operation=['右轉使邊塊和中心塊對齊','b3.png',13,13]
        elif(initial_color[1][4]==initial_color[3][0]-4):
            check_yellow_flag=1
            operation=['右轉使邊塊和中心塊對齊','b2.png',13]
        elif(initial_color[1][4]==initial_color[4][0]-4):
            check_yellow_flag=1
            operation=['左轉使邊塊和中心塊對齊','b4.png',14]
    else:
        if(check_blue()==1 or check_green()==1 or check_orange()==1 or check_red()==1):
            check_yellow_flag=1
            operation=['右轉使處理好的邊塊在左側','b5.png',13]
        elif(check_blue()==2 or check_green()==2 or check_orange()==2 or check_red()==2):
            check_yellow_flag=1
            operation=['右轉使處理好的邊塊在左側','b6.png',13,13]
        elif(check_blue()==3 or check_green()==3 or check_orange()==3 or check_red()==3):
            check_yellow_flag=1
            operation=['左轉使處理好的邊塊在左側','b7.png',14]
        elif(check_blue()==4 or check_green()==4 or check_orange()==4 or check_red()==4):
            check_yellow_flag=1
            operation=['利用十三步法 讓右側兩邊塊對調 使同顏色角塊在同一面','b1.png',2,14,14,1,14,2,14,14,4,13,1,14,3]
    
    if check_yellow_flag==0:
        break
        
    print_op(operation[0])
    
    if(operation[0]==13 or operation[0]==14):
        key=0
    elif(operation[0]==19 or operation[0]==20):
        key=1
    
    while(len(operation)!=0):
        change_flag=read_image_and_detect_change()
        
        if(change_flag==operation[0] and len(operation)==1):
            operation=[]
            break
        elif(change_flag==operation[0]):
            operation=operation[1:]
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
        elif(check_str(str(operation[0]))==1):
            print(operation[0])
            toImage = Image.new('RGBA',(800,300))
            fromImge = Image.open('white.png')
            loc = (0,0)
            toImage.paste(fromImge, loc)
            font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
            draw = ImageDraw.Draw(toImage)
            draw.text((20, 40), operation[0],font=font, fill=(0,0,0))
            
            operation=operation[1:]
            
            if(check_str(str(operation[0]))==1):
                fromImge = Image.open(operation[0])
                loc = (0,100)
                toImage.paste(fromImge, loc)
                operation=operation[1:]
                
            toImage.save('word.png')
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1

while (1):#
    
    operation=[]
    
    check_yellow_flag=0
    
    if(check_edge_and_middle(initial_color[1][1],initial_color[1][4])==0 and
       check_edge_and_middle(initial_color[2][1],initial_color[2][4])==0 and
       check_edge_and_middle(initial_color[3][1],initial_color[3][4])==0 and
       check_edge_and_middle(initial_color[4][1],initial_color[4][4])==0):
        check_yellow_flag=1
        operation=['四面頂塊未對齊 利用右頂部角塊法 解出第三面','c1.png',10,10,13,9,13,13,10,13,10,10]
    elif(check_edge_and_middle(initial_color[1][1],initial_color[1][4])==1 and
       check_edge_and_middle(initial_color[2][1],initial_color[2][4])==1 and
       check_edge_and_middle(initial_color[3][1],initial_color[3][4])==1 and
       check_edge_and_middle(initial_color[4][1],initial_color[4][4])==1):
        check_yellow_flag=0
    elif(check_edge_and_middle(initial_color[1][1],initial_color[1][4])==1):
        check_yellow_flag=1
        operation=['使剛完成的第三面到背面',19,19]
    elif(check_edge_and_middle(initial_color[3][1],initial_color[3][4])==1):
        check_yellow_flag=1
        operation=['使剛完成的第三面到背面',20]
    elif(check_edge_and_middle(initial_color[4][1],initial_color[4][4])==1):
        check_yellow_flag=1
        operation=['使剛完成的第三面到背面',19]
    elif(initial_color[1][4]+3==initial_color[4][1]):
        check_yellow_flag=1
        operation=['利用右頂部角塊法 解出魔術方塊','c1.png',10,10,13,9,13,13,10,13,10,10]
    elif(initial_color[1][4]+3==initial_color[3][1]):
        check_yellow_flag=1
        operation=['利用左頂部角塊法 解出魔術方塊','c2.png',10,10,14,9,13,13,10,14,10,10]
        

    
    if check_yellow_flag==0:
        break
        
    print_op(operation[0])
    
    if(operation[0]==13 or operation[0]==14):
        key=0
    elif(operation[0]==19 or operation[0]==20):
        key=1
    
    while(len(operation)!=0):
        change_flag=read_image_and_detect_change()
        
        if(change_flag==operation[0] and len(operation)==1):
            operation=[]
            break
        elif(change_flag==operation[0]):
            operation=operation[1:]
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
        elif(check_str(str(operation[0]))==1):
            print(operation[0])
            toImage = Image.new('RGBA',(800,300))
            fromImge = Image.open('white.png')
            loc = (0,0)
            toImage.paste(fromImge, loc)
            font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
            draw = ImageDraw.Draw(toImage)
            draw.text((20, 40), operation[0],font=font, fill=(0,0,0))
            
            operation=operation[1:]
            
            if(check_str(str(operation[0]))==1):
                fromImge = Image.open(operation[0])
                loc = (0,100)
                toImage.paste(fromImge, loc)
                operation=operation[1:]
                
            toImage.save('word.png')
            print_operations(operation)
            if(operation[0]==13 or operation[0]==14):
                key=0
            elif(operation[0]==19 or operation[0]==20):
                key=1
                
'''print('display:')
for i in range(0,6):
    print('\n')
    for j in range(0,3):
        print(print_color(initial_color[i][3*j]),
              print_color(initial_color[i][3*j+1]),
              print_color(initial_color[i][3*j+2]),'\n')'''
        
print("well done!")

toImage = Image.new('RGBA',(800,100))
fromImge = Image.open('white.png')
loc = (0,0)
toImage.paste(fromImge, loc)
font = ImageFont.truetype("SimHei.ttf", 20, encoding="utf-8")
draw = ImageDraw.Draw(toImage)
draw.text((20, 40), 'Well Done!',font=font, fill=(0,0,0))
toImage.save('word.png')
toImage = Image.new('RGBA',(800,500))
fromImge = Image.open('white.png')
loc = (0,0)
toImage.paste(fromImge, loc)
fromImge = Image.open('word.png')
loc = (0,0)
toImage.paste(fromImge, loc)
toImage.save('image.png')
cv2.imshow('flow', image1)
i1=0
while(1):
    image=read_image()
    cv2.imshow('camera', image)
    i1=i1+1

