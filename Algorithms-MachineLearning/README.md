
https://blog.devcenter.co/developing-a-license-plate-recognition-system-with-machine-learning-in-python-787833569ccd

Using the blog above to learn the concepts of:

Plate Localisation:

  -Convert image to binary.
  
  -Isolate Plate in the picture.  
  
  
Connected Componant Analysis (CCA):

  -A pixel is connected to another if they have the same value and adjacent to eachother.
  
  -Draw rectangle over all mapped regions.
  
  This produces many other connected regions including the plate itself.
  
  Typical licence plate characteristics need to be applied now.
  
  
Connected Componant Analysis 2 :

  -Rectangular in shape, width>height, 
  
  -Plate's width proportion to full image ranges between 15 and 40%
  
  -Plate's height proportion to full image ranges between 8 and 20%
  
 
Character Segmentation:

  -Map out and resize characters for recognition step to follow.
  
Character Recognition
  
Machine Learning:

  -Uses supervised learning which uses a known (training) dataset to predict.
 
 
Various packages are needed including:

  scikit-learn   For machine learning.
  
  scikit-image   Contains scipy(complicated calculations), 
  
  numpy(array manipulations), 
                  
  matplotlib(disp images,plot graphs),
                  
  pillow(imaging lib)
