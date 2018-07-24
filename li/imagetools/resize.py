from PIL import Image
import os, sys
import argparse
import numpy as np
from scipy import misc
from scipy.misc import imread, imresize
import json
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', required=True)
    args = parser.parse_args()
    image_files = [os.path.join(args.image_dir, f) for f in os.listdir(args.image_dir) if os.path.isfile(os.path.join(args.image_dir, f))]
    for image_file in image_files:
        if(image_file.endswith('png')) :
            orig_img = imread(image_file)
            img = imresize(orig_img, (480, 640), interp='bilinear', mode='RGB')
            misc.imsave(image_file, img)
    with open(os.path.join(args.image_dir, 'out.json')) as f:
        listData = json.load(f)
    for entry in listData :
        rects = entry['rects']
        imagepath = entry['image_path']
        newPath = os.path.join(args.image_dir, os.path.basename(imagepath))
        entry['image_path'] = newPath
        for rect in rects :
            rect['y1'] = rect['y1']*480.0/1536.0;
            rect['y2'] = rect['y2']*480.0/1536.0;
            rect['x1'] = rect['x1']*640.0/2040.0;
            rect['x2'] = rect['x2']*640.0/2040.0;

    #write back to file
    with open(os.path.join(args.image_dir, 'out1.json'), 'w') as fout:
        json.dump(listData, fout, sort_keys=True, indent=4)
if __name__ == '__main__':
    main()
