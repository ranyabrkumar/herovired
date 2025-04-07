# #===========================================================================================================================
# In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the strength of the password. 

#       ●       Implement a Python function called check_password_strength that takes a password string as input.
      
#       ●       The function should check the password against the following criteria:
      
#               ○       Minimum length: The password should be at least 8 characters long.
              
#               ○       Contains both uppercase and lowercase letters.
              
#               ○       Contains at least one digit (0-9).
              
#               ○       Contains at least one special character (e.g., !, @, #, $, %).
      
#       ●       The function should return a boolean value indicating whether the password meets the criteria.
      
#       ●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.
      
#       ●       Provide appropriate feedback to the user based on the strength of the password.  
#================================================================================================================================
'''Function to check whether the password entered is strong or not
    Argument: password
    Return: Whether password is strong or not [bool value]
'''
def check_password_strength(password):
    len_of_password=len(password)
    minLength=8
    isUCPresent=False
    isLCPresent=False
    isDigitPresent=False
    isSpecialCharPresent=False
    isStrong=False
    for char in password:                   # Looping through each character of password  
        if char.islower():                  #Checking if the char is lowercase     
            isLCPresent=True
        if char.isupper():                  #Checking if the char is uppercase  
            isUCPresent=True
        if char.isdigit():                  #Checking if the char is a digit  
            isDigitPresent=True
        if not char.isalnum():              #Checking if the char is not a alpha numeric  
            isSpecialCharPresent=True
        if ' ' in password:
            isSpacePresent=True
    if len_of_password>=minLength and isDigitPresent and isLCPresent and isUCPresent and isSpecialCharPresent and not isSpacePresent:
        print ("Password is strong")
        isStrong=True
    else:
        print("Please enter a strong password. ")
        if len_of_password<minLength:
            print("ERROR: Password should have minimun 8 characters")
        if not isDigitPresent:
            print("ERROR: Password should have atleast a digit")
        if not isLCPresent:
            print("ERROR: Password should have atleast a lowercase letter")
        if not isUCPresent:
            print("ERROR: Password should have atleast a uppercase letter")
        if not isSpecialCharPresent:
            print("ERROR: Password should have atleast a specialcase letter")
        if isSpacePresent:
            print("ERROR: Password shouldnot have conatin emptyspace")
    return isStrong

if __name__ == "__main__":
    password=input("Enter the password: ")
    check_password_strength(password)

