<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Python][python-shield]][python-url]
[![scikit-learn][sklearn-shield]][sklearn-url]
[![FastAPI][fastapi-shield]][fastapi-url]
[![Stars][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO / TITLE -->
<br />
<div align="center">

<h1 align="center">🚢 Titanic Survival Prediction Model</h1>

<p align="center">
  Predict Survival, Empower Decisions Instantly
  <br />
  <br />
  <a href="https://github.com/USERNAME/REPO_NAME"><strong>Explore the Repository »</strong></a>
  <br />
  <br />
  <a href="#downloads">Download Files</a>
  ·
  <a href="#getting-started">Run Locally</a>
  ·
  <a href="https://github.com/USERNAME/REPO_NAME/issues">Report Bug</a>
</p>
</div>

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary><strong>Table of Contents</strong></summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#why-this-project">Why This Project?</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#languages-used">Languages Used</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#downloads">Downloads</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#model-details">Model Details</a></li>
    <li><a href="#future-work">Future Work</a></li>
  </ol>
</details>

---

## About The Project

This project demonstrates a **complete end-to-end Machine Learning workflow**, from data preprocessing and feature engineering to **model deployment as a web application**.

It focuses on **production-ready practices**, including:
- Pipeline-based preprocessing
- Safe model serialization
- Version-controlled environments
- Web-based inference using FastAPI

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Why This Project?

The **Titanic Survival Prediction Model** simplifies deploying ML models with an intuitive web interface for real-time predictions.

### Key Features

- 🧩 **User-Friendly Interface**  
  Collects passenger details and displays survival probabilities interactively.

- 🚀 **Seamless Integration**  
  Built to fit into scalable ML deployment architectures.

- 📦 **Environment Management**  
  Uses `requirements.txt` to ensure consistent setup across environments.

- ⚡ **Quick Insights**  
  Enables fast evaluation of individual passenger risk factors.

- 🌐 **Web-Based Accessibility**  
  Simple HTML templates allow easy customization and extension.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Built With

**Machine Learning & Data**
- 🧠 scikit-learn
- 📊 pandas, numpy

**Backend & Deployment**
- ⚡ FastAPI
- 🚀 Uvicorn

**Model Management**
- 📦 pickle
- 🔗 sklearn Pipelines & ColumnTransformer

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Languages Used

<p align="left">
  <img src="https://img.shields.io/badge/Python-78.4%25-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/HTML-21.6%25-orange?style=for-the-badge&logo=html5" />
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Project Structure

Titanic_Survival_Prediction_Model/
│
├── app.py # FastAPI backend
├── titanic_pipeline.pkl # Trained ML pipeline
├── requirements.txt # Dependency versions
├── Titanic_Model.ipynb # EDA + Training notebook
│
├── templates/
│ └── index.html # Web UI
│
└── README.md


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Downloads

- 📓 **Jupyter Notebook (EDA + Model Training)**  
  👉 [Download Titanic_Model.ipynb](https://github.com/USERNAME/REPO_NAME/blob/main/Titanic_Model.ipynb)

- 🧠 **Trained Model Pipeline (`.pkl`)**  
  👉 [Download titanic_pipeline.pkl](https://github.com/USERNAME/REPO_NAME/blob/main/titanic_pipeline.pkl)

> ⚠️ Ensure the same library versions are used when loading the pickle file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/USERNAME/REPO_NAME.git
   cd Titanic_Survival_Prediction_Model
2. Install dependencies
   ```bash
   pip install -r requirements.txt
3. Run the application
   ```bash
   uvicorn app:app --reload
4. Browser : http://127.0.0.1:8000



