

def guest(userName: str, passCode: str):
    """Guest login"""
    if userName != "guest" or passCode != "guest":
        return False
    else:
        return True
