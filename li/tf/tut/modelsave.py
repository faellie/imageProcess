#from https://www.tensorflow.org/guide/keras
import tensorflow as tf
from tensorflow.python.saved_model import tag_constants

# Create some variables.
v1 = tf.get_variable("v1", shape=[3], initializer = tf.zeros_initializer)
v2 = tf.get_variable("v2", shape=[5], initializer = tf.zeros_initializer)

inc_v1 = v1.assign(v1+1)
dec_v2 = v2.assign(v2-1)

# Add an op to initialize the variables.
init_op = tf.global_variables_initializer()

# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, initialize the variables, do some work, and save the
# variables to disk.
# with tf.Session() as sess:
#     sess.run(init_op)
#     # Do some work with the model.
#     inc_v1.op.run()
#     dec_v2.op.run()
#     # Save the variables to disk.
#     save_path = saver.save(sess, "/opt/TF/output/tmp/model.ckpt")
#     print("Model saved in path: %s" % save_path)


builder = tf.saved_model.builder.SavedModelBuilder("/opt/TF/output/tmp1/")
with tf.Session(graph=tf.Graph()) as sess:
    inputs_dict = {
        "batch_size_ph": batch_size_ph,
        "features_data_ph": features_data_ph,
        "labels_data_ph": labels_data_ph
    }
    outputs_dict = {
        "logits": logits
    }
    builder.add_meta_graph_and_variables(sess,
                                         [tag_constants.TRAINING],
                                         # signature_def_map=foo_signatures,
                                         # assets_collection=foo_assets,
                                         strip_default_attrs=False)
    builder.save()
