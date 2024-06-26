# Heart Failure Predictor

A heart failure predictor app made as a Machine Learning project in BINUS University.

- 2602078726 • Albert Yulius Ramahalim ([ZaniteA](https://github.com/ZaniteA))
- 2602069596 • Jack Julius Ryadi Lie ([jackyy](https://github.com/jackyy))
- 2602082944 • Christoffer Edbert Karuniawan ([Chrisedyong](https://github.com/Chrisedyong))


## About

In this project, we build a classification model for heart failure prediction using Gradient Boosting Classifier. This project is based on [fedesoriano's Heart Failure Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction/data?select=heart.csv), which is a combination of several independent datasets on heart failure.

This project consists mainly of two parts:

- An [interactive Python notebook](./Heart_Failure_Predictor.ipynb), where we performed the exploratory data analysis (EDA), data preprocessing, and model experimentation before finally choosing the Gradient Boosting Classifier.

- A graphical user interface (GUI) app developed using [PyQt6](https://pypi.org/project/PyQt6/) to provide a user-friendly method of interacting with our classifier. The source code can be found under `./src/`.

  Currently, only Windows is supported. The release and installation instructions can be found [here](https://github.com/ZaniteA/heart-failure-predictor/releases/tag/v1.2).
