from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg19 import preprocess_input
from keras.applications.vgg19 import decode_predictions
from keras.applications.vgg19 import VGG19
import cv2

#load the model
model = VGG19()
#load image
image = load_img("d:/clock.jpg", target_size=(224,224))
#convert to gray scale
image = img_to_array(image)
#reshape
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
#Prepare input
image = preprocess_input(image)
#predict 
yhat = model.predict(image)
#convert probablility to class label
label = decode_predictions(yhat)
label = label[0][0]
#print the classification
print('%s (%.2f%%)' % (label[1], label[2] * 100))
#Print to image
org = cv2.imread("d:/clock.jpg")
cv2.putText(org, "Label: {}, {:.2f}%".format(label[1], label[2]*100),
	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv2.imshow("Classification", org)
cv2.waitKey(0)





