# Fashion-MNIST Image Classifier

## Description

An interactive web application built with Streamlit for image classification using two deep learning models: a Convolutional Neural Network (CNN) and a VGG16-based model.

The application allows users to upload clothing images, select a model, and explore classification results and training performance.

## Features

- Upload images in JPG, JPEG, or PNG format.
- Switch between CNN and VGG16 models.
- Automatically preprocess images according to the selected model.
- Display the uploaded image.
- Predict clothing categories using pretrained-on-Fashion-MNIST models.
- Display the predicted class and its probability.
- Show classification probabilities for all 10 Fashion-MNIST classes.
- Visualize training and validation accuracy and loss.

## Technologies

- **Python** — application logic and data processing.
- **Streamlit** — interactive web interface.
- **TensorFlow / Keras** — neural network models and predictions.
- **NumPy** — image array processing.
- **Pillow** — image loading and preprocessing.
- **Matplotlib** — training performance visualization.
- **Poetry** — dependency management.

## Models

The application uses two models trained on the Fashion-MNIST dataset:

**CNN**
- Custom convolutional neural network.
- Input shape: 28 × 28 × 1.
- Classification into 10 clothing categories.

**VGG16**
- Model based on the VGG16 architecture.
- Input shape: 224 × 224 × 3.
- Transfer learning for Fashion-MNIST classification.

## Installation & Usage

Clone the repository:

```bash
git clone <repository-url>
cd ml-app
```

Install dependencies using Poetry:

```bash
poetry install
```

Run the Streamlit application:

```bash
poetry run streamlit run app.py
```

Open the application in your browser, upload an image, and select the desired classification model.

## Dataset

The models were trained using the Fashion-MNIST dataset, which contains 70,000 grayscale images across 10 clothing categories.

**Note:** The models were trained on Fashion-MNIST images. Predictions on real-world photographs may be less accurate due to differences in image backgrounds, lighting, and object appearance.
