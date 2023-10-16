import cv2
import face_recognition
img=cv2.imread("1.jpg") #read the image
cv2.imshow("test",img) # print the image for testing
cv2.waitKey(2)

face_location=face_recognition.face_locations(img,model="hog") # detect face in the image
print("There are {} faces in this image".format(len(face_location)))

# looping through face locations to get its values
for index,current_face_location in enumerate(face_location):
    top,right,bottom,left=current_face_location
    print("Found face {} at top {},right {},bottom {},left {}".format(index+1,top,right,bottom,left))

