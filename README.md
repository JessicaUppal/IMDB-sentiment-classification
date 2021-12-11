## IMDB Review Sentiment Classification


![imdb_logo](imdb_logo.png)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Contents

* [Dataset and Project Outline](#dataset-header)
* [Setup](#setup-header)
* [Presentation](#presentation-header)
* [Project Report](#report-header)
* [IMDB scraping](#scraping-header)
* [PostgreSQL connection](#postgres-header)
* [NLP Pipeline](#pipeline-header)
* [Logistic Regression](#lr-header)
* [Random Forest Model](#rf-header)
* [Naive Bayes Model](#nb-header)
* [SVM Model](#svm-header)
* [Collaborators](#team-header)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## <a id="dataset-header"></a>Dataset and Project Outline

For our project we’ve used sentiment analysis to classify reviews scraped of the IMDB website as either positive or negative using sentiment classification. 

For our project we have explored the [IMDB Review Dataset]( https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)\
Available from [Kaggle.com](https://www.kaggle.com). 
The dataset provides 50k reviews, where 25,000 are postive reviews and 25,000 are negative.
* Our project uses NLP sentiment analysis to classify whether unlabelled reviews are positive or negative.
* First we will apply some pre-processing and carry out some initial data exploration, and determine the ratios of positive and negative reviews using jupyter notebook. 
* We will import scraped imdb reviews data to an SQL database
* We will use Pyspark to create a natural language processing model, apply tokenizer and remove stop words.
* We will train the model on the kaggle dataset, then apply the unlabelled data we have scraped, to test whether the model is accurate.

We have used 2 CSV files in this data set: 

* IMDB Dataset.csv
* new_upcoming_dvd_reviews.csv

CSV files are placed in the Resources folder.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## <a id="setup-header"></a>Setup

* For the project we used google collab in order to run PySpark, which hasn't been installed in our local machines
* [<img src="https://miro.medium.com/max/800/1*nPcdyVwgcuEZiEZiRqApug.jpeg" align="right"  width="180">](https://spark.apache.org/docs/latest/api/python/)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## <a id="presentation-header"></a>Presentation

The project presentation can be found in the [/Presentation](Presentation/) directory:

* imdb.pdf

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## <a id="report-header"></a>Project Report

The project report can be found in the the main repository directory:

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## <a id="scraping"></a>IMDB Scraping

* Splinter and Beautiful Soup have been used to scrape reviews for the latest movie releases and append to our SQL database. We extracted the title of the movie, the URL and the review from the scraped html.

* Two URL variables are defined to bookend each side of the scraped URL for each specific release, this will give us the full URL for the required page.
* The FOR LOOP constructs the URL and navigates into that page to scrape the review.
* Film title, URL, and review are added to a dictionary, and then appended to the film reviews list.
* Film reviews list is transformed to Pandas DataFrame and then exported to CSV, called new_upcoming_dvd_reviews.csv



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## <a id="postgres"></a>PostgreSQL connection
[<img src="https://wiki.postgresql.org/images/a/a4/PostgreSQL_logo.3colors.svg" align="right"  width="100">](https://www.postgresql.org/)
  
The database will be created using PostgreSQL. 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## <a id="pipeline"></a>NLP Pipeline

* We followed a basic pipeline of tokenization of the review, which split the sentence into individual words. 
* The stop words that didn’t hold any sentimental value were removed. 
* In future it may also be useful to remove punctuation, and use .lower() function to reduce repetition of words. 
* Hashing TF was used to map individual words to an index. 
* A disadvantage of using HashingTF is that two different words could get mapped to the same index, and if this was a crucial word to our sentiment analysis such as “good” and “bad” this could decrease the accuracy of the model. 
* The output column contains either a 0 or 1 where 0 is a positive review and 1 is a negative review
* The data was split randomly into training and testing as a 70/ 30 split, in order to evaluate the performance of our machine learning models. 
* More data was needed in the training data set to give a better accuracy calculated on the test set.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## <a id="lr-header"></a>Logistic Regression 

* For the first model, we used to train our model was logistic regression
* This model achieved an accuracy of 0.860, making it the second highest accuracy out of the four models used.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## <a id="rf-header"></a>Random Forest Model

* The second model we used was the random forest model.
* Out of the four models we achieved the lowest accuracy score of 0.685.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## <a id="nb-header"></a>Naive Bayes Model

* This model achieved an accuracy of 0.844
* The Naive Bayes model assumes that all predictors are independent where one feature in a class doesn’t affect the presence of another one, however in our dataset the reviews were dependant. 
* Although the predictors weren’t completely independent in our case the model still produced a high accuracy rate.
* The high accuracy rate may be accounted to Naïve Bayes model being highly accurate after applying techniques like Stop Word removal, and TF-IDF.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## <a id="svm-header"></a>SVM Model

* We used the SVM model which allows for more accurate machine learning because it’s multidimensional. 
* The SVM model achieved the highest accuracy out of the four models0.877)
* This model works well with a clear margin of separation between classes, which in our data was positive and negative.


----------------------------------------------------------------------------------------------------------------------------

## <a id="team-header"></a>Collaborators

* [Isha Singh](https://github.com/isha167)
* [Jesse Edwards](https://github.com/Squonk713)
* [Jessica Uppal](https://github.com/JessicaUppal)



