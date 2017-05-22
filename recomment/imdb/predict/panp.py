#!/usr/bin/python


import pandas as pd
imdb_data = pd.read_csv('../inputdata/movie_metadata.csv',header=None)

#print imdb_data

#X = imdb_data.loc[:, 1:25] #+ imdb_data[:,26:]
#$y = imdb_data.loc[:,25]

mdb_data['num_critic_for_reviews']=imdb_data['num_critic_for_reviews'].fillna(0.0).astype(np.float32)
imdb_data['director_facebook_likes']=imdb_data['director_facebook_likes'].fillna(0.0).astype(np.float32)
imdb_data['actor_3_facebook_likes'] = imdb_data['actor_3_facebook_likes'].fillna(0.0).astype(np.float32)
imdb_data['actor_1_facebook_likes'] = imdb_data['actor_1_facebook_likes'].fillna(0.0).astype(np.float32)
imdb_data['gross'] = imdb_data['gross'].fillna(0.0).astype(np.float32)
imdb_data['num_voted_users'] = imdb_data['num_voted_users'].fillna(0.0).astype(np.float32)
imdb_data['cast_total_facebook_likes'] = imdb_data['cast_total_facebook_likes'].fillna(0.0).astype(np.float32)
imdb_data['num_user_for_reviews'] = imdb_data['num_user_for_reviews'].fillna(0.0).astype(np.float32)
imdb_data['facenumber_in_poster'] = imdb_data['facenumber_in_poster'].fillna(0.0).astype(np.float32)
imdb_data['actor_2_facebook_likes'] = imdb_data['actor_2_facebook_likes'].fillna(0.0).astype(np.float32)
imdb_data['budget'] = imdb_data['budget'].fillna(0.0).astype(np.float32)
imdb_data['movie_facebook_likes'] = imdb_data['movie_facebook_likes'].fillna(0.0).astype(np.float32)


imdb_data['imdb_score']=imdb_data['imdb_score'].fillna(0.0).astype(int)
my=list(zip(imdb_data['director_facebook_likes'],imdb_data['actor_1_facebook_likes'],imdb_data['actor_2_facebook_likes'],imdb_data['actor_3_facebook_likes']))
u = np.array(my)
u
X=u[:,:-1]
y=u[:,-1]
X
y
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25, random_state=0)

from sklearn import tree
clf=tree.DecisionTreeClassifier()
clf.fit(X_train,y_train)
print "DecisionTree",clf.score(X_test,y_test)