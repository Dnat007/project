## Explain Image preprocessing steps:
1. first just load the image
2. Try to make the images size should be fixed (image size is of 128 X 128)
3. Image should be converted into 1-D array(Flatten the image)
4. Then convert the image into array and store it into X 
6. Apply Random forest technique into that to get the good result 
9. __Evaluation metrics used__ : accuracy is used here
8. create the model 

## Flask setup 
1. Load the model using joblib 
2. Then load the image do the same preprocess steps
3. reshape the image as (from -1 to 1)
4. Try to predict the model 

- Over here since its a image classification task it would be very good if we have used the CNN approach over here 
- by using ML we have only __70%__ accuracy
- We can enhance the model performance by using hyperparameter tunning but since i dont have a very high configuration laptop it would took more than 900 mins then the system crahsed so i unable to use that hyper parameter tunning
<br>
#  to run this completly you need to have the data folder inside your notebook folder inside the data there is a folder dataset_full and inside that you got the images
# data set is quite large cant able to add it over here we can add it here by using LFS but i can provide you the dataset link -- https://drive.google.com/file/d/1lWgKokYUrD5PPMO3tCy-yMN2ytaSnjTV/view?usp=sharing