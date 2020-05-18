# Convolutional-Neural-Network
Summary of some CNN architectures and their applications

* In this post, I will sumarize some main categories about CNN and some CNN-based networks. Particularly, I will construct and compare the results trained by VGG16, VGG19, ResNet50 networks for Object Regconition problem so the original architecture of the CNN will be summarized shortly.

* **1. About Convolutional Neural Network**

Convolutional neural network (ConvNets or CNNs) is one of the main categories to do images recognition, images classifications. Objects detections, recognition faces etc., are some of the areas where CNNs are widely used.

CNNs are particularly useful for finding patterns in images to recognize objects, faces, and scenes. They learn directly from image data, using patterns to classify images and eliminating the need for manual feature extraction.

* **2. CNN's architecture**

a. Convolution Layers

Convolution Layer is the first layer to extract features from an input image. Convolution preserves the relationship between pixels by learning image features using small squares of input data. It is a mathematical operation that takes two inputs such as image matrix and a filter or kernel.

<p align = "center">
  <img src = "https://user-images.githubusercontent.com/51883796/82188939-d5981480-9918-11ea-9078-6a3a9272bdc6.png">
</p>

b. Pooling layers

It is common to periodically insert a Pooling layer in-between successive Conv layers in a ConvNet architecture. Its function is to progressively reduce the spatial size of the representation to reduce the amount of parameters and computation in the network, and hence to also control overfitting.

The Pooling Layer operates independently on every depth slice of the input and resizes it spatially, using the MAX operation. The most common form is a pooling layer with filters of size 2x2 applied with a stride of 2 downsamples every depth slice in the input by 2 along both width and height, discarding 75% of the activations.

<p align = "center">
  <img src = "https://user-images.githubusercontent.com/51883796/82189572-ce253b00-9919-11ea-8d27-b51c7f639bdd.jpeg">
</p>

c. Normalization layer

Many types of normalization layers have been proposed for use in ConvNet architectures, sometimes with the intentions of implementing inhibition schemes observed in the biological brain. However, these layers have since fallen out of favor because in practice their contribution has been shown to be minimal, if any. For various types of normalizations, see the discussion in Alex Krizhevsky’s cuda-convnet library API.

d. Fully connected layer

Neurons in a fully connected layer have full connections to all activations in the previous layer, as seen in regular Neural Networks. Their activations can hence be computed with a matrix multiplication followed by a bias offset. See the Neural Network section of the notes for more information.

<p align = "center">
  <img src = "https://user-images.githubusercontent.com/51883796/82190787-c6669600-991b-11ea-9d28-d6c50428d411.PNG">
</p>

* A CNN for image classification

<p align = "center">
  <img src = "https://user-images.githubusercontent.com/51883796/82191050-28270000-991c-11ea-913e-09113cdeb8cf.jpeg">
</p>

* **3. Case studies**

a. VGG16 and VGG19

The runner-up in ILSVRC 2014 was the network from Karen Simonyan and Andrew Zisserman that became known as the VGGNet. Its main contribution was in showing that the depth of the network is a critical component for good performance.
                                                                                              
Their final best network contains 16 CONV/FC layers and, appealingly, features an extremely homogeneous architecture that only performs 3x3 convolutions and 2x2 pooling from the beginning to the end. Their pretrained model is available for plug and play use in Caffe. A downside of the VGGNet is that it is more expensive to evaluate and uses a lot more memory and parameters (140M).

VGG16 and VGG19 are two most famous architectures of VGG net. The only difference of these two is VGG16 has 13 convolution layers and 3 fully connected layers, whereas VGG19 has 3 more convolution layers. 

The image bellow shows the architecture of VGG16:

<p align = "center">
  <img src = "https://user-images.githubusercontent.com/51883796/82195073-03358b80-9922-11ea-891e-f6d4e0114831.png">
</p>

