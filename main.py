import modules.util as util
from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import modules.predict as predict
import modules.logit as logit
import modules.visualize as visualize
import modules.auth as auth

# Reading in information to create menus from csv dynamically
menuOptions = util.readInMenuOption()
logit.customMsg('Menus Updated')

app = FastAPI()

# Handling CORS
origins = ["*"]

# log server boot
logit.customMsg('Server Boot Success')


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


class InputData(BaseModel):
    workYear: str
    # jobTitle: str
    jobCategory: str
    employeeResidence: str
    experienceLevel: str
    employmentType: str
    workSetting: str
    companyLocation: str
    companySize: str


@app.post("/predict")
async def predictSalary(input_data: InputData):
    year = int(input_data.workYear)  # conversion from str to int for model
    result = predict.makePrediction(year=year,
                                    title='Data Engineer',
                                    category=input_data.jobCategory,
                                    residence=input_data.employeeResidence,
                                    experience=input_data.experienceLevel,
                                    e_type=input_data.employmentType,
                                    setting=input_data.workSetting,
                                    c_location=input_data.companyLocation,
                                    c_size=input_data.companySize)
    prediction = str(round(result[0]))
    response = {"prediction": prediction}
    return response


@app.get("/workYear")
def yearOption():
    menuOptions = util.readInMenuOption()
    yearList = menuOptions['work_year']
    yearList.remove(2020)
    yearList.remove(2021)
    yearList.remove(2022)
    yearList.append(2024)
    yearList.append(2025)
    yearList.sort()
    return yearList


@app.get("/jobTitle")
def jobTitle():
    try:
        titles = 'Data Engineer'
        titles.sort()
        return titles
    except (Exception):
        logit.error('Exception')


@app.get("/jobCategory")
def jobCategory():
    try:
        categories = menuOptions['job_category']
        categories.sort()
        return categories
    except (Exception):
        logit.error('Exception')


@app.get("/employeeResidence")
def employeeResidence():
    try:
        residence = menuOptions['employee_residence']
        residence.sort()
        return residence
    except (Exception):
        logit.error('Exception')


@app.get("/experienceLevel")
def experienceLevel():
    try:
        experience = menuOptions['experience_level']
        experience.sort()
        return experience
    except (Exception):
        logit.error('Exception')


@app.get("/employmentType")
def employmentType():
    try:
        eType = menuOptions['employment_type']
        eType.sort()
        return eType
    except (Exception):
        logit.error('Exception')


@app.get("/workSetting")
def workSetting():
    try:
        setting = menuOptions['work_setting']
        setting.sort()
        return setting
    except (Exception):
        logit.error('Exception')


@app.get("/companyLocation")
def companyLocation():
    try:
        location = menuOptions['company_location']
        location.sort()
        return location
    except (Exception):
        logit.error('Exception')


@app.get("/companySize")
def companySize():
    try:
        cSize = menuOptions['company_size']
        cSize.sort()
        return cSize
    except (Exception):
        logit.error('Exception')


@app.get("/locationVsalary")
async def api_location_v_salary(company_location: str, predicted_salary: str):
    predicted_salary = int(predicted_salary)
    # Get the image buffer
    image_buffer = visualize.locationVsalary(company_location, predicted_salary)
    # Return the image as bytes
    return Response(content=image_buffer.read(), media_type="image/png")


@app.get("/salaryDistrib")
async def api_salary_distrib(predicted_salary: str):
    predicted_salary = int(predicted_salary)
    # Get the image buffer
    image_buffer = visualize.salaryDistrib(predicted_salary)
    # Return the image as bytes
    return Response(content=image_buffer.read(), media_type="image/png")


@app.get("/categoryVusd")
async def api_category_v_usd(category: str, predicted_salary: str):
    predicted_salary = int(predicted_salary)
    # Get the image buffer
    image_buffer = visualize.categoryVusd(category, predicted_salary)
    # Return the image as bytes
    return Response(content=image_buffer.read(), media_type="image/png")


@app.get("/getLogs")
def logs(request: Request):
    with open('./logs/apiActivity.txt', 'r') as file:
        logInfo = file.read()
        return logInfo


@app.get("/login")
def login(request: Request):
    userName = request.headers.get('userName')
    passCode = request.headers.get('passCode')
    if auth.guest(userName, passCode):
        return {'status': 0}
    else:
        return {'status': 1}


# AutoStart Uvicorn to serve backend
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
