#user_id='abhishek003'
#password= 'abhishek'

abhi = input("enter app name: ")
if abhi=="instagram":
    user_id=input("enter user_id: ")
    if user_id=='abhishek003':
        print("user_id match ")
        password=input("enter your password: ")
        if password=='abhishek':
            print('login successfull welcome to instagram')
        else :
            print('password did not match')
    else :
        print('userd_id did not match')
else:
    print('app did not match')