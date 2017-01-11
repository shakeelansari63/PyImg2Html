import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import struct
import time


loc = raw_input("img location : ")
loc = '/Users/HID/Desktop/img-html/'+loc

img=mpimg.imread(loc)

f = open("output.html", 'w')
f.write("<html>\n")
f.write("<table cellspacing=\'0px\'>")

backc=""
count=0
color=[]

for i in img:
    f.write("<tr>\n")
    for j in i:
        for k in j:
            color.append(int(k*255))
        c='%02x%02x%02x' % (color[0], color[1], color[2])
        if backc == c or count == 0:
            count += 1
            backc = c
        elif backc != c:
            for a in range(0,count):
                data = "<td height='0.1' width='0.1' bgcolor='%s'></td>\n" % (backc)
                f.write(data)
            count = 1
            backc = c
        color=[]
    count-=1
    for i in range(0,count):
        data = "<td height='0.1' width='0.1' bgcolor='%s'></td>\n" % backc
        f.write(data)
    f.write("</tr>\n")
    count = 0
    backc = ""
f.write("</table>\n")
f.write("</html>")
f.close()
