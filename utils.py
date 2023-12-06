import tensorflow as tf
import os
import shutil
import glob
import random
import matplotlib.pyplot as plt
from tensorflow.keras import preprocessing

def copy(paths, destination):
    for path in paths:
      book = ((path.split("/")[1]).split("-")[0])
      chap = ((path.split("/")[-1]))
      shutil.copy2(path, destination)
      os.rename(os.path.join(destination, chap), os.path.join(destination, book + chap))


def create_dataset(path):
  dataset = preprocessing.text_dataset_from_directory(
      path,
      labels = None,
      batch_size = batch_size,
      seed = seed
  )
  return dataset

def render_history(history):
    plt.title("Training loss vs. validation loss")
    plt.plot(history.history["loss"], label="loss")
    plt.plot(history.history["val_loss"], label="val_loss")
    plt.legend()
    plt.show()
    plt.close()

    plt.title("Training accuracy vs. validation accuracy")
    plt.plot(history.history["accuracy"], label="accuracy")
    plt.plot(history.history["val_accuracy"], label="val_accuracy")
    plt.legend()
    plt.show()
    plt.close()


def compare_histories(history_list):
    for training_name, history in history_list.items():
      plt.plot(history["val_accuracy"], label=training_name)
      
    plt.legend()
    plt.title("Comparision of val_accuracy")
    plt.show()
