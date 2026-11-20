# SMS Spam Detection

A Machine Learning-based SMS Spam Detection system that classifies text messages as **Spam** or **Ham (Legitimate)** using TF-IDF feature extraction and a tuned Support Vector Machine (SVM) classifier.

The project includes a Streamlit web application that allows users to enter SMS messages and receive real-time predictions.

## Project Overview

SMS spam messages are commonly used for fraudulent promotions, phishing attempts, unwanted advertisements, and scams. This project applies supervised machine learning to identify potentially unwanted messages automatically.

The system uses natural language preprocessing, TF-IDF vectorization, and multiple classification algorithms to identify the most effective model.

## Key Features

- SMS text preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- TF-IDF feature extraction
- Comparison of three machine learning algorithms
- SVM hyperparameter tuning using GridSearchCV
- Model evaluation using classification metrics
- Saved machine learning pipeline
- Interactive Streamlit web interface
- Prediction history during an application session

## Machine Learning Workflow

```text
Dataset Collection
        |
        v
Data Loading and Exploration
        |
        v
Text Preprocessing
        |
        v
Label Encoding
        |
        v
Train-Test Split (80:20)
        |
        v
TF-IDF Feature Extraction
        |
        v
Model Training
        |
        v
Algorithm Comparison
        |
        v
SVM Hyperparameter Tuning
        |
        v
Model Evaluation
        |
        v
Save Final Model
        |
        v
Streamlit Application
        |
        v
Spam / Ham Prediction
```

## Dataset

**Dataset:** SMS Spam Collection

**Source:** [UCI Machine Learning Repository - SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)

The dataset contains 5,574 SMS messages labelled as:

- `ham`: Legitimate messages
- `spam`: Unwanted or spam messages

The dataset is used for supervised binary text classification.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Text Processing | TF-IDF |
| Algorithms | Naive Bayes, Logistic Regression, Linear SVM |
| Hyperparameter Tuning | GridSearchCV |
| Model Serialization | Joblib |
| Development Environment | Jupyter Notebook, VS Code |
| Web Application | Streamlit |
| Version Control | Git, GitHub |

## Machine Learning Models

Three classification algorithms were evaluated using the same training and test split.

| Model | Accuracy | Precision (Spam) | Recall (Spam) | F1 Score (Spam) |
|---|---:|---:|---:|---:|
| Multinomial Naive Bayes | 96.62% | 100.00% | 73.28% | 84.58% |
| Logistic Regression | 97.58% | 90.77% | 90.08% | 90.42% |
| SVM | 97.97% | 93.65% | 90.08% | 91.83% |
| **Tuned SVM** | **98.07%** | **93.70%** | **90.84%** | **92.24%** |

The tuned SVM was selected as the final model based on its overall performance.

## Final Model Evaluation

**Final model:** Tuned Linear Support Vector Machine (LinearSVC)

<details>
<summary>Classification Report</summary>

| Class | Precision | Recall | F1 Score | Support |
|---|---:|---:|---:|---:|
| Ham | 0.99 | 0.99 | 0.99 | 903 |
| Spam | 0.94 | 0.91 | 0.92 | 131 |
| Accuracy | | | 98.07% | 1,034 |

</details>

### Confusion Matrix

| Actual / Predicted | Ham | Spam |
|---|---:|---:|
| Ham | 895 | 8 |
| Spam | 12 | 119 |

### Performance Summary

- Test accuracy: **98.07%**
- Spam precision: **93.70%**
- Spam recall: **90.84%**
- Spam F1-score: **92.24%**
- Correct predictions: **1,014 / 1,034**
- False positives: **8**
- False negatives: **12**

The model correctly identified 119 of 131 spam messages in the test set.

*Note: These results are based on the held-out test dataset. Performance on unseen real-world messages may differ.*

## Project Structure

```text
SMS-Spam-Detection/
│
├── dataset/
│   ├── SMSSpamCollection
│   └── readme
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── models/
│   └── final_spam_detection_model.pkl
│
├── src/
│   └── predict.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

The `.venv/` virtual environment is intentionally excluded from version control.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Debnathdas/SMS-Spam-Detection.git
```

### 2. Navigate to the project directory

```bash
cd SMS-Spam-Detection
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

Open the local application in your browser:

```text
http://localhost:8501
```

## Application Usage

1. Start the Streamlit application.
2. Enter an SMS message in the input field.
3. Click **Analyze Message**.
4. View the classification result.
5. Review previous predictions in the session history.

Example:

| Input Message | Expected Classification |
|---|---|
| Congratulations! You won a free prize. Claim now! | Spam |
| Hey, are you coming tomorrow? | Ham |
| URGENT! Claim your cash reward now. | Spam |
| Please call me when you reach home. | Ham |

These examples illustrate expected use cases; actual predictions are generated by the trained model.

## Model Implementation Details

### 1. Text Preprocessing

The preprocessing stage includes:

- Converting text to lowercase
- Removing URLs
- Removing punctuation and special characters
- Normalizing whitespace
- Removing duplicate and invalid records
- Encoding labels into numerical values

### 2. TF-IDF Vectorization

Term Frequency-Inverse Document Frequency (TF-IDF) converts SMS messages into numerical feature vectors.

The final pipeline applies TF-IDF before passing the resulting features to the classifier.

### 3. Classification

The final classifier is LinearSVC, selected after comparing multiple algorithms and performing hyperparameter tuning.

### 4. Hyperparameter Optimization

GridSearchCV with stratified 5-fold cross-validation was used to search for suitable TF-IDF and SVM hyperparameters.

### 5. Model Serialization

The complete trained pipeline is saved using Joblib, allowing the application to load the vectorizer and classifier without retraining.

## Limitations

- The model is trained on the SMS Spam Collection dataset and may not generalize to every type of modern spam.
- New spam patterns and unfamiliar language may affect prediction quality.
- The system performs binary classification and does not independently verify whether a message is fraudulent.
- LinearSVC does not directly provide calibrated prediction probabilities.
- The evaluation results depend on the dataset and selected train-test split.

## Future Improvements

- Expand training data with newer SMS spam examples.
- Improve detection of phishing and fraudulent messages.
- Experiment with additional text classification models.
- Add probability calibration where appropriate.
- Add automated unit and integration tests.
- Improve the application interface and prediction analytics.
- Deploy the application to a public hosting platform.
- Monitor model performance and retrain when necessary.

## Author

**Debnath Das**

- GitHub: [@Debnathdas](https://github.com/Debnathdas)
- Project Repository: [SMS-Spam-Detection](https://github.com/Debnathdas/SMS-Spam-Detection)

## Acknowledgements

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/) for the SMS Spam Collection dataset.
- [Scikit-learn](https://scikit-learn.org/) for machine learning tools.
- [Streamlit](https://streamlit.io/) for the interactive application framework.

---

**Project:** SMS Spam Detection  
**Domain:** Machine Learning / Natural Language Processing  
**Task:** Supervised Binary Text Classification  
**Final Algorithm:** Tuned Linear Support Vector Machine (LinearSVC)
