import os
import shutil
import random
from PIL import Image
from pathlib import Path


def preprocessing(image_folder, annotation_folder):
    
    ''' preprocess images , convert images into jpg format , delete if there are other extension
        except .jpg  . Creating new directory if not exists , if exists then delete . Split data 
        into train and test, check annotaions 


        args: 
        image_folder : path of image folder 
        annotaion_folder : path of annotaion folder 
     

     '''

    # Check if the image and annotation folders exist
    if not os.path.exists(image_folder):
        print(f"{image_folder} does not exist")
        return
    if not os.path.exists(annotation_folder):
        print(f"{annotation_folder} does not exist")
        return
    

    # Delete obj and test directories if they exist
    if os.path.exists("obj"):
        shutil.rmtree("obj")
    if os.path.exists("test"):
        shutil.rmtree("test")
    
    # Create obj and test directories
    os.makedirs("obj/images")
    os.makedirs("obj/labels")
    os.makedirs("test/images")
    os.makedirs("test/labels")

    # Initialize counters
    obj_images_count = 0
    obj_labels_count = 0
    test_images_count = 0
    test_labels_count = 0

    # Get a list of all image files in the image folder
    image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in image_files:
        # Check if the corresponding annotation file exists
        annotation_file = os.path.join(annotation_folder, os.path.splitext(os.path.basename(image_file))[0] + ".txt")
        if not os.path.exists(annotation_file):
            # Delete image file if annotation file does not exist
            os.remove(image_file)
            continue

        # Convert image to JPG format if necessary
        if not image_file.lower().endswith('.jpg'):
            with Image.open(image_file) as img:
               if img.mode != 'RGB':
                  img = img.convert('RGB')
               jpg_image_file = os.path.splitext(image_file)[0] + ".jpg"
               img.save(jpg_image_file)
            os.remove(image_file)
            image_file = jpg_image_file

        # Split into obj and test directories
        
        if random.random() < 0.12:
            shutil.copy(image_file, "test/images")
            shutil.copy(annotation_file, "test/labels")
            test_images_count += 1
            test_labels_count += 1
        else:
            shutil.copy(image_file, "obj/images")
            shutil.copy(annotation_file, "obj/labels")
            obj_images_count += 1
            obj_labels_count += 1

    # Print summary
    total_images_count = obj_images_count + test_images_count
    total_labels_count = obj_labels_count + test_labels_count
    print(f"Total images after preprocessing: {total_images_count}, Total labels: {total_labels_count}")
    print(f"obj images: {obj_images_count}, obj labels: {obj_labels_count}")
    print(f"test images: {test_images_count}, test labels: {test_labels_count}")







image_path = Path("images/")
annotation_path = Path("annotation/")

preprocessing(image_path,annotation_path)