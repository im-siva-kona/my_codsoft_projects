#using random module to generate a random password
import random 

#function to create a random passwornd of user given length
def generate_password(len):
    
        pass_chars= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

        possible_password= random.sample(pass_chars, len)

        
        your_password= "".join(possible_password)
        

        return your_password

   
#input for length of password
len = int(input("Enter the length of password you want:"))


your_password= generate_password(len)



#display the password
print("Your Password is:",your_password) 
