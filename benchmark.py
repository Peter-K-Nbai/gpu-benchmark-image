import tensorflow as tf
import time


def check_gpu():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        return True
    else:
        return False


def benchmark(n: int):
    # create random matrices
    A = tf.random.uniform((n, n), minval=0, maxval=1, dtype=tf.float32)
    B = tf.random.uniform((n, n), minval=0, maxval=1, dtype=tf.float32)

    # warm up to ensure everything is loaded
    _ = tf.matmul(A, B)

    # benchmark matrix multiplication
    start_time = time.time()
    C = tf.matmul(A, B)
    end_time = time.time()

    return end_time - start_time
