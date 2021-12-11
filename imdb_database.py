import pandas as pd
data = pd.read_csv("new_upcoming_dvd_reviews.csv", index_col=0)
from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:postgres@localhost:5432/movie_review")
data.to_sql("IMDB_REVIEWS", engine, if_exists="append")
