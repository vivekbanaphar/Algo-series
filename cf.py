from NorenRestApiPy.NorenApi import NorenApi
import logging
import yaml
import pyotp

# Enable debug to see requests and responses
logging.basicConfig(level=logging.ERROR)

class ShoonyaApiPy(NorenApi):
    def __init__(self):
        # Initialize NorenApi with the correct host URL
        NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/', 
                          websocket='wss://api.shoonya.com/NorenWSTP/')

# Start of our program
api = ShoonyaApiPy()  # Initialize the ShoonyaApiPy instance

# Load credentials from YAML file
with open('cred.yml', 'r') as file:
    creds = yaml.safe_load(file)

# Extracting credentials
token = creds['token']
otp = pyotp.TOTP(token).now()  # Generate OTP using the token

# Credentials
uid = creds['user']
pwd = creds['pwd']
factor2 = otp  # 2FA factor
vc = creds['vc']
app_key = creds['apikey']
imei = creds['imei']

# Make the API call
ret = api.login(userid=uid, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)

# Check login success
if ret.get('stat') == 'Ok':
    print('Login Successful')
else:
    print('Login Failed:', ret)  # If you want to see the error response
#print(dir(api))
