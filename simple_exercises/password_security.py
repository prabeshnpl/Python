import requests
import hashlib


def fetching_api_hashes(query_char):
    try:
        url = 'https://api.pwnedpasswords.com/range/' + query_char
        res = requests.get(url)
        if res.status_code != 200:
            raise RuntimeError(
                f'Error fetching {res.status_code}.Please check the API')
        else:
            return res
    except RuntimeError as err:
        return err


def sha_1_converter(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()


def prowned(password):
    sha1_hash1 = sha_1_converter(password)
    first5, last = sha1_hash1[:5], sha1_hash1[5:]
    hashes = fetching_api_hashes(first5)
    count = hashes.text.count('\n')

    splitted = (lines.split(':') for lines in hashes.text.split('\n'))

    for start , end in splitted:
        if start == last:
            return int(end)
    return 0 

 
password_list = (input('\nEnter all the passwords(separated by space) to check.\n(Press enter after entering all passwords) \n : ')).split(' ')

for password in password_list:
    times = prowned(password)
    if times:
        print(f'\nYour password = {password} has been hacked {times} times. You should change it..')
    else:
        print(f'\nCongratulations!!! Your password = {password} has never been hacked . You are ready to go!!')