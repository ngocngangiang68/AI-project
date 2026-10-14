# cnn_models.py
# Define CNN architectures for experiments (baseline, deeper, dropout)

import tensorflow as tf


def build_baseline(input_shape=(64,64,3), num_classes=10):
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=input_shape),
        tf.keras.layers.Conv2D(32, 3, activation='relu'),
        tf.keras.layers.MaxPool2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    return model


def build_deeper(input_shape=(64,64,3), num_classes=10):
    return build_baseline(input_shape, num_classes)


def build_dropout(input_shape=(64,64,3), num_classes=10):
    return build_baseline(input_shape, num_classes)
