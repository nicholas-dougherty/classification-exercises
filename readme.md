***
```
          ____ _        _    ____ ____ ___ _____ ___ ____    _  _____ ___ ___  _   _ 
         / ___| |      / \  / ___/ ___|_ _|  ___|_ _/ ___|  / \|_   _|_ _/ _ \| \ | |
        | |   | |     / _ \ \___ \___ \| || |_   | | |     / _ \ | |  | | | | |  \| |
        | |___| |___ / ___ \ ___) |__) | ||  _|  | | |___ / ___ \| |  | | |_| | |\  |
         \____|_____/_/   \_\____/____/___|_|   |___\____/_/   \_\_| |___\___/|_| \_|
 ```
***                                                                              
                                                                                                  
The first machine learning concept covered in the curriculum is classification.     
This method can answer whether or not a new observation is A or B (maybe even C, D, or E). 
Classification is a __supervised learning task__. Which of course means it trains on data w/
answers/labels. This labeling is used to produce a _decision rule_ used to classify future data. 
***
## Main Ideas
- With classification, we use labeled data to train algorithms IOT classify future data points.
- The training data allows us to train an algorithm to produce a decision rule.
- Using a boundary between points or a distance between points, we classify new datapoints into A or B (or C or D or E)       

Classification is a technique for identifying an observation's class. Performed by modeling patterns in the related data which drive the outcome.        
         
The primary goal of developing a classification model is to generalize patterns. This is done so that the category/class of new data can be identified with a high degree of certaintly. Classification can be performed on structured or unstructured data. It can be used to predict binary classes (2 classes) or multi-classes (>2 classes).

#### Predicting Categorical Outcomes

In this repository, we will explore supervised machine learning related to classification using structured data. We will work through the data science pipeline, expanding our knowledge of these techniques, through each stage of the data science pipeline, as well as improving our knowledge of the python programming language.

***

## Vocabulary:

- Classifier: An algorithm which maps input data to a specific category.
- Classification Model: A series of steps that take the patterns of input variables, generalize them, and applies those generalizations to new data IOT predict the class.
- Feature: A feature (otherwise known as the input/independent variable), is an individually measurable property of observable phenomena.
- Binary Classification: Classification with two possible outcomes, e.g. pass/fail.
- Multiclass Classification: Classification with more than two classes, where each sample is assigned to one and only one target label, e.g. Grade levels of students in school (1st-12th).
***
### Common Classification Algorithms

- Logistic Regression | (sklearn.linear_model.LogisticRegression)
- Decision Tree | (sklearn.tree.DecisionTreeClassifier)
- Naive Bayes | (sklearn.naive_bayes.BernoulliNB)
- K-Nearest Neighbors | (sklearn.neighbors.KNeighborsClassifier)
- Random Forest | (sklearn.ensemble.RandomForestClassifier)
- Support Vector Machine | (sklearn.svm.SVC)
- Stochastic Gradient Descent | (sklearn.linear_model.SGDClassifier)
- AdaBoost | (sklearn.ensemble.AdaBoostClassifier)
- Bagging | (sklearn.ensemble.BaggingClassifier)
- Gradient Boosting | (sklearn.ensemble.GradientBoostingClassifier)
Peruse [Scikitlearn documentation](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning) on supervised methods for more information.
***
### Data Preparation Needs

1. Features need to be turned into numbers
2. Categorical features or discrete features will be numbers that represent those categories
3. Continuous features may need to be scaled so we're not comparing different units like dollars to cm to age.
***
#### General Concepts:

##### Logistic Regression

- Technically a regression algorithm 
    - (Goal is to find the values for the coefficients that weight each input variable).
- Used to predict binary outcomes.
- The output is a value between 0 and 1 that represents the probability of one class over the other.

##### Decision Tree (CART: Classification And Regression Trees)

- A sequence of rules used to classify 2 or more classes.
- Each node represents a single input variable (x) and a split point or class of that variable.
- The leaf nodes of the tree contain an output variable (y) which is used to make a prediction.
- Predictions are made by walking the splits of the tree until arriving at a leaf node and output the class value at that leaf node.

##### Random Forest

Random forest is an implementation of bootstrap aggregation, aka bagging, which is an ensemble algorithm.

Bootstrapping is a statistical method for estimating a quantity from a data sample, e.g. mean. You take lots of samples of your data, calculate the mean, then average all of your mean values to give you a better estimation of the true mean value. In bootstrap aggregation, or bagging, the same approach is used for estimating entire statistical models, such as decision trees. Multiple samples of your training data are taken and models are constructed for each sample set.

When you need to make a prediction for new data, each model makes a prediction and the predictions are averaged to give a better estimatation of the true output value.

Random forest is a tweak on this approach of bootstrapping, where decision trees are created so that rather than selecting optimal split points, suboptimal splits are made by introducing randomness. The models created for each sample of the data are therefore more different than they otherwise would be, in normal bootstrapping, but still accurate in their unique and different ways. This all combines their prediction results in a better estimate of the true underlying output value.

If you get good results with an algorithm with high variance (like decision trees), you can often get better results by bagging that algorithm, e.g. using a random forest.

##### K-Nearest Neighbor

K-Nearest Neighbor (KNN) makes predictions based on how close a new data point is to known data points.

It is considered "lazy" as it does not attempt to construct a general internal model, but simply stores instances of the training data. Classification is computed from a simple majority vote of the K nearest neighbours of each point.

Predictions are made for a new data point by searching through the entire training set for the K most similar instances (the neighbors) and summarizing the output variable for those K instances. For regression problems, this might be the mean output variable. For classification problems, this might be the mode (or most common) class value.

It is important to define a metric to measure the similarity between data instances. Euclidean distance can be used if attributes are all on the same scale (or you convert them to the same scale).

##### Support Vector Machine

A technique that uses higher dimensions to best seperate data points into two classes.

Support Vector Machines select hyperplane (a line that splits the input variable space) to best separate the points in the input variable space by their class, either class 0 or class 1. In two-dimensions, you can visualize this as a line.

An optimization algorithm is used to find the values for the coefficients that maximizes the margin. The distance between the hyperplane and the closest data points is referred to as the margin. The best or optimal hyperplane that can separate the two classes is the line that has the largest margin. Only these points, called the support vectors, are relevant in defining the hyperplane and in the construction of the classifier.

##### Naïve Bayes

Naive Bayes is based on Bayes’ theorem that assumes independence between every pair of features.

It is comprised of two types of probabilities that can be calculated directly from your training data:

The probability of each class
The conditional probability for each class given each x value
Once calculated, the probability model can be used to make predictions for new data using Bayes Theorem. When your data is real-valued it is common to assume a Gaussian distribution (bell curve) so that you can easily estimate these probabilities. (so normalize your data!)

It assumes that each input variable is independent (which is often not the case), thus it is called "naive". This is a strong assumption and unrealistic for real data, nevertheless, the technique is very effective on a large range of complex problems, including document classification and spam filtering.