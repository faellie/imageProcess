from PIL import Image
import os, sys
import argparse
import numpy as np
from scipy import misc
from scipy.misc import imread, imresize

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', required=True)
    args = parser.parse_args()
    image_files = [os.path.join(args.image_dir, f) for f in os.listdir(args.image_dir) if os.path.isfile(os.path.join(args.image_dir, f))]
    for image_file in image_files:
        orig_img = imread(image_file)
        outfilename = image_file.replace('.jpg', '.png')
        misc.imsave(outfilename, orig_img)
        #im = Image.open('Foto.jpg')
        #im.save('Foto.png')



if __name__ == '__main__':
    main()
