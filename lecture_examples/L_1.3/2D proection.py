#----------Набір скриптів, що демонструють технології реалізації графічних перетворень--------
# #---------------------------------Простий перенос скалярними операціями---------------------
from graphics import *
xw=600; yw=600; st=50
win = GraphWin("2-D проекции в библиотеке graphics", xw, yw)
win.setBackground('white')
dx = 50; dy = 50
x1=st; y1=yw-2*st; x2=2*st; y2=yw-st
x11=x1+dx; y11=y1-dy; x22=x2+dx; y22=y2-dy
obj = Rectangle(Point(x1, y1), Point(x2, y2))
obj.draw(win)
obj = Rectangle(Point(x11, y11), Point(x22, y22))
obj.draw(win)
win.getMouse()
win.close()
#------------------------------------Циклічний перенос скалярними операціями-----------------
import time
win = GraphWin("2-D проекции в библиотеке graphics ПЕРЕНОС", xw, yw)
win.setBackground('white')
dx = 50; dy = 50
x1=st; y1=yw-2*st; x2=2*st; y2=yw-st
x11=x1+dx; y11=y1-dy; x22=x2+dx; y22=y2-dy
obj = Rectangle(Point(x1, y1), Point(x2, y2))
obj.draw(win)
stop=xw/dx;
stop = float(stop)
ii = int(stop)
for i in range(ii):
    time.sleep(0.3)
    obj = Rectangle(Point(x11, y11), Point(x22, y22))
    obj.draw(win)
    x11 = x11 + dx;
    y11 = y11 - dy;
    x22 = x22 + dx;
    y22 = y22 - dy
win.getMouse()
win.close()
#-------------------------Циклічний перенос типу "РУХ" скалярними операціями-----------------
win = GraphWin("2-D проекции в библиотеке graphics ПЕРЕНОС З РУХОМ", xw, yw)
win.setBackground('white')
dx = 50; dy = 50
x1=st; y1=yw-2*st; x2=2*st; y2=yw-st
x11=x1+dx; y11=y1-dy; x22=x2+dx; y22=y2-dy
obj = Rectangle(Point(x1, y1), Point(x2, y2))
obj.draw(win)
stop=xw/dx;
stop = float(stop)
ii = int(stop)
for i in range(ii):
    time.sleep(0.2)
    obj.setOutline("white")
    obj = Rectangle(Point(x11, y11), Point(x22, y22))
    obj.draw(win)
    obj = Rectangle(Point(x11, y11), Point(x22, y22))
    obj.draw(win)
    x11 = x11 + dx;
    y11 = y11 - dy;
    x22 = x22 + dx;
    y22 = y22 - dy
win.getMouse()
win.close()
#-------------------------Циклічний перенос типу "РУХ" матричними операціями-----------------
win = GraphWin("2-D проекции в библиотеке graphics ПЕРЕНОС З РУХОМ матрицями", xw, yw)
win.setBackground('white')
dx = 50; dy = 50
x1=st; y1=yw-2*st; x2=2*st; y2=yw-st
#-------------------------блок матричних перетворень типу ПЕРЕНОС----------------------------
import numpy as np
a = np.array([ [x1, y1, 1] ])
f = np.array([ [1, 0, dx], [0, 1, -dy], [0, 0, 1] ])    # по строках
ft=f.T
total = a.dot(ft)
x11=total[0, 0];  y11=total[0, 1];
a2 = np.array([ [x2, y2, 1] ])
f2 = np.array([ [1, 0, dx], [0, 1, -dy], [0, 0, 1] ])
ft2=f2.T
total2 = a2.dot(ft2)
x22=total2[0, 0];  y22=total2[0, 1];
#-------------------------блок скалярних перетворень типу ПЕРЕНОС----------------------------
# x11=x1+dx; y11=y1-dy; x22=x2+dx; y22=y2-dy
obj = Rectangle(Point(x1, y1), Point(x2, y2))
obj.draw(win)
stop=xw/dx;
stop = float(stop)
ii = int(stop)
for i in range(ii):
    time.sleep(0.2)
    obj.setOutline("white")
    obj = Rectangle(Point(x11, y11), Point(x22, y22))
    obj.draw(win)
    obj = Rectangle(Point(x11, y11), Point(x22, y22))
    obj.draw(win)
    # ---------------------циклічний блок матричних перетворень типу ПЕРЕНОС------------------
    a = np.array([[x11, y11, 1]])
    f = np.array([[1, 0, dx], [0, 1, -dy], [0, 0, 1]])
    ft = f.T
    total = a.dot(ft)
    x11 = total[0, 0];
    y11 = total[0, 1];
    a2 = np.array([[x22, y22, 1]])
    f2 = np.array([[1, 0, dx], [0, 1, -dy], [0, 0, 1]])
    ft2 = f2.T
    total2 = a2.dot(ft2)
    x22 = total2[0, 0];
    y22 = total2[0, 1];
    # --------------------циклічний блок скалярних перетворень типу ПЕРЕНОС--------------------
    # x11 = x11 + dx;
    #  y11 = y11 - dy;
    #  x22 = x22 + dx;
    #  y22 = y22 - dy
win.getMouse()
win.close()
#--------------------------------------------------------------------------------------------

#--------------Циклічний перенос типу "РУХ" та поворот матричними операціями-----------------
win = GraphWin("2-D проекции в библиотеке graphics ПЕРЕНОС обертання З РУХОМ матрицями", xw, yw)
win.setBackground('white')
dx = 50; dy = 50
x1=st; y1=yw-2*st;
x2=2*st; y2=yw-2*st;
x3=2*st; y3=yw-st;
x4=st; y4=yw-st;

#-------------------------блок матричних перетворень типу ПЕРЕНОС----------------------------
import numpy as np
a = np.array([ [x1, y1, 1] ])
f = np.array([ [1, 0, dx], [0, 1, -dy], [0, 0, 1] ])
ft=f.T
total = a.dot(ft)
x11=total[0, 0];  y11=total[0, 1];

a2 = np.array([ [x2, y2, 1] ])
f2 = np.array([ [1, 0, dx], [0, 1, -dy], [0, 0, 1] ])
ft2=f2.T
total2 = a2.dot(ft2)
x22=total2[0, 0];  y22=total2[0, 1];

a3 = np.array([ [x3, y3, 1] ])
f3 = np.array([ [1, 0, dx], [0, 1, -dy], [0, 0, 1] ])
ft3=f3.T
total3 = a3.dot(ft3)
x33=total3[0, 0];  y33=total3[0, 1];

a4 = np.array([ [x4, y4, 1] ])
f4 = np.array([ [1, 0, dx], [0, 1, -dy], [0, 0, 1] ])
ft4=f4.T
total4 = a4.dot(ft4)
x44=total4[0, 0];  y44=total4[0, 1];
#*************** ПОВОРОТ *************************************************************
import math as mt
TetaG=45; TetaR=(3/14*TetaG)/180

ap = np.array([ [x11, y11, 1] ])
fp = np.array([ [mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1] ])
ftp=fp.T
totalp = ap.dot(ftp)
x11=totalp[0, 0];  y11=totalp[0, 1];

a2p = np.array([ [x22, y22, 1] ])
fp2 = np.array([ [mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1] ])
ft2p=fp2.T
total2p = a2p.dot(ft2p)
x22=total2p[0, 0];  y22=total2p[0, 1];

a3p = np.array([ [x33, y33, 1] ])
fp3 = np.array([ [mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1] ])
ft3p=fp3.T
total3p = a3p.dot(ft3p)
x33=total3p[0, 0];  y33=total3p[0, 1];

a4p = np.array([ [x44, y44, 1] ])
fp4 = np.array([ [mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1] ])
ft4p=fp4.T
total4p = a4p.dot(ft4p)
x44=total4p[0, 0];  y44=total4p[0, 1];

obj = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))
obj.draw(win)
obj.setOutline("white")
obj = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))
#obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))

stop=xw/dx*6;
stop = float(stop)
ii = int(stop)

obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))
obj.draw(win)
obj.setOutline("white")
obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))

#win.getMouse()
#**********************************************************************************

for i in range(ii):
    time.sleep(0.2)

    obj.setOutline("white")
    obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))

    # ---------------------циклічний блок матричних перетворень типу ПЕРЕНОС------------------
    a = np.array([[x11, y11, 1]])
    f = np.array([[1, 0, dx], [0, 1, -dy], [0, 0, 1]])
    ft = f.T
    total = a.dot(ft)
    x11 = total[0, 0];
    y11 = total[0, 1];

    a2 = np.array([[x22, y22, 1]])
    f2 = np.array([[1, 0, dx], [0, 1, -dy], [0, 0, 1]])
    ft2 = f2.T
    total2 = a2.dot(ft2)
    x22 = total2[0, 0];
    y22 = total2[0, 1];

    a3 = np.array([[x33, y33, 1]])
    f3 = np.array([[1, 0, dx], [0, 1, -dy], [0, 0, 1]])
    ft3 = f3.T
    total3 = a3.dot(ft3)
    x33 = total3[0, 0];
    y33 = total3[0, 1];

    a4 = np.array([[x44, y44, 1]])
    f4 = np.array([[1, 0, dx], [0, 1, -dy], [0, 0, 1]])
    ft4 = f4.T
    total4 = a4.dot(ft4)
    x44 = total4[0, 0];
    y44 = total4[0, 1];

#-------------------------------циклічний поворот на TetaR-------------------------------------------

    DTetaR = (3 / 14 * ((xw/dx)*0.65)) / 180
    TetaR=TetaR+DTetaR
    ap = np.array([[x11, y11, 1]])
    fp = np.array([[mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1]])
    ftp = fp.T
    totalp = ap.dot(ftp)
    x11 = totalp[0, 0];
    y11 = totalp[0, 1];

    a2p = np.array([[x22, y22, 1]])
    fp2 = np.array([[mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1]])
    ft2p = fp2.T
    total2p = a2p.dot(ft2p)
    x22 = total2p[0, 0];
    y22 = total2p[0, 1];

    a3p = np.array([[x33, y33, 1]])
    fp3 = np.array([[mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1]])
    ft3p = fp3.T
    total3p = a3p.dot(ft3p)
    x33 = total3p[0, 0];
    y33 = total3p[0, 1];

    a4p = np.array([[x44, y44, 1]])
    fp4 = np.array([[mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1]])
    ft4p = fp4.T
    total4p = a4p.dot(ft4p)
    x44 = total4p[0, 0];
    y44 = total4p[0, 1];

    obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))
    obj.draw(win)

    # --------------------циклічний блок скалярних перетворень типу ПЕРЕНОС--------------------

win.getMouse()
win.close()


#--------------Циклічний перенос типу "РУХ" та поворот матричними операціями-----------------
win = GraphWin("2-D проекции в библиотеке graphics ПЕРЕНОС обертання З РУХОМ матрицями", xw, yw)
win.setBackground('white')
dx = 50; dy = 50
x1=st; y1=yw-2*st;
x2=2*st; y2=yw-2*st;
x3=2*st; y3=yw-st;
x4=st; y4=yw-st;

#-------------------------блок матричних перетворень типу ПЕРЕНОС----------------------------
import numpy as np
a = np.array([ [x1, y1, 1] ])
f = np.array([ [1, 0, dx], [0, 1, -dy], [0, 0, 1] ])
ft=f.T
total = a.dot(ft)
x11=total[0, 0];  y11=total[0, 1];

a2 = np.array([ [x2, y2, 1] ])
f2 = np.array([ [1, 0, dx], [0, 1, -dy], [0, 0, 1] ])
ft2=f2.T
total2 = a2.dot(ft2)
x22=total2[0, 0];  y22=total2[0, 1];

a3 = np.array([ [x3, y3, 1] ])
f3 = np.array([ [1, 0, dx], [0, 1, -dy], [0, 0, 1] ])
ft3=f3.T
total3 = a3.dot(ft3)
x33=total3[0, 0];  y33=total3[0, 1];

a4 = np.array([ [x4, y4, 1] ])
f4 = np.array([ [1, 0, dx], [0, 1, -dy], [0, 0, 1] ])
ft4=f4.T
total4 = a4.dot(ft4)
x44=total4[0, 0];  y44=total4[0, 1];
#*************** ПОВОРОТ *************************************************************
import math as mt
TetaG=45; TetaR=(3/14*TetaG)/180

ap = np.array([ [x11, y11, 1] ])
fp = np.array([ [mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1] ])
ftp=fp.T
totalp = ap.dot(ftp)
x11=totalp[0, 0];  y11=totalp[0, 1];

a2p = np.array([ [x22, y22, 1] ])
fp2 = np.array([ [mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1] ])
ft2p=fp2.T
total2p = a2p.dot(ft2p)
x22=total2p[0, 0];  y22=total2p[0, 1];

a3p = np.array([ [x33, y33, 1] ])
fp3 = np.array([ [mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1] ])
ft3p=fp3.T
total3p = a3p.dot(ft3p)
x33=total3p[0, 0];  y33=total3p[0, 1];

a4p = np.array([ [x44, y44, 1] ])
fp4 = np.array([ [mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1] ])
ft4p=fp4.T
total4p = a4p.dot(ft4p)
x44=total4p[0, 0];  y44=total4p[0, 1];

obj = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))
obj.draw(win)
#obj.setOutline("white")
obj = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))
#obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))

stop=xw/dx*6;
stop = float(stop)
ii = int(stop)

obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))
obj.draw(win)
#obj.setOutline("white")
obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))

#win.getMouse()
#**********************************************************************************

for i in range(ii):
    time.sleep(0.2)

    #obj.setOutline("white")
    obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))

    # ---------------------циклічний блок матричних перетворень типу ПЕРЕНОС------------------
    a = np.array([[x11, y11, 1]])
    f = np.array([[1, 0, dx], [0, 1, -dy], [0, 0, 1]])
    ft = f.T
    total = a.dot(ft)
    x11 = total[0, 0];
    y11 = total[0, 1];

    a2 = np.array([[x22, y22, 1]])
    f2 = np.array([[1, 0, dx], [0, 1, -dy], [0, 0, 1]])
    ft2 = f2.T
    total2 = a2.dot(ft2)
    x22 = total2[0, 0];
    y22 = total2[0, 1];

    a3 = np.array([[x33, y33, 1]])
    f3 = np.array([[1, 0, dx], [0, 1, -dy], [0, 0, 1]])
    ft3 = f3.T
    total3 = a3.dot(ft3)
    x33 = total3[0, 0];
    y33 = total3[0, 1];

    a4 = np.array([[x44, y44, 1]])
    f4 = np.array([[1, 0, dx], [0, 1, -dy], [0, 0, 1]])
    ft4 = f4.T
    total4 = a4.dot(ft4)
    x44 = total4[0, 0];
    y44 = total4[0, 1];

#-------------------------------циклічний поворот на TetaR-------------------------------------------

    DTetaR = (3 / 14 * ((xw/dx)*0.65)) / 180
    TetaR=TetaR+DTetaR
    ap = np.array([[x11, y11, 1]])
    fp = np.array([[mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1]])
    ftp = fp.T
    totalp = ap.dot(ftp)
    x11 = totalp[0, 0];
    y11 = totalp[0, 1];

    a2p = np.array([[x22, y22, 1]])
    fp2 = np.array([[mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1]])
    ft2p = fp2.T
    total2p = a2p.dot(ft2p)
    x22 = total2p[0, 0];
    y22 = total2p[0, 1];

    a3p = np.array([[x33, y33, 1]])
    fp3 = np.array([[mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1]])
    ft3p = fp3.T
    total3p = a3p.dot(ft3p)
    x33 = total3p[0, 0];
    y33 = total3p[0, 1];

    a4p = np.array([[x44, y44, 1]])
    fp4 = np.array([[mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1]])
    ft4p = fp4.T
    total4p = a4p.dot(ft4p)
    x44 = total4p[0, 0];
    y44 = total4p[0, 1];

    obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))
    obj.draw(win)

    # --------------------циклічний блок скалярних перетворень типу ПЕРЕНОС--------------------

win.getMouse()
win.close()

