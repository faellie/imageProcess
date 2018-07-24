import os, sys
import numpy as np
from scipy import misc
from scipy.misc import imread, imresize


import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', required=True)
    parser.add_argument('--out_dir', required=True)
    parser.add_argument('--width', default=640, type=int)
    parser.add_argument('--height', default=480, type=int)
    args = parser.parse_args()
    image_files = [os.path.join(args.image_dir, f) for f in os.listdir(args.image_dir) if os.path.isfile(os.path.join(args.image_dir, f))]
    size = args.width, args.height
    index = 1
    for image_file in image_files:
        orig_img = imread(image_file)
        #outfilename = '%s/%s' % (args.out_dir, os.path.basename(image_file))
        outfilename = '%s/out_%d.png' % (args.out_dir, index)
        if(orig_img.shape[0] > orig_img.shape[1]):
            img = imresize(np.rot90(orig_img), (args.height, args.width), interp='bilinear')
            misc.imsave(outfilename, img)
        else:
            img = imresize(orig_img, (args.height, args.width), interp='bilinear', mode='RGB')
            misc.imsave(outfilename, img)
        #
        # if(orig_img.shape[0] > orig_img.shape[1]):
        #     img = np.rot90(orig_img)
        #     misc.imsave(outfilename, img)
        # else :
        #     misc.imsave(outfilename, orig_img)
        index = index + 1



if __name__ == '__main__':
    main()
