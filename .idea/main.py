
from csv_functions import *

import tensorflow as tf
import numpy as np

# get cameras data
cameras = get_cameras('data/Mapa_Ubicaci_n_C_maras_de_Fotodetecci_n_Municipio_de_Medell_n.csv')

# get accidents data
accidents = get_accidents('data/Accidentalidad_Vial_Municipio_de_Medell_n_2016_Geo_only.csv')

print(cameras)
print(len(accidents))

import matplotlib.pyplot as plt
import math


accident_x_values = [accident.get_x() for accident in accidents]
accident_y_values = [accident.get_y() for accident in accidents]
plt.scatter(accident_x_values, accident_y_values)

camera_x_values = [camera.get_x() for camera in cameras]
camera_y_values = [camera.get_y() for camera in cameras]

print(len(cameras))

data_length = len(accidents)

iteration_n = 100

num_points = len(accidents)
dimensions = 2

# Código de ejmplo tomado como referencia para clustering.
# https://blog.altoros.com/using-k-means-clustering-in-tensorflow.htm l

data = np.empty([num_points, 2])


for i, point in enumerate(accident_x_values):
    data[i] = [accident_x_values[i], accident_y_values[i]]

data_tf = tf.convert_to_tensor(data, np.float64) #.float32)

number_of_clusters = 77

centroids = tf.Variable(tf.slice(tf.random_shuffle(data_tf), [0, 0], [number_of_clusters, -1]))


points_expanded = tf.expand_dims(data_tf, 0)
centroids_expanded = tf.expand_dims(centroids, 1)

distances = tf.reduce_sum(tf.square(tf.subtract(points_expanded, centroids_expanded)), 2)
assignments = tf.argmin(distances, 0)

means = []
for c in np.arange(number_of_clusters):
    means.append(tf.reduce_mean(
        tf.gather(data_tf,
                  tf.reshape(
                      tf.where(
                          tf.equal(assignments, c)
                      ), [1, -1])
                  ), reduction_indices=[1]))

new_centroids = tf.concat(means , 0)

update_centroids = tf.assign(centroids, new_centroids)
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for step in np.arange(iteration_n):
        [_, centroid_values, points_values, assignment_values] = sess.run(
            [update_centroids, centroids, data_tf, assignments])

    print
    "centroids" + "\n", centroid_values

plt.scatter(points_values[:, 0], points_values[:, 1], c=assignment_values, s=50, alpha=0.5)
plt.plot(centroid_values[:, 0], centroid_values[:, 1], 'kx', markersize=15)

plt.scatter(camera_x_values, camera_y_values)

plt.show()

