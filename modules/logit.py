from datetime import datetime


def customMsg(message: str):
    now = datetime.now()
    with open('./logs/apiActivity.txt', 'a') as file:
        current_time = now.strftime("%H:%M:%S")
        message = 'MSG   |  ' + current_time + '  |  ' + message+'\n'
        file.write(message)


def warn(message: str):
    now = datetime.now()
    with open('./logs/apiActivity.txt', 'a') as file:
        current_time = now.strftime("%H:%M:%S")
        message = 'WARN  |  ' + current_time + '  |  ' + message+'\n'
        file.write(message)


def error(message: str):
    now = datetime.now()
    with open('./logs/apiActivity.txt', 'a') as file:
        current_time = now.strftime("%H:%M:%S")
        message = 'ERROR |  ' + current_time + '  |  ' + message+'\n'
        file.write(message)
