def segment(image,list):
    count=1
    while(list):
        print('list is',list)
        start=list.pop(0)
        stop=list.pop(0)
        crop_img = image[0:rows,start:stop]
        title='cropped_'+str(count)+'.jpg'
        cv2.imwrite(title, crop_img)
        count+=1
    

segment(img,pts)
