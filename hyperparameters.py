"""
Hyperparameters modeled from project 4 for training process
"""

"""
Number of epochs. If you experiment with more complex networks you
might need to increase this. Likewise if you add regularization that
slows training.
"""
num_epochs = 10

"""
A critical parameter that can dramatically affect whether training
succeeds or fails. The value for this depends significantly on which
optimizer is used. Refer to the default learning rate parameter
"""
learning_rate = 1e-4

"""
Momentum on the gradient (if you use a momentum-based optimizer)
"""
momentum = 0.01

"""
Resize image size
"""
img_size = 224

"""
Sample size for calculating the mean and standard deviation of the
training data. This many images will be randomly seleted to be read
into memory temporarily.
"""
preprocess_sample_size = 400

"""
Maximum number of weight files to save to checkpoint directory. If
set to a number <= 0, then all weight files of every epoch will be
saved. Otherwise, only the weights with highest accuracy will be saved.
"""
max_num_weights = 5

"""
Defines the number of training examples per batch.
You don't need to modify this.
"""
batch_size = 25

"""
The number of hand classes. Don't change this.
"""
num_classes = 6
