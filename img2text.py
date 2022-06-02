import os
import platform
import argparse
import cv2
import win32api
import pytesseract
from re import split


if 'Windows' in platform.platform():
    user = os.getlogin()
    installed_dirs = [fp for fp in [os.path.join(d, p, 'Tesseract-OCR') for p in ['Program Files', 'Program Files (x86)', 'Windows\System32', 'Users\%s\AppData\Local' % user, 'Users\%s\AppData\Local\Programs' % user] 
                            for d in win32api.GetLogicalDriveStrings().split('\000')[:-1]] if os.path.exists(fp)]
    if len(installed_dirs) == 0:
        raise Exception('Failed to find installation of "Tesseract-OCR", download from: https://github.com/UB-Mannheim/tesseract/wiki')
    
    pytesseract.pytesseract.tesseract_cmd = os.path.join(installed_dirs[0], 'tesseract.exe')

def get_text(fullname):
    img = cv2.imread(fullname)
    text = pytesseract.image_to_string(img)
    return text

def img_to_text_file(filepath):
    fullname = path.abspath(filepath)
    outfile = path.join(path.dirname(fullname), '%s.txt' % path.splitext(fullname)[0])
    
    if path.isfile(fullname):
        print('img2txt: %s -> %s' % (fullname, outfile))
        text = get_text(fullname)
        with open(outfile, 'w') as o:
            o.write(text)
    else:
        print('Image doesn\'t exist %s' % fullname)

def main():
    parser = argparse.ArgumentParser(description='Converts an img to text.')
    parser.add_argument('images', nargs='+', type=str, help='path to image(s)')
    args = parser.parse_args()
    
    output = os.path.join(os.path.abspath('.'), 'image.txt')
    images = [os.path.normpath(os.path.abspath(fp)) for f in args.images for fp in split(r'\s*[;,]{1,}\s*', f)]
    if len(images) == 0:
        print('No valid images provided.')
    else:
        outfile = os.path.join(os.path.abspath('.'), 'image.txt')
        if os.path.exists(outfile):
            os.remove(outfile)
        
        with open(outfile, 'w') as output:
            for image in images:
                if not os.path.exists(image):
                    print('Image not found %s' % image)
                    continue
                
                text = get_text(image)
                output.writelines(['Image: ' + image])
                output.write(text + '\n')
                
                print('Writting %s -> %s' % (image, outfile))


if __name__ == '__main__':
    main()