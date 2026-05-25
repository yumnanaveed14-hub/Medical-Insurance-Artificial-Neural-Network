# 🧠 Medical Insurance Cost Prediction using Deep Learning (ANN)

## 📌 Project Overview

This project is a **Deep Learning-based Medical Insurance Cost Prediction system** built using an Artificial Neural Network (ANN).  
The model predicts insurance charges based on personal health and demographic factors such as age, BMI, smoking status, number of children, and region.

The project demonstrates the complete pipeline of a Deep Learning application including data preprocessing, model training, evaluation, and deployment using a web interface.

---

## 🚀 Live Demo

👉 Gradio App  
[https://your-gradio-link-here](https://b3da074a0a1ce2ab29.gradio.live/)

---

## 📊 Problem Statement

Medical insurance cost prediction is a regression problem where the goal is to estimate the insurance charges for individuals based on their attributes.  
Traditional machine learning models often fail to capture complex nonlinear relationships, which is why a **Neural Network (ANN)** is used.

---

## 🧠 Deep Learning Model

A fully connected **Artificial Neural Network (ANN)** was built using TensorFlow/Keras.

### Architecture:
- Input Layer: 6 features
- Hidden Layer 1: 128 neurons (ReLU)
- Hidden Layer 2: 64 neurons (ReLU)
- Hidden Layer 3: 32 neurons (ReLU)
- Output Layer: 1 neuron (Linear activation)

---

## ⚙️ Workflow

1. Data Collection (Medical Insurance dataset)
2. Data Preprocessing
   - Encoding categorical variables
   - Feature scaling using StandardScaler
3. Train-Test Split (80-20)
4. ANN Model Building
5. Model Training
6. Model Evaluation
7. Deployment using Gradio Web Interface

---

## 📂 Dataset Features

- Age
- Sex
- BMI
- Children
- Smoker
- Region
- Charges (Target Variable)

---

## 🛠️ Tech Stack

- Python 🐍
- TensorFlow / Keras 🧠
- Scikit-learn 📊
- Pandas & NumPy 🔢
- Gradio 🌐
- Google Colab ☁️

---

## 📈 Model Performance

The model was evaluated using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

The ANN successfully learned nonlinear relationships between features and insurance charges.

---

## 🖥️ Web Application

A simple and interactive **Gradio interface** was built to allow users to input their details and get real-time insurance cost predictions.

---

## 📸 Screenshots

(Add your screenshots here)

- Model training output
- Gradio interface UI
- Prediction results

---

## 📦 Installation (For Local Use)

```bash
pip install tensorflow gradio scikit-learn pandas numpy joblib
