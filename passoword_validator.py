import random

punctuation_signs = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

uppercaseLetter=chr(random.randint(65,90)) 


uppercaseLetter2=chr(random.randint(65,90)) 



lowercaseLetter = chr(random.randint(97, 122))


lowercaseLetter2 = chr(random.randint(97, 122))


digit1 =  chr(random.randint(48, 57))

digit2 =  chr(random.randint(48, 57))
 
random_punctuation = random.choice(punctuation_signs)

print(random_punctuation)



def random_passoword():
    return uppercaseLetter + uppercaseLetter2 + lowercaseLetter + lowercaseLetter2 + digit1 + digit2 + random_punctuation



print(random_passoword())


















# password = input('Enter a password')


 

 
