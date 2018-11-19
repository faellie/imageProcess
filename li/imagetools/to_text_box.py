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

def to_text_box(path):
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

    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        #get the original image which have the same file name in same dir but with .jpg
        originalImageFile = xml_file.replace('.xml', '.jpg')
        image = cv2.imread(originalImageFile)
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
            newImage = image[value[5]:value[7], value[4]:value[6], :]
            if(y2 - y1 < x2 - x1) :
                newImage  = imutils.rotate_bound(newImage, 90)
            print("writing to ", outputpath)
            #resize (width = 24 hight = 36)
            newImage = cv2.resize(newImage, (24, 36), cv2.INTER_AREA)
            #change to grey
            newImage = cv2.cvtColor(newImage,cv2.COLOR_BGR2GRAY)
            cv2.imwrite(outputpath, newImage)
    return


def main():
    #image_path = '/opt/TF/test/FullSet/eval'
    image_path = '/opt/TF/data/testfull'
    to_text_box(image_path)
    #xml_df.to_csv(image_path + '/train.csv', index=None)
    #xml_df.to_csv(image_path + '/eval.csv', index=None)
    print('Successfully converted xml to csv.')


main()
