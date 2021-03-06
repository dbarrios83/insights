import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from csv_functions import *

# get cameras data
cameras = get_cameras('data/Mapa_Ubicaci_n_C_maras_de_Fotodetecci_n_Municipio_de_Medell_n.csv')


points_n = 4000
clusters_n = 77
iteration_n = 100

points = tf.constant(np.random.uniform(0, 100, (points_n, 2)))

points

camera_x_values = [camera.get_x() for camera in cameras]
camera_y_values = [camera.get_y() for camera in cameras]


centroids = tf.Variable(tf.slice(tf.random_shuffle(points), [0, 0], [clusters_n, -1]))

points_expanded = tf.expand_dims(points, 0)
centroids_expanded = tf.expand_dims(centroids, 1)

distances = tf.reduce_sum(tf.square(tf.subtract(points_expanded, centroids_expanded)), 2)
assignments = tf.argmin(distances, 0)

means = []
for c in np.arange(clusters_n):
    means.append(tf.reduce_mean(
        tf.gather(points,
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
            [update_centroids, centroids, points, assignments])

    print
    "centroids" + "\n", centroid_values

plt.scatter(points_values[:, 0], points_values[:, 1], c=assignment_values, s=50, alpha=0.5)
plt.plot(centroid_values[:, 0], centroid_values[:, 1], 'kx', markersize=15)
plt.show()