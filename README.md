# Mobile_Price_Range_Prediction


we have a dataset which contains 21 features. This experiment can help us to understand which features have more impact on Price Range.
-----------------------------------------------------

📖 Random Forest Classification
Random forest classifier creates a set of decision trees from randomly selected subset of training set. It then aggregates the votes from different decision trees to decide the final class of the test object.Ensembled algorithms are those which combines more than one algorithms of same or different kind for classifying objects. For example, running prediction over Naive Bayes, SVM and Decision Tree and then taking vote for final consideration of class for test object.Basic parameters to Random Forest Classifier can be total number of trees to be generated and decision tree related parameters like minimum split, split criteria etc.




📖 XGboost
XGBoost stands for “Extreme Gradient Boosting”. XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements Machine Learning algorithms under the Gradient Boosting framework. It provides a parallel tree boosting to solve many data science problems in a fast and accurate way.


-----------------------------------------------------

📋 Execution Instruction
The order of execution of the program files is as follows:

1) app.ipynb

This file must be executed, to define all the functions and variables required for classification operations which leads to the production of the model.h5 file. and to evaluate the model performance on unseen data

2)Open Heroku link to predict Mobile Price Range

Flask app link : https://mobilepricerangeprediciton.herokuapp.com/

-----------------------------------------------------

Conclusion:

●From EDA we can see that here are mobile phones in 4 price ranges.
The number of elements is almost similar.

●Half the devices have Bluetooth, and half don’t

●there is a gradual increase in battery as the price range increases

●Ram has continuous increase with price range while moving from Low cost to Very high cost
costly phones are lighter

●RAM, battery power, pixels played more significant role in deciding the price range of mobile
phone.

●form all the above experiments we can conclude that Support vector machine and XGboosting
with using hyperparameterswe got the best results

●The accuracy and performance of the model is evaluated by using confusion matrix


