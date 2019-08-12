import tensorflow as tf
v = tf.Variable(0,dtype=tf.float32,name='v')
ema = tf.train.ExponentialMovingAverage(0.99)
maintain_averages_op = ema.apply(tf.global_variables())
saver = tf.train.Saver()
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    sess.run(tf.assign(v,10))
    sess.run(maintain_averages_op)
    saver.save(sess,'./model.ckpt')
    print(sess.run([v,ema.average(v)]))