from ..config import Config

class Auth:
    def verify_token(self,access_token):
        if access_token == Config.API_SECRET_KEY:
            return True
        elif access_token != Config.API_SECRET_KEY:
            return False

Auth = Auth()
