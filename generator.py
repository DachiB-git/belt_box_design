# pip3 install requests
import requests

HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
# Retrieve these from https://htmlcsstoimage.com/dashboard
HCTI_API_USER_ID = '4ca005f0-183e-4480-a324-b39590bed5ce'
HCTI_API_KEY = '1bf562e1-9793-4807-9d9f-4b8a49767228'


data = { 'url': "https://dachib-git.github.io/belt_box_design/",
         'google_fonts' : "Arial|Helvetica|sans-serif",
         'ms_delay': 1000,
         'viewport_height': 1080,
         'viewport_width' : 1920
         }

image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

print("Your image URL is: %s"%image.json()['url'])
# https://hcti.io/v1/image/7ed741b8-f012-431e-8282-7eedb9910b32

