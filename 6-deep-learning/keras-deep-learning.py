# Deep learning refers to neural networks with multiple hidden layers that can
# learn increasingly abstract representations of the input data. This is obviously an
# oversimplification, but it’s a practical definition for us right now.

import tensorflow as tf
sess = tf.Session()

from keras import backend as K
K.set_session(sess)
