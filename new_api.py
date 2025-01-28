import requests

def post_to_ehb_api(data_dict):
    pass

def number_is_blacklist(phone_number):
    version = 'v3'
    apikey = 'RXHTgDMWkbBVFag4Ex96'
    response = 'json'
    phone = phone_number

    blacklist_uri = f'https://api.blacklistalliance.net/standard/api/{version}/Lookup/key/{apikey}/phone/{phone}/response/{response}'


    headers = {"accept": "application/json"}

    response = requests.get(blacklist_uri, headers=headers)
    if (response.status_code) == 200:
        return (response.json()['message']!='Good')



def is_duplicate(phone_number):
    duplicate_uri = f"https://ehbportal.herokuapp.com/checkDuplicateLeadsData/{phone_number}/"
    response = requests.get(duplicate_uri)
    print('____________________________________________________')
    if 'DUPLICATE' in response.text:
        return True
    else:    
        return False


# print(is_duplicate('2147999203'))
# 7183448888
# print(number_is_not_blacklist('9176597909'))