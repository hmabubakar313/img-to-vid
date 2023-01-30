import os
import cv2 
from PIL import Image 
  
# Checking the current directory path
print(os.getcwd()) 
  
# Folder which contains all the images
# load images from the folder in Json format
image_list = [
    {"image": "/home/bakar/Desktop/vid/img/image1.jpeg", "width": 640, "height": 480},
    {"image": "/home/bakar/Desktop/vid/img/image2.jpg", "width": 800, "height": 600},
    {"image": "/home/bakar/Desktop/vid/img/image3.jpeg", "width": 720, "height": 540},
    {"image": "/home/bakar/Desktop/vid/img/image4.jpeg", "width": 640, "height": 480},
]
mean_height = 0
mean_width = 0

# Folder which contains all the images
# from which video is to be generated

for file in image_list:
    im = Image.open(file['image'])
    width, height = im.size
    print('Original Dimensions : ',width, height, end = ' ')

# select smallest width and height from the images
for image in image_list:
    mean_width += image['width']
    mean_height += image['height']
    # get minimum width 
    if min(image_list, key = lambda x: x['width']) == image:
        mean_width = image['width']
    # get minimum height
    if min(image_list, key = lambda x: x['height']) == image:
        mean_height = image['height']
        print('Resized Dimensions : ', mean_width, mean_height, end = ' ')
        

for file in image_list:
    # if file is jpg or jpeg or png
    if file['image'].endswith(('.jpg', '.jpeg', '.png')):
        # opening image using PIL Image
        im = Image.open(file['image'])
        # im.size includes the height and width of image
        width, height = im.size
        print('Original Dimensions : ',width, height, end = ' ')
        # resizing
        imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
        imResize.save(file['image'], 'JPEG', quality=95)
        print(im.filename.split('\\')[-1], " is resized") 
    
    
def generate_video():
    # get all the images from image_list
    load_images = [cv2.imread(file['image']) for file in image_list]
    video_name = 'video.avi'
    
    images = [img for img in load_images]
    # if images are in jpg or jpeg or png format
    if image_list[0]['image'].endswith(('.jpg', '.jpeg', '.png')):
        frame = cv2.imread(image_list[0]['image'])
        height, width, layers = frame.shape
        # video is generated
        video = cv2.VideoWriter(video_name, 0, 1, (width, height))
        # Appending the images to the video one by one
        for image in images:
            video.write(image)
        # Deallocating memories taken for window creation
        cv2.destroyAllWindows()
        video.release()
    

generate_video()
    