import cv2
import face_recognition

# read image
img=cv2.imread("1.jpg") #read the image
cv2.imshow("test",img) # print the image for testing
cv2.waitKey(2)

# detect face in the image #hog - low end #cnn - highend
face_location=face_recognition.face_locations(img,model="hog")
print("There are {} faces in this image".format(len(face_location)))
# CNN for Highend
# face_location=face_recognition.face_locations(img,model="cnn")
# print("There are {} faces in this image".format(len(face_location)))


# looping through face locations to get its values
for index,current_face_location in enumerate(face_location):
    top,right,bottom,left=current_face_location
    print("Found face {} at top {},right {},bottom {},left {}".format(index+1,top,right,bottom,left))

# slice image
current_face_image= img[top:bottom,left:right]
cv2.imshow("Face no"+str(index+1),current_face_image)
cv2.waitKey(0)

