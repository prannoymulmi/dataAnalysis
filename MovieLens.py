import pandas as pd;
from pandas import DataFrame;


path_user = 'D:\python\pydata-book\ch02\movielens\users.dat'
unames = ['user_id', 'gender', 'age', 'occupation id', 'zip'];

path_ratings = 'D:\python\pydata-book\ch02\movielens\\ratings.dat'
rnames = ['user_id', 'movie_id', 'rating','timestamp'];

path_movies = 'D:\python\pydata-book\ch02\movielens\movies.dat'
mnames = ['movie_id', 'title', 'genre']

user_names = pd.read_table(path_user, sep='::', names=unames, engine='python');

movie_names = pd.read_table(path_movies, sep='::', names=mnames, engine='python');

rating_names = pd.read_table(path_ratings, sep='::', names=rnames, engine='python');
# print rating_names[:10];
data = pd.merge(pd.merge(user_names, rating_names), movie_names);
# print movie_names[:5];

#grouping the data by title and getting the std of the ratings
print data.groupby('title')['rating'].std().sort_values()[100:200];

#getting the mean of the data by ratings and making a pivot table
mean_rating_by_gender = pd.pivot_table(data, aggfunc="mean", columns="gender", values='rating', index=["title"])
# print mean_rating_by_gender;

##########################

# Note : A Single column is a series in pandas and a data frame is a collection of series how a 2d array is a collections of lists


###########################


#grouping the data by title and getting the total number of occurances of a single title in the data
ratings_by_title = data.groupby('title').size();
# print ratings_by_title;

#gets the keys of the
filtered_titles = ratings_by_title.index[ratings_by_title >= 250];

# use loc for single column filter and use iloc for multiple colum filter
mean_active_ratings = mean_rating_by_gender.loc[filtered_titles];

# print filtered_titles;
# print mean_active_ratings;


# print data.columns.get_indexer(['title'])