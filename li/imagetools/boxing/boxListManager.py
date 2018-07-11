import os
import sys
import json
import li.imagetools.boxing.boxList

class BoxListManager:
    'list of boxes for all images'
    theList = [];
    current_image = ""
    'expect a BoxList'

    def add(self, boxes):
        boxlist = li.imagetools.boxing.boxList.BoxList(BoxListManager.current_image, boxes)
        li.imagetools.boxing.boxListManager.BoxListManager.theList.append(boxlist);
        BoxListManager.current_image="";

    @staticmethod
    def get( image_path):
        for entry in BoxListManager.theList :
            if(entry.image_path == image_path):
                return entry.rects;

    @staticmethod
    def update(boxes):
        rects = BoxListManager.get(BoxListManager.current_image);
        if rects != None :
            rects.add();

    @staticmethod
    def setCurrentImage(image_file):
        BoxListManager.current_image=image_file;

    @staticmethod
    def getCurrentImage(image_file):
        return BoxListManager.current_image;

    @staticmethod
    def clear():
        for entry in BoxListManager.theList:
            if entry.image_path == BoxListManager.current_image:
                entry.rects = [];

    @staticmethod
    def savetofile(cls, filename):
        with open(filename, 'w') as outfile:
            json.dump(BoxListManager.theList, outfile)

    def toStr(self):
        for entry in li.imagetools.boxing.boxListManager.BoxListManager.theList:
            print json.dumps(vars(entry),sort_keys=True, indent=4)


