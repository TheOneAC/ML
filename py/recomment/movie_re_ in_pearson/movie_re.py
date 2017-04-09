#!/usr/bin/python

import random
import pandas as pd

from pandas import Series, DataFrame
from math import sqrt

def data_pre(csvname):
	df = pd.read_csv(csvname)
	df.fillna(0, inplace = True)

	movie = []
	for movie_name in df.icol(0):
			movie.append(movie_name)

	user = []
	for username  in df.columns:
		user.append(username);
	dic_socre = {}
	for index,username  in zip(range(df.shape[1]),user):
		score = {}
		if index != 0:
			for movie_name, star in zip(movie, df.icol(index)):
				if star != 0:
					score[movie_name] = star
			dic_socre[username] = score

	
	user = user[1:]
	return user, dic_socre
		


def pearson(rating1, rating2):
	sum_xy = 0
	sum_x = 0
	sum_y = 0
	sum_x2 = 0
	sum_y2 = 0
	n = 0
	for key in rating1:
		if key in rating2:
			n += 1
			x = rating1[key]
			y = rating2[key]
			sum_xy += x * y
			sum_x += x
			sum_y += y;
			sum_x2 += pow(x, 2)
			sum_y2 += pow(y, 2)
	denominator = sqrt(sum_x2 - pow(sum_x, 2)/n) * sqrt(sum_y2 - pow(sum_y, 2)/n)
	if denominator == 0:
		return 0
	else:
		return (sum_xy - sum_x * sum_y/n)/denominator


def computeNearstNeighbor(username, users):
	'''computer username to all users distance and sort'''
	distances = []
	for user in users:
		if user != username:
			#distance = manhattan(users[user],users[username])
			#distance = minkowski(users[user],users[username], 2)
			# olijide distance
			distance = pearson(users[user],users[username])
			distances.append((distance,user))
	distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
	return distances

def recommend(username, users):
	nearest_username = computeNearstNeighbor(username,users)[0][1]
	recommendations = []
	neighborRatings = users[nearest_username]
	userRatings = users[username]
	for artist in neighborRatings:
		if not artist in userRatings:
			recommendations.append((artist, neighborRatings[artist]))
			#recommendations.append(artist)
	return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)
	#return recommendations






if __name__  == "__main__":
	user, comments = data_pre('Movie_Ratings.csv')
	for username in user:
   		print "recomend movie to < " + username + " >: "
   		print recommend(username, comments)
   	
   	