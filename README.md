## IMDB Review Sentiment Classification


![Title Image](Resources/imdb_logo.png)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Contents

* [Dataset](#dataset-header)
* [Project Outline](#project-header)
* [Presentation](#presentation-header)
* [Logistic Regression](#lr-header)
* [Random Forest Model](#rf-header)
* [Naive Bayes Model](#nb-header)
* [SVM Model](#svm-header)
* [Collaborators](#team-header)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## <a id="dataset-header"></a>Dataset

For our project we have explored the [IMDB Review Dataset]( https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)\
Available from [Kaggle.com](https://www.kaggle.com). 
The dataset provides 25,000  movie reviews for training and 25,000 for testing. 
* Our project aims to predict whether a review is positive or negative using the natural language processing model.
* First we will apply some pre-processing and carry out some initial data exploration, and determine the ratios of positive and negative reviews using jupyter notebook. 
* We will import the data to an SQL database (if we have time we will get our own data from imdb using scrape
* We will use Pyspark to create a natural language processing model,, apply tokenizer and remove stop words.
* We will train the model on the kaggle dataset, then apply the data we have scraped.

We have used 2 CSV files in this data set: 

* IMDB Dataset
* new_upcoming_dvd_reviews.csv

CSV files are placed in the Resources folder.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------



## <a id="project-header"></a>Project Outline
We will be …

The dataset from Kaggle consists of one csv file. The second csv file is from the scraped data from the IMDB website. It contains three colums which is the movie title, url and review. When making predictions on the best model we dropped the title and url columns. 

[<img src="https://wiki.postgresql.org/images/a/a4/PostgreSQL_logo.3colors.svg" align="right"  width="100">](https://www.postgresql.org/)
  
The database will be created using PostgreSQL. 



<a href="https://plotly.com/javascript/"><img src="https://images.plot.ly/logo/plotlyjs-logo@2x.png" align="right" height="50"></a>



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## <a id="presentation-header"></a>Presentation

The project presentation can be found in the [/Presentation](Presentation/) directory:

* imdb_report.pdf

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## <a id="lr-header"></a>Logistic Regression 


## <a id="rf-header"></a>Random Forest Model


## <a id="nb-header"></a>Naive Bayes Model



## <a id="svm-header"></a>SVM Model



----------------------------------------------------------------------------------------------------------------------------

## <a id="team-header"></a>Collaborators

* [Isha Singh](https://github.com/isha167)
* [Jesse Edwards](https://github.com/Squonk713)
* [Jessica Uppal](https://github.com/JessicaUppal)



