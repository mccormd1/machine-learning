# Solution is available in the other "solution.py" tab
import tensorflow as tf

# TODO: Convert the following to TensorFlow:
x = 10
y = 2
z = x/y - 1
print('normal python:',z)

x=tf.constant(10)
y=tf.constant(2)
z=tf.subtract(tf.divide(x,y),tf.cast(tf.constant(1),tf.float64))
# TODO: Print z from a session

with tf.Session() as sess:
    output = sess.run(z)
    print('Tensorflow version:',output)

