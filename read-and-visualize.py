"""
read-and-visualize.py
This script reads and visualises an image that is specified by user using the Linux command line.

Author: Alberto Castro Villasana
Contact: josealberto.castro@udem.edu
Organisation: UDEM
First created on Friday 02 February 2024
"""

#Import libraries
import cv2
import argparse

def parse_user_data():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_image', type=str, required=True, help="Specified input image url or location")
    args = parser.parse_args()

    return args

def load_image(filename):

    img = cv2.imread(filename)

    if img is None:
        print("Error: Image not found")
        return None
    
    return img
    

def visualise_image(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def pipeline():
    
    args = parse_user_data()
    
    imagen = load_image(args.input_image)

    visualise_image(imagen)
    


if __name__ == "__main__":
    pipeline()

