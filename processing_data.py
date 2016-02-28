##list processing:
'''
vhist=[0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 3,
 6,
 8,
 10,
 12,
 14,
 16,
 16,
 15,
 14,
 13,
 11,
 11,
 10,
 9,
 9,
 9,
 10,
 12,
 21,
 26,
 28,
 32,
 42,
 47,
 47,
 48,
 47,
 47,
 48,
 46,
 44,
 29,
 28,
 26,
 23,
 21,
 18,
 14,
 7,
 0,
 0,
 0,
 7,
 16,
 23,
 28,
 32,
 37,
 39,
 38,
 38,
 29,
 24,
 19,
 14,
 11,
 8,
 8,
 8,
 8,
 0,
 0,
 0,
 0,
 0,
 27,
 34,
 39,
 42,
 45,
 48,
 50,
 52,
 29,
 20,
 15,
 11,
 8,
 5,
 2,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0]

#print(vhist)
assuming no segment is touching the border. we can always add a buffer/border to achieve this.

also assuming that each segment is more than 1 pixel wide, to ignore all corner cases..

## while comparing numpy data 'vhist[i] is 0' does not work 

'''

pts=[]
for i in range(len(vhist)-1):
    if vhist[i] == 0 and vhist[i+1] != 0:
        print('start found:',i+1)
        pts.append(i+1)
    elif vhist[i] != 0 and vhist[i+1] == 0:
        print('stop found',i)
        pts.append(i)
        
print(pts)        

'''
In [52]: pts
Out[52]: [11, 50, 54, 71, 77, 91]

'''


def drawlines(image,points,thick):
    for point in points:
        cv2.line(image,(point,0),(point,rows),(255,0,200),thick)
    cv2.imwrite('lined_image.jpg',image)

##rows,img is already defined
drawlines(img,pts,1)

        
