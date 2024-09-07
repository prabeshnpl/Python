import re

pattern_gmail = re.compile(r'^[a-zA-Z0-9._%+-]+@gmail\.com$')
pattern_password =re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$')

while True:
    gmail=input('Enter you gmail id: ')
    gmail_truth = pattern_gmail.search(gmail)
    if gmail_truth == None:
        print("enter valid gmail.")
        continue
    else:
        while True:
            password=input('\n\t\tConditions\n\ni)   At least one upper and lower case each\nii)  At least one special character\niii) At least one number\niv) 8-12 characters\n\nEnter your new password: ')
            password_truth = pattern_password.search(password)
            if password_truth == None: 
                print('Please enter valid password')
            else:
                print('\nThank you for your registration .\n\n',gmail_truth.group(),'\n','*'*len(password_truth.group()))
                break
        break