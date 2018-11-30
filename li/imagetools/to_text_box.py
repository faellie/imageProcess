#Try get cut text images from the bounding box and put in a new image file.
#also change image to grey scale as color do nothing in our cases

import os
import errno
import glob
#import pandas as pd
import xml.etree.ElementTree as ET
import cv2
import imutils

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def to_text_box(path, include_bg=False):
    #make dirs first or imwrite will not work
    make_sure_path_exists(os.path.join(path, 'out', 'marker'))
    make_sure_path_exists(os.path.join(path, 'out', 'zero'))
    make_sure_path_exists(os.path.join(path, 'out', 'one'))
    make_sure_path_exists(os.path.join(path, 'out', 'two'))
    make_sure_path_exists(os.path.join(path, 'out', 'three'))
    make_sure_path_exists(os.path.join(path, 'out', 'four'))
    make_sure_path_exists(os.path.join(path, 'out', 'five'))
    make_sure_path_exists(os.path.join(path, 'out', 'six'))
    make_sure_path_exists(os.path.join(path, 'out', 'seven'))
    make_sure_path_exists(os.path.join(path, 'out', 'eight'))
    make_sure_path_exists(os.path.join(path, 'out', 'nine'))
    make_sure_path_exists(os.path.join(path, 'out', 'bg'))

    #dic to hold index for each classes
    indexes = {}
    indexes['marker'] = 0
    indexes['zero'] = 0
    indexes['one'] = 0
    indexes['two'] = 0
    indexes['three'] = 0
    indexes['four'] = 0
    indexes['five'] = 0
    indexes['six'] = 0
    indexes['seven'] = 0
    indexes['eight'] = 0
    indexes['nine'] = 0
    indexes['bg'] = 0  #i.e. background not any number

    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        #get the original image which have the same file name in same dir but with .jpg
        originalImageFile = xml_file.replace('.xml', '.jpg')
        image = cv2.imread(originalImageFile)
        imgheight, imgwidth  = image.shape[:2]

        #these mark the boundary of the all the numbers
        x_start = 0
        y_start = 0
        x_end = 0
        y_end = 0
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            # value[3] is the class
            indexes[value[3]] = indexes[value[3]] + 1;
            outputpath=os.path.join(path, 'out', value[3], str(indexes[value[3]]) + '.jpg')
            y1 = value[5]
            y2 = value[7]
            x1 = value[4]
            x2 = value[6]

            #update the boundary
            x_start = min(x1, x_start)
            y_start = min(y1, y_start)
            x_end = max(x2, x_end)
            y_end = max(y2, y_end)


            #newImage = image[value[5]:value[7], value[4]:value[6], :]
            newImage = image[y1:y2, x1:x2, :]
            if(y2 - y1 < x2 - x1) :
                newImage  = imutils.rotate_bound(newImage, 90)
            print("writing to ", outputpath)
            #resize (width = 24 hight = 36)
            newImage = cv2.resize(newImage, (24, 36), cv2.INTER_AREA)
            #change to grey
            newImage = cv2.cvtColor(newImage,cv2.COLOR_BGR2GRAY)
            cv2.imwrite(outputpath, newImage)

            #create some background boxes
            #shift by 4 in each direction
            #do this only if it not marker
            shift = 4
            if value[3]!='marker':
                if y1-shift > 0:
                    bg1 =  image[y1-shift:y2-shift, x1:x2, :]
                    if(y2 - y1 < x2 - x1) :
                        bg1  = imutils.rotate_bound(bg1, 90)
                    indexes['bg'] = indexes['bg'] + 1;
                    outputpath=os.path.join(path, 'out', 'bg', str(indexes['bg']) + '.jpg')
                    #resize (width = 24 hight = 36)
                    bg1 = cv2.resize(bg1, (24, 36), cv2.INTER_AREA)
                    #change to grey
                    bg1 = cv2.cvtColor(bg1,cv2.COLOR_BGR2GRAY)
                    cv2.imwrite(outputpath, bg1)
                if y2 + shift < imgheight:
                    bg2 =  image[y1 + shift:y2+ shift, x1:x2, :]
                    if(y2 - y1 < x2 - x1) :
                        bg2  = imutils.rotate_bound(bg2, 90)
                    indexes['bg'] = indexes['bg'] + 1;
                    outputpath=os.path.join(path, 'out', 'bg', str(indexes['bg']) + '.jpg')
                    #resize (width = 24 hight = 36)
                    bg2 = cv2.resize(bg2, (24, 36), cv2.INTER_AREA)
                    #change to grey
                    bg2 = cv2.cvtColor(bg2,cv2.COLOR_BGR2GRAY)
                    cv2.imwrite(outputpath, bg2)
                if x1-shift> 0:
                    bg3 =  image[y1:y2, x1-shift:x2-shift, :]
                    if(y2 - y1 < x2 - x1) :
                        bg3  = imutils.rotate_bound(bg3, 90)
                    indexes['bg'] = indexes['bg'] + 1;
                    outputpath=os.path.join(path, 'out', 'bg', str(indexes['bg']) + '.jpg')
                    #resize (width = 24 hight = 36)
                    bg3 = cv2.resize(bg3, (24, 36), cv2.INTER_AREA)
                    #change to grey
                    bg3 = cv2.cvtColor(bg3,cv2.COLOR_BGR2GRAY)
                    cv2.imwrite(outputpath, bg3)
                if x2+shift < imgwidth:
                    bg4 =  image[y1:y2, x1+shift:x2+shift, :]
                    if(y2 - y1 < x2 - x1) :
                        bg4  = imutils.rotate_bound(bg4, 90)
                    indexes['bg'] = indexes['bg'] + 1;
                    outputpath=os.path.join(path, 'out', 'bg', str(indexes['bg']) + '.jpg')
                    #resize (width = 24 hight = 36)
                    bg4 = cv2.resize(bg4, (24, 36), cv2.INTER_AREA)
                    #change to grey
                    bg4 = cv2.cvtColor(bg4,cv2.COLOR_BGR2GRAY)
                    cv2.imwrite(outputpath, bg4)


        #now add 5X5 BG box from outside the boundary from the full image
        count = 0
        while count < 25:
            #select a random point
            from random import randint
            rx1 = randint(shift , imgwidth - 22)
            ry1 = randint(shift, imgwidth - 32)
            if((rx1 < x_start - shift or rx1 > x_end + shift or y1 < y_start -shift or y1 > y_end + shift ) and rx1 < imgwidth -22 and ry1 < imgheight - 32):
                rx2 = rx1 + 22
                ry2 = ry1 + 32
                bg =  image[ry1:ry2, rx1:rx2, :]
                if(ry2 - ry1 < rx2 - rx1) :
                    bg  = imutils.rotate_bound(bg, 90)

                indexes['bg'] = indexes['bg'] + 1;
                outputpath=os.path.join(path, 'out', 'bg', str(indexes['bg']) + '.jpg')
                #resize (width = 24 hight = 36)
                bg = cv2.resize(bg, (24, 36), cv2.INTER_AREA)
                #change to grey
                bg = cv2.cvtColor(bg,cv2.COLOR_BGR2GRAY)
                cv2.imwrite(outputpath, bg)
                count += 1


    return


def main():
    #image_path = '/opt/TF/test/FullSet/eval'
    image_path = '/opt/TF/data/testfull'
    #image_path = '/opt/TF/data/test'
    to_text_box(image_path)
    #xml_df.to_csv(image_path + '/train.csv', index=None)
    #xml_df.to_csv(image_path + '/eval.csv', index=None)
    print('done!!')


main()
