Chosen topic : Machine Learning to predict quality of white wine.

1. Data   From UCI : get dataset on white wine in csv format.

2. Examine dataset and find what characteristics make a wine "tasty" by trying to find correlations
   or relationships between various wine characteristics and its taste value. Do this using Tableau.

3. Choose the most suitable characteristics and Load into AWS S3 bucket (finalprojectadwwhitewine)

3. Using Google Colab notebook read data from S3 bucket  https://finalprojectadwwhitewine.s3.ap-south-1.amazonaws.com/winequality-white.csv

---------From Machine Learning Homework on exoplanets-----------------------------

4. Perform data cleansing and transformation into Pandas dataframe ie remove null columns and rows.

5. Select columns for training and testing and column for prediction i.e. quality or tastiness
   Values for numeric. Set labels for various values ie good, fair, ok, drinkable, poor.

6. Create a Train Test split using sklearn

7. Scale the data using MinMaxScaler

8. Select a classifier model

9. Train the model and determine the training and testing data score.

10. Use Hyperparameter Tuning - GridSearch to tune the models parameters.

11. Train the model with GridSearch 

12.  Print out :
	precision    recall  f1-score   support

--------------------------------------------------------------------------------
13. Create webpage : Write up and Tableau visualisations.

14. Deploy web page using Heroku or or means.
