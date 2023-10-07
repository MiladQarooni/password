password = input('Please define Your Passwrod: ') #str
#Define the new variable to check the every char
isLowerChar,isUpperChar,isNoneAlNumChar, isNum= False,False,False,False
if len(password)>=9 and len(password)<=16:
    for char in password:
        if char.islower():
            isLowerChar=True
        elif char.isupper():
            isUpperChar=True
        elif char.isnumeric():
            isNum=True
        elif not char.isalnum():
            isNoneAlNumChar=True
    if isNum and isNoneAlNumChar and isUpperChar and isLowerChar:
        print('Password is Valid and you can choose')
    else:
        print('Password is invalid!Please Try another!')
else:
    print('Password must be at between 9 and 16 character!!!')
