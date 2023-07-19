# Clustering
Code for hierarchical clustering, 1-d k-means clustering, 2-d k-means clustering and their associated sub functions

Sub functions include: min_val which finds the smallest value in a list, max-val which finds the maximum value, min_index which finds the number with the smallest index, max_index which finds the number with the largest index, asc which sorts a list of values in ascending order, desc which sorts a list of values in descending order, distance which finds the distance each point is from the next (which is most useful when the list is already sorted by asc or desc) and then displays the points that are the closest together, newlist which makes a new list, dist_index which takes a list of data and returns the indexes of the two closest points, and average which takes the average values of a list of data.

Hierarchical clustering sorts and creates groups via points that are close to each other. It is less sensitive to outliers making it a safe option, although it is not possible to specify the number of clusters desired by the user.

K-means clustering will create groups given a specified k, or the number of clusters needed. 1-d is specific to individual values of data while 2-d can be used for coordinates on scatter plots. 
