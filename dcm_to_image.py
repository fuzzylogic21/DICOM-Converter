import pydicom as dicom
import os
import cv2
import PIL
import sys
import matplotlib.pyplot as plt


# make it True if you want in PNG format
PNGorJPEG = sys.argv[1] #PNG or JPEG
print("converting dicom images to ", PNGorJPEG)
# Specify the .dcm folder path
input_folder_path = sys.argv[2] #Input path
print("Reading dicom images from ",input_folder_path)
# Specify the output jpg/png folder path
output_folder_path = sys.argv[3] #output path
print("Writing images to ", output_folder_path)

images_path = os.listdir(input_folder_path)
for n, image in enumerate(images_path):
    if image.endswith('.dcm'):
        print("Image Name : ", image)
        ds = dicom.dcmread(os.path.join(input_folder_path, image))
        pixel_array_numpy = ds.pixel_array
        if PNGorJPEG == "JPG":
            image = image.replace('.dcm', '.jpg')
            #image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
            print("Image format : ",sys.argv[1])
            #plt.imshow( image)
            #plt.show()
        else:
            image = image.replace('.dcm', '.png')
        cv2.imwrite(os.path.join(output_folder_path, image), pixel_array_numpy)
        print("Image Path : " ,output_folder_path)
        print("Image Path : " ,image)
        if n % 50 == 0:
            print('{} image converted'.format(n))
