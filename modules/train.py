import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import xgboost as xgb
from sklearn.metrics import mean_squared_error
# import visualize
import joblib


# Load in the data from csv
def loadData(csvFileName: str):
    """
    Loads data from a csv file and returns a pandas dataframe.
    """
    df = pd.read_csv(csvFileName)
    return df


# Eliminate irrelevant columns
def dropCols(dataFrame, columns: list):
    """
    Method for dropping a list of columns
    """
    return dataFrame.drop(columns=columns)


# Describe all columns
def describeAll(dataFrame):
    """
    Describes each column individually in one call
    """
    for column in dataFrame.columns:
        print(f"Description of {column}:")
        print(dataFrame[column].describe())
        print("\n")


# Check for null or empty cells
def nullEmptyCheck(dataFrame):
    """
    Checks entire DataFrame cell-by-cell for empty or null/none
    Prints column name and row of problem cell
    BEWARE: This function is n^2
    """
    for column in dataFrame:
        for index, item in enumerate(dataFrame[column]):
            if item == "" or pd.isna(item):
                raise Exception(f"Empty or null in data: {column, index}")
    print("[Data Clean] No missing or null values")


# Encode using OneHotEncoder
def encode(dataFrame):
    """
    Returns dataframe with categorical data encoded.
    Also returns column transformer for re-intreprutation.
    """
    categorical_cols = dataFrame.select_dtypes(include=['object']).columns
    # Create a ColumnTransformer object
    ct = ColumnTransformer([
        ("onehot", OneHotEncoder(sparse=False,
                                 handle_unknown='ignore'),
         categorical_cols)
    ], remainder='passthrough')

    return ct.fit_transform(dataFrame), ct


# =================================== MAIN ================================== #
# =========================================================================== #
# load raw data to pandas dataframe
df = loadData('../jobs_in_data.csv')

# investigating data
describeAll(df)

# removing irrelevant or redundant information
df = dropCols(df, ['salary', 'salary_currency'])

# display visualizations
# visualize.showNow(df)

# check for NaNs or Emptys
nullEmptyCheck(df)

# Save original values for decoding for checking predictions
original_vals = df[['employee_residence',
                    'job_category',
                    'job_title',]]

# Splitting the data into features and target variable
X = df.drop('salary_in_usd', axis=1)
y = df['salary_in_usd']

# Splitting the data into training and testing sets (75% train, 25% test)
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    random_state=42)

# Original vals from test set for decoding
original_vals_test = original_vals.iloc[X_test.index]

# Encode feature sets individually
encoded_X_train, ct = encode(X_train)
encoded_X_test = ct.transform(X_test)

# Initialize XGBoost regressor with some general parameters
xg_reg = xgb.XGBRegressor(objective='reg:squarederror', colsample_bytree=0.7,
                          learning_rate=0.01, max_depth=10,
                          alpha=10, n_estimators=500)

# Train the model
xg_reg.fit(encoded_X_train, y_train)

# Predictions and evaluation
preds = xg_reg.predict(encoded_X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
print(f"RMSE: {rmse}")

# Accuracy Score
#absolute value of prediction minus actual / actual



# Display original values with predictions
for i, (pred, actual) in enumerate(zip(preds, y_test)):
    country = original_vals_test.iloc[i]['employee_residence']
    job_category = original_vals_test.iloc[i]['job_category']
    job_title = original_vals_test.iloc[i]['job_title']
    pred = round(pred)
    print(f"Test Case {i + 1}: {country}, {job_category}, {job_title}\nPredict: {pred}, Actual: {actual}, ACC: {1 - (round(abs((pred-actual)/actual), 2))}\n")
    if i > 4:
        break

# Save model
joblib.dump(xg_reg, 'xgboost_model.joblib')
# Save columnTransformer
joblib.dump(ct, 'column_transformer.joblib')
