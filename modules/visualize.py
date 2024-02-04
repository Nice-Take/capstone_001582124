import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import BytesIO


def showNow(dataFrame):
    df = dataFrame

    # Histogram/Density Plot for Target Variable (Salary)
    plt.figure(figsize=(10, 6))
    sns.histplot(df['salary_in_usd'], kde=True)
    plt.title('Distribution of Salary in USD')
    plt.xlabel('Salary in USD')
    plt.ylabel('Frequency')
    plt.show()

    # Count Plot for a Categorical Variable (e.g., Job Category)
    plt.figure(figsize=(10, 6))
    sns.countplot(y='job_category', data=df)
    plt.title('Frequency of Job Categories')
    plt.xlabel('Count')
    plt.ylabel('Job Category')
    plt.show()

    # Bar Plot for Year vs Average Salary
    plt.figure(figsize=(10, 6))
    sns.barplot(x='work_year', y='salary_in_usd',
                data=df, estimator=np.mean, ci=None)
    plt.title('Average Salary in USD by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Salary in USD')
    plt.show()

    # Box Plot for Company Location vs Salary
    plt.figure(figsize=(18, 8))
    sns.boxplot(x='company_location', y='salary_in_usd', data=df)
    plt.title('Salary in USD by Company Location')
    plt.xlabel('Company Location')
    plt.ylabel('Salary in USD')
    current_label_size = plt.xticks()[1][0].get_fontsize()
    plt.xticks(rotation=45, fontsize=current_label_size / 1.8)
    plt.xticks(rotation=90)  # Rotate the x labels for better readability
    plt.show()

    # Box Plot for job_category vs Salary
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='job_category', y='salary_in_usd', data=df)
    plt.title('Salary in USD by Job Category')
    plt.xlabel('Job Category')
    plt.ylabel('Salary in USD')
    current_label_size = plt.xticks()[1][0].get_fontsize()
    plt.xticks(rotation=45, fontsize=current_label_size / 1.8)
    plt.xticks(rotation=33)  # Rotate the x labels for better readability
    plt.show()


def categoryVusd(category: str, predicted_salary: int):
    plt.figure(figsize=(8, 8))
    sns.boxplot(x='job_category', y='salary_in_usd', data=df)
    category_list = df['job_category'].unique()
    category_position = list(category_list).index(category)
    plt.scatter(category_position, predicted_salary, color='red', s=200, label=f'Predicted Value: {predicted_salary}')
    plt.title('Salary in USD by Job Category')
    plt.xlabel('Job Category')
    plt.ylabel('Salary in USD')
    current_label_size = plt.xticks()[1][0].get_fontsize()
    plt.xticks(rotation=45, fontsize=current_label_size / 1.8)
    plt.xticks(rotation=33)
    # plt.show()
    # creating buffer to send to client
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf


def salaryDistrib(predicted_salary: int):
    plt.figure(figsize=(8, 8))
    sns.histplot(df['salary_in_usd'], kde=True)
    plt.axvline(x=predicted_salary, color='red', linestyle='dashdot', linewidth=2, label=f'Predicted Value: {predicted_salary}')
    plt.legend()
    plt.title('Distribution of Salary in USD')
    plt.xlabel('Salary in USD')
    plt.ylabel('Frequency')
    # plt.show()
    # creating buffer to send to client
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf


def locationVsalary(company_location: str, predicted_salary: int):
    zoom_margin = 6
    plt.figure(figsize=(8, 8))
    sns.boxplot(x='company_location', y='salary_in_usd', data=df)
    # Find the position of the company location on the x-axis
    location_list = df['company_location'].unique()
    location_position = list(location_list).index(company_location)
    # Add a red dot for the predicted salary at the specified company location
    plt.scatter(location_position, predicted_salary, color='red', s=200)
    # Calculate the zoom range, ensuring it stays within the bounds of the plot
    left_limit = max(location_position - zoom_margin, 0)
    right_limit = min(location_position + zoom_margin + 1, len(location_list))
    plt.xlim(left_limit, right_limit)
    plt.title('Salary in USD by Company Location')
    plt.xlabel('Company Location')
    plt.ylabel('Salary in USD')
    plt.xticks(rotation=33)  # Rotate the x labels for better readability
    #plt.show()
    # creating buffer to send to client
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf


df = pd.read_csv('./jobs_in_data.csv')
