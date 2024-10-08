# Heart Disease Detection Project

## Project Overview
This project aims to predict heart disease occurrence based on multiple health-related features. Using machine learning models, the project addresses the challenge of class imbalance and ensures accurate prediction of heart disease risks. The dataset includes various demographic, behavioral, and medical attributes for individuals, such as BMI, Smoking, Alcohol Drinking, Physical Health, and more.

The focus is on using data preprocessing techniques and machine learning algorithms to classify whether an individual has heart disease (Yes or No). Special attention is paid to class imbalance in the dataset by using a combination of oversampling and undersampling methods.

## Dataset

- **Source**: The dataset consists of 319,795 rows and 18 columns. It includes medical, lifestyle, and demographic information.
- **Target Variable**: HeartDisease (binary: Yes/No)
- **Features**:
  - Continuous: BMI, PhysicalHealth, MentalHealth, SleepTime
  - Categorical: Smoking, AlcoholDrinking, Stroke, DiffWalking, Sex, AgeCategory, Race, Diabetic, PhysicalActivity, GenHealth, Asthma, KidneyDisease, SkinCancer

## Project Flow

1. **Data Preprocessing**
   - **Data Cleaning**: Duplicates were removed to avoid redundancy in the dataset.
   - **Handling Categorical Features**: One-hot encoding was applied to categorical variables with more than two categories, such as AgeCategory, Race, Diabetic, and GenHealth, converting them into numerical form.

2. **Handling Class Imbalance**
   The dataset was highly imbalanced, with significantly more instances of individuals without heart disease than those with the condition. The following techniques were implemented:
   - **Oversampling**: Techniques like SMOTE (Synthetic Minority Over-sampling Technique) were used to generate synthetic examples for the minority class (individuals with heart disease) to balance the class distribution.
   - **Undersampling**: The majority class (individuals without heart disease) was reduced in size to prevent overwhelming the model with majority class examples, without discarding excessive amounts of data.

3. **Model Training**
   Several machine learning algorithms were trained to predict heart disease, including:
   - Logistic Regression
   - Decision Trees
   - Random Forests
   - Support Vector Machines (SVM)
   - Gradient Boosting

4. **Evaluation Metrics**
   - **Accuracy**: The percentage of correctly predicted instances out of the total predictions.
   - **F1 Score**: A balanced evaluation metric considering both precision and recall, especially important for imbalanced datasets like this one. The F1 score helped assess how well the model performed on the minority class (HeartDisease = Yes).

## Model Selection and Hyperparameter Tuning

Several machine learning models were tested, and after evaluating their performance, **Gradient Boosting** was chosen as the best model. It provided the most balanced performance, particularly in handling class imbalance. 

For further optimization, **BayesSearchCV** was used for hyperparameter tuning. This method allowed for an efficient search through the hyperparameter space, improving both the accuracy and F1 score of the model.

## Results

- **Testing Accuracy**: 87.9%
- **F1 Score**: 70.59%

Despite the strong overall performance, the model had a **10% false negative rate**, which is concerning due to the limited data available for individuals with heart disease. However, given the original class imbalance (10:1 ratio of majority to minority), this result is acceptable.

Key insights from the results:
- The model performed well on **unseen data**, even after dropping 30% of the majority class (individuals without heart disease), demonstrating that the model's efficiency was not compromised by the data reduction.
- To further improve accuracy and reliability, **more data collection** from individuals with heart disease is essential, as it will help reduce false negatives.

## Key Challenges and Solutions

- **Class Imbalance**: The most significant challenge in this project was class imbalance. Without addressing this issue, the model would have been biased toward predicting the majority class (No heart disease). By using a combination of oversampling and undersampling, the dataset was balanced, ensuring that the model could effectively learn patterns from both classes.

## Future Improvements

1. **Increasing Data Collection**: Gathering more data, particularly from individuals with heart disease, is crucial for improving the model’s predictive performance and reducing false negatives.

## Conclusion

The project successfully addresses the heart disease prediction challenge by focusing on accurate classification and handling the inherent class imbalance. The Gradient Boosting model, optimized through Bayesian search, demonstrated strong generalization to unseen data, achieving high accuracy and F1 scores. However, reducing false negatives and further improving the model’s reliability requires more comprehensive data collection from individuals with heart disease.
