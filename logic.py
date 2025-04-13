from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def detect_bird(image, model_path="keras_model.h5", labels_path="labels.txt"):
  np.set_printoptions(suppress=True)
  model = load_model(model_path, compile=False)
  class_names = open(labels_path, "r", encoding="UTF-8").readlines()
  image = image.convert("RGB")
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
  image_array = np.asarray(image)
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
  data[0] = normalized_image_array
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]
  return class_name[2:], confidence_score*100

  
