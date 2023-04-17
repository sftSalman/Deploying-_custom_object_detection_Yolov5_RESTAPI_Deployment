![yolo5](https://user-images.githubusercontent.com/33355278/232350798-3ce7af8c-ab21-402d-beb5-8e931f9d9d4b.jpg)


# Cats and Dogs detection using yolov5 and deployment using REST API (Flask)
![Screenshot 2023-04-17 061324](https://user-images.githubusercontent.com/33355278/232351759-12253d57-61f0-4c2f-bd05-2450684bf371.png)
)



![Screenshot 2023-04-17 060830](https://user-images.githubusercontent.com/33355278/232352004-a08de8c9-57d0-4433-bcf7-b312b5452362.png)
![Screenshot 2023-04-17 060925](https://user-images.githubusercontent.com/33355278/232352007-d0cb8706-22fe-4e6f-be45-35fef1c06f35.png)
![Screenshot 2023-04-17 061512](https://user-images.githubusercontent.com/33355278/232352008-e08a9bba-e441-46b6-8abe-9b1d52d7315e.png)


# Installation


To get started with this project, follow the steps below:

1. Clone the repository to your local machine:


2. Create a virtual environment using `venv` module:
  `py -m venv myenv`

3. Activate the virtual environment:
  `myenv\Scripts\activate`

4. Install the project dependencies:
  `py -m pip install -r requirements.txt`

5. Start the application:
  `py myapp.py --port 5000`



# Dataset 
The given datasets has 103 images with different types of image extenson like .jpg , .svg, jpeg . So we need to preprocess data properly . We used a python function called `preprocess.py` which perform 
## Checking image format 
## Convert all types of images into .jpg format
## Create new directory 
-obj/images
-obj/labels
-test/images
-test/labels

## Split data 
-90 images for training 
-12 images for testing 
## Check annotation 

# Annotation : 
For annotatating I used "labelImg" (https://github.com/heartexlabs/labelImg)
