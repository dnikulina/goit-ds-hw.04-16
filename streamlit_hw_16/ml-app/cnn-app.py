import streamlit as st
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
import json

model = load_model("models/cnn_model.keras")
model_2 = load_model("models/vgg16_model.keras")

model_choice = st.selectbox("За якою моделлю класифікуємо?", ["CNN", "VGG16"])

st.title(f"{model_choice} Класифікатор")


uploaded_file = st.file_uploader("Виберіть зображення...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Завантажене зображення")

    if model_choice == "CNN":
        selected_model = model
        formatted_image = ImageOps.grayscale(image)
        formatted_image = formatted_image.resize((28, 28))
        formatted_image = np.array(formatted_image) / 255.0
        formatted_image = np.expand_dims(formatted_image, axis=-1)
        formatted_image = np.expand_dims(formatted_image, axis=0)
        with open("histories/cnn_history.json", "r") as f:
            training_history = json.load(f)
    else:
        selected_model = model_2
        formatted_image = ImageOps.grayscale(image).convert("RGB")
        formatted_image = formatted_image.resize((32, 32))
        formatted_image = np.array(formatted_image) / 255.0
        formatted_image = np.expand_dims(formatted_image, axis=0)
        with open("histories/vgg16_history.json", "r") as f:
            training_history = json.load(f)

    predictions = selected_model.predict(formatted_image)

    acc = training_history["accuracy"]
    val_acc = training_history["val_accuracy"]
    loss = training_history["loss"]
    val_loss = training_history["val_loss"]
    epochs = range(1, len(acc) + 1)

    fig, ax = plt.subplots()
    ax.plot(epochs, acc, label="Training acc", color="indigo")
    ax.plot(epochs, val_acc, label="Validation acc", color="pink")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Accuracy")
    ax.grid(True)
    ax.legend()
    st.subheader(f"Графік точності моделі {model_choice}")
    st.pyplot(fig)
    # plt.close(fig)

    fig, ax = plt.subplots()
    ax.plot(epochs, loss, label="Training loss", color="indigo")
    ax.plot(epochs, val_loss, label="Validation loss", color="pink")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.grid(True)
    ax.legend()
    st.subheader(f"Графік помилки моделі {model_choice}")
    st.pyplot(fig)
    # plt.close(fig)

    class_names = [
        "T-shirt/top",
        "Trouser",
        "Pullover",
        "Dress",
        "Coat",
        "Sandal",
        "Shirt",
        "Sneaker",
        "Bag",
        "Ankle boot",
    ]

    predicted_class = np.argmax(predictions[0])
    predicted_name = class_names[predicted_class]
    percentage = predictions[0][predicted_class] * 100
    st.success(f"Передбачений клас: {predicted_name}")
    st.write(f"Впевненість моделі: {percentage:.2f}%")
    st.write("Передбачення інших класів:")
    for i, prediction in enumerate(predictions[0]):
        if i != predicted_class:
            class_percent = prediction * 100
            st.write(f"{class_names[i]}: {class_percent:.2f}%")
