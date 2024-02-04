import joblib
import pandas as pd


def makePrediction(year: int,
                   title: str,
                   category: str,
                   residence: str,
                   experience: str,
                   e_type: str,
                   setting: str,
                   c_location: str,
                   c_size: str):
    """Loads model and creates a prediction based upon input"""
    # convert input to dataframe
    pred_data = pd.DataFrame({'work_year': [year],
                              'job_title': [title],
                              'job_category': [category],
                              'employee_residence': [residence],
                              'experience_level': [experience],
                              'employment_type': [e_type],
                              'work_setting': [setting],
                              'company_location': [c_location],
                              'company_size': [c_size]})
    # Load model
    model = joblib.load('models/xgboost_model.joblib')
    transformer = joblib.load('models/column_transformer.joblib')

    # Transform
    transformed = transformer.transform(pred_data)

    # Make prediction w/loaded model
    predicted_salary = model.predict(transformed)

    print(f"Predicted Salary: {predicted_salary}")
    return predicted_salary
