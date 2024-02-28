"""
examen_practico.py
Este script es un código para el examen practico.

Autores:
Organización: UDEM
Fecha de creación: 23 de febrero de 2024
"""

import argparse
import cv2 
import sys 
import numpy as np

def user_interaction():
    var = argparse.ArgumentParser()
    var.add_argument('--input',type=str,required=True,help='Path image')
    var.add_argument('--output',type = str, required=True,help='output')
    args = var.parse_args()
    return args

def read_image(filename):
    img = cv2.imread(filename)
    if img is not None:
        return img
    elif img is None:
        sys.exit("Error when loading image")

def visualize_image(img, title):
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotate_180(img):
    img_rotated = cv2.rotate(img,cv2.ROTATE_180)
    return img_rotated

def traslate_image(img):
    rows,cols,_ = img.shape
    M = np.float32([[1,0,50],[0,1,0]])
    img_traslated = cv2.warpAffine(img,M,(cols,rows))
    return img_traslated

def pipeline():
    args = user_interaction()
    print(args.input)
    print(args.output)
    imagen = read_image(args.input)
    visualize_image(imagen, "Input image")
    imagen_rotada = rotate_180(imagen)
    
    imagen_trasladada = traslate_image(imagen)
    visualize_image(imagen_trasladada, "Traslated image")
    


if __name__ == '__main__':
    pipeline()