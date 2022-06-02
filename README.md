# img2text

Python script for converting images to text.


## Installation

- Install python packages `python -m pip install -r requirements.txt`
- Alternatively install python packages
  - cv2 `pip install opencv-python`
  - win32api `pip install pywin32`
  - pytesseract `pip install pytesseract`
- Install the **tesseract** binary
  - **Linux**: `sudo apt-get install tesseract-ocr libtesseract-dev`
  - **Windows**: [Tesseract installer for Windows](https://github.com/UB-Mannheim/tesseract/wiki#tesseract-installer-for-windows)


## How to use

1. Change to the project directory
```shell
root@hostname:[/]$ cd img2text/
```

2. Run the python script with relative or absolute path to an image.
```shell
root@hostname:[img2text/] $ python img2text.py ./samples/image-1.png
Writting text ./samples/image-1.png -> ./output.txt
```

3. Allows for multiple files in sequence.
```shell
root@hostname:[img2text/] $ 
root@hostname:[img2text/] $ python img2text.py ./samples/image-1.png ./samples/image-2.png ./samples/image-3.png ./samples/image-4.png
Writting text ./samples/image-1.png -> ./output.txt
Writting text ./samples/image-2.png -> ./output.txt
Writting text ./samples/image-3.png -> ./output.txt
Writting text ./samples/image-4.png -> ./output.txt
root@hostname:[img2text/] $ 
```

4. Currently all contents will be dumped into an `output.txt` within your current running directory.
```shell
root@hostname:[img2text/] $ 
root@hostname:[img2text/] $ cat ./output.txt
Hello World!
root@hostname:[img2text/] $ 
```