import tensorflow as tf
from tensorflow.python.tools import inspect_checkpoint as chkp
from tensorflow.python.saved_model import tag_constants
tf.reset_default_graph()

# Create some variables.
chkp_paht="/home/zihuangw/workspace/sandbox/LI/TF/TensorBox/output/lstm_rezoom_2018_07_16_15.59/save.ckpt-50000"
#chkp_paht="/opt/TF/output/tmp/model.ckpt"
#chkp.print_tensors_in_checkpoint_file(chkp_paht, tensor_name='', all_tensors=False, all_tensor_names=True)

# v1 = tf.get_variable("v1", shape=[3])
# v2 = tf.get_variable("v2", shape=[5])
# Add ops to save and restore all the variables.
x_in = tf.placeholder(tf.float32, name='x_in', shape=[480, 640, 3])
saver = tf.train.Saver()

# Later, launch the model, use the saver to restore variables from disk, and
# do some work with the model.
with tf.Session() as sess:
    #Restore variables from disk.
    sess.run(tf.global_variables_initializer())
    saver.restore(sess, chkp_paht)

    print("Model restored.")
    #Check the values of the variables
    print("v1 : %s" % v1.eval())
    print("v2 : %s" % v2.eval())
# with tf.Session(graph=tf.Graph()) as sess:
#     tf.saved_model.loader.load(sess, [tag_constants.SERVING],  "/opt/TF/output/tmp1/")
#     print("v1 : %s" % v1.eval())
#     print("v2 : %s" % v2.eval())
