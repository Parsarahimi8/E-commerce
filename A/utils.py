from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *

def sen_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('6F66516F2F39436A4D6457574A59476C76655A41346371684E417938712B622B57784B614C6133775474343D')

        params = {
            'sender': '',#optional
            'receptor': phone_number,
            'message': f'کد تایید شما{code}',
            }
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)
        
        
        

class IsAdminUserMixin(UserPassesTestMixin):
     def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
    