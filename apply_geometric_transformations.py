"""
apply_geometric_transformations.py
This script reads and visualises an image that is specified by user using the Linux command line and applies geometric tranformations to this image.

Authors: Alberto Castro Villasana , Ana Bárbara Quintero, Héctor Camacho Zamora
Organisation: UDEM
First created on Friday 06 February 2024
"""

import cv2
import numpy as np
import argparse

def parse_user_data():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_image', type=str, required=True, help="Specified input image url or location")
    args = parser.parse_args()
    return args

def load_image(filename):
    img = cv2.imread(filename)
    if img is None:
        print(f"ERROR! - Image {filename} could not be read")
    return img

def apply_rotation(img):
    height, width = img.shape[:2]
    ang = 45
    #// divide y redondea
    center = (width // 2, height // 2)
    #Devuelve una matriz de transformacion 2x3
    rotation_mtx = cv2.getRotationMatrix2D(center, ang, 1.0)
    print(rotation_mtx)
    img_rotated = cv2.warpAffine(img, rotation_mtx, (width, height))

    return img_rotated

def apply_translation(img):
    M = np.float32([[1, 0, 50], [0, 1, 0]])  # Shift 50 pixels to the right
    img_translated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return img_translated

def apply_reflection(img):
    img_reflected = cv2.flip(img, 1)  # Flip horizontally
    return img_reflected

def visualise_image(img, title):
    width, height = 300, 300  # Por ejemplo, 200x200 píxeles para cada imagen
    
    # Redimensiona las imágenes
    img = cv2.resize(img, (width, height))

    cv2.imshow(title, img)
    cv2.waitKey(0)

def visualise_combined_image(images, titles, window_title="Combined Image"):
    # Decide el tamaño deseado para cada imagen
    width, height = 200, 200  # Por ejemplo, 200x200 píxeles para cada imagen
    
    # Redimensiona las imágenes
    resized_images = [cv2.resize(img, (width, height)) for img in images]
    
    # Combina las imágenes horizontalmente
    combined_image = np.hstack(resized_images)
    
    # Muestra la imagen combinada
    cv2.imshow(window_title, combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def close_windows():
    cv2.destroyAllWindows()

def run_pipeline():
    args = parse_user_data()
    img = load_image(args.input_image)

    img_rotated = apply_rotation(img)
    img_translated = apply_translation(img)
    img_reflected = apply_reflection(img)

    visualise_image(img, 'Input image')
    visualise_image(img_rotated, 'Rotated image')
    visualise_image(img_translated, 'Translated image')
    visualise_image(img_reflected, 'Reflected image')

    # Combina y visualiza las imágenes
    #images = [img, img_rotated, img_translated, img_reflected]
    #titles = ['Input image', 'Rotated image', 'Translated image', 'Reflected image']
    #visualise_combined_image(images, titles)

    close_windows()
    print('Program finished!\n')

if __name__ == "__main__":
    run_pipeline()


