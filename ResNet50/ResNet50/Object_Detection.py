from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import decode_predictions
from keras.applications.resnet50 import preprocess_input
import cv2

#load the model
model = ResNet50()

#load the image
image = load_img('d:/clock.jpg', target_size=(224,224))

#preprocess the image
image = img_to_array(image)
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
image = preprocess_input(image)

# predict the probability across all output classes
yhat = model.predict(image)
# convert the probabilities to class labels
label = decode_predictions(yhat)
# retrieve the most likely result, e.g. highest probability
label = label[0][0]
# print the classification
print('%s (%.2f%%)' % (label[1], label[2]*100))
org = cv2.imread("d:/clock.jpg")
#(imagenetID, label, prob) = P[0][0]
cv2.putText(org, "Label: {}, {:.2f}%".format(label[1], label[2]*100),
	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
cv2.imshow("Classification", org)
cv2.waitKey(0)
