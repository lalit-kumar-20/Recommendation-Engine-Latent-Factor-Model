# Recommendation_System-Collaborative_Filtering

The model recommends a set of movies to user based on Machine Learning Techniques

Algorithm:- Latent Factor Model for Collaborative Filtering

Optimization Technique:- Stochastic Gradient Descent

Steps--

1.Analyze the data

2.Construct a rating matrix

3.Initialize factor matrices

4.Compute the error using RMSE

5.Minimize error using SGD

Save the output(in pkl file) in the form of MXN matrix, where M is the number of users(as userID) and N is the number of movies(as artistID) where each entry rij represents the rating of product j for a given user i.
Here we get two differnet list.

 1.A higher rating indicates that the user is more likely to watch that listed movies.
 
 2.A lower rating indicates that the user is dislikely to watch that listed movies.
