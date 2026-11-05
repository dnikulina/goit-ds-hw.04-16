# Data Science Coursework Portfolio

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat-square&logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=flat-square&logo=scikitlearn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=flat-square&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-Neural%20Networks-red?style=flat-square&logo=keras&logoColor=white)

## Overview

This repository contains my Data Science coursework and practical assignments completed during the GoIT Data Science program. The notebooks cover the full learning path from NumPy and pandas fundamentals to classical machine learning, recommendation systems, computer vision, and recurrent neural networks.

The main focus is on practical data analysis, model building, experimentation, evaluation, and understanding how different algorithms behave on real datasets.

## Tech Stack

- **Programming:** Python
- **Data Analysis:** pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** scikit-learn
- **Deep Learning:** TensorFlow, Keras
- **Recommendation Systems:** Surprise
- **Environment:** Jupyter Notebook, Google Colab
- **Version Control:** Git, GitHub

## Coursework

| Notebook | Topic | Main Tools |
| --- | --- | --- |
| [Hw1.ipynb](./Hw1.ipynb) | NumPy fundamentals and matrix operations | NumPy |
| [Hw2.1.ipynb](./Hw2.1.ipynb) | Data cleaning and exploratory analysis | pandas, Matplotlib |
| [Hw2.2.ipynb](./Hw2.2.ipynb) | Missing values and dataset preprocessing | pandas, Matplotlib |
| [Hw2.3.ipynb](./Hw2.3.ipynb) | Book dataset analysis and visualization | pandas, Matplotlib, Seaborn |
| [Hw3.1.ipynb](./Hw3.1.ipynb) | Linear regression from scratch and with scikit-learn | NumPy, pandas, scikit-learn |
| [OverfittingHW4.1.ipynb](./OverfittingHW4.1.ipynb) | Overfitting and regularization | Linear Regression, Ridge, Lasso |
| [Hw5.1.ipynb](./Hw5.1.ipynb) | Human Activity Recognition | SVM, Random Forest, feature engineering |
| [Hw6.1.ipynb](./Hw6.1.ipynb) | Clustering and dimensionality reduction | K-Means, PCA |
| [Hw7.1.ipynb](./Hw7.1.ipynb) | Recommendation systems | SVD, SVD++, NMF, GridSearchCV |
| [_GoIT_HW_8_new.ipynb](./_GoIT_HW_8_new.ipynb) | Neural network built with low-level TensorFlow | TensorFlow, MNIST |
| [Hw_9.ipynb](./Hw_9.ipynb) | Dense and convolutional neural networks | Keras, Fashion-MNIST |
| [Hw_10.ipynb](./Hw_10.ipynb) | CNN experiments and transfer learning | Keras, VGG16, data augmentation |
| [Hw11.ipynb](./Hw11.ipynb) | Recurrent neural networks for sentiment analysis | SimpleRNN, GRU, LSTM, Bidirectional RNN |

## Featured Project: Human Activity Recognition

The Human Activity Recognition project classifies four types of physical activity — **walking, running, stair movement, and idle state** — using accelerometer sensor data.

### What I did

- prepared and analyzed the sensor dataset;
- created time-domain statistical features;
- trained and compared **SVM** and **Random Forest** classifiers;
- evaluated the models using classification reports and confusion matrices;
- analyzed the effect of feature engineering on model quality.

### Result

The best-performing model was **Random Forest with time-domain features**, which achieved:

- **Accuracy: 1.00**
- **Weighted F1-score: 1.00**

Feature engineering also significantly improved recognition of the underrepresented **stairs** class.

[View Human Activity Recognition notebook](./Hw5.1.ipynb)

## Other Selected Results

### Recommendation Systems

In the recommendation systems assignment, I experimented with SVD-based models and hyperparameter tuning.

Best tuned SVD result:

- **RMSE: 0.9086**
- **n_factors:** 200
- **n_epochs:** 75
- **learning rate:** 0.007
- **regularization:** 0.1

[View recommendation systems notebook](./Hw7.1.ipynb)

### MNIST Neural Network

A fully connected neural network was implemented using low-level TensorFlow mechanisms.

- **Train accuracy: 92.16%**
- **Test accuracy: 90.02%**

[View MNIST notebook](./_GoIT_HW_8_new.ipynb)

### CNN and Transfer Learning

I experimented with CNN architectures, data augmentation, and transfer learning with VGG16 on Fashion-MNIST.

Best CNN result in the experiments:

- **Validation accuracy: 93.89%**
- **Test accuracy: 92.54%**

[View CNN and transfer learning notebook](./Hw_10.ipynb)

### Recurrent Neural Networks

I compared SimpleRNN, GRU, LSTM, Bidirectional GRU, and stacked recurrent architectures for IMDB sentiment classification.

Best test result:

- **Deep GRU → GRU model**
- **Validation accuracy: 88.80%**
- **Test accuracy: 88.66%**

[View RNN notebook](./Hw11.ipynb)

## Repository Structure

This repository contains Jupyter notebooks together with supporting datasets used in the assignments.

```text
.
├── Hw1.ipynb
├── Hw2.1.ipynb
├── Hw2.2.ipynb
├── Hw2.3.ipynb
├── Hw3.1.ipynb
├── OverfittingHW4.1.ipynb
├── Hw5.1.ipynb
├── Hw6.1.ipynb
├── Hw7.1.ipynb
├── _GoIT_HW_8_new.ipynb
├── Hw_9.ipynb
├── Hw_10.ipynb
├── Hw11.ipynb
└── datasets and supporting files
```

## About

This repository reflects my progress in Data Science and Machine Learning, from working with data and classical algorithms to building and evaluating neural network architectures.

I am currently developing my skills as a **Junior Data Scientist** and continuing to deepen my knowledge through practical experimentation and project work.
