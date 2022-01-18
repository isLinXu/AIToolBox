import numpy as np
import os


class Dataset():
    def __init__(self, images, labels):
        # convert from [0, 255] -> [0.0, 1.0]
        images = images.astype(np.float32)
        images = np.multiply(images, 1.0 / 255.0)
        self._images = images
        self._labels = labels

    @property  # getter
    def images(self):
        return self._images

    @property
    def labels(self):
        return self._labels


def extract_images(image_dir, name):
    files = open(os.path.join(image_dir, name), 'rb')
    files.read(16)

    buf = files.read(28 * 28 * 60000)

    images = np.frombuffer(buf, dtype=np.uint8)
    # images = images.reshape(-1, 784)
    images = images.reshape(-1, 1, 28, 28)
    return images


def extract_labels(image_dir, name):
    files = open(os.path.join(image_dir, name), 'rb')
    files.read(8)

    buf = files.read(28 * 28 * 10000)

    labels = np.frombuffer(buf, dtype=np.uint8)
    return labels


def read_data_sets(image_dir):
    class DataSets():
        pass

    data_sets = DataSets()

    TRAIN_IMAGES = 'train-images-idx3-ubyte'
    TRAIN_LABELS = 'train-labels-idx1-ubyte'
    TEST_IMAGES = 't10k-images-idx3-ubyte'
    TEST_LABELS = 't10k-labels-idx1-ubyte'
    VALIDATION_SIZE = 5000

    train_images = extract_images(image_dir, TRAIN_IMAGES)
    train_labels = extract_labels(image_dir, TRAIN_LABELS)

    train_images = train_images[VALIDATION_SIZE:]
    train_labels = train_labels[VALIDATION_SIZE:]

    validation_images = train_images[:VALIDATION_SIZE]
    validation_labels = train_labels[:VALIDATION_SIZE]

    test_images = extract_images(image_dir, TEST_IMAGES)
    test_labels = extract_labels(image_dir, TEST_LABELS)

    data_sets.train = Dataset(train_images, train_labels)
    data_sets.validation = Dataset(validation_images, validation_labels)
    data_sets.test = Dataset(test_images, test_labels)

    return data_sets