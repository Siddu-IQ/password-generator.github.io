# random password generator
# password should at least 12 character
# mixture of upper_case, lower_case, digit, character
# except < > 
while True:
    print("\nWelcome to our RANDOM PASSWORD GENERATOR\n")
    
    ui=input("Enter the length of password you want:\t")
    if ui.isdigit() and int(ui)==0:
        print("\t Length of Password can't be Zero")
    elif ui.isdigit() and int(ui)<12:
        print("\t Length of a Strong Password must be greater than or equal to 12")
    elif ui.isdigit() and int(ui)>=12:
        pLen=int(ui)
        import string as st
        pChar=st.ascii_letters+st.digits+" !\"#$%&'()*+,-./:;=?@[\]^_`{|}~"
        while True:
            password=""
            for i in range(pLen):
                import random as rn
                password+=rn.choice(pChar)
            lFlag=uFlag=dFlag=sFlag=False
            for p in st.punctuation:
                if p in password:
                    pFlag=True
                    break
            for d in st.digits:
                if d in password:
                    dFlag=True
                    break
            for u in st.ascii_uppercase:
                if u in password:     
                    uFlag=True
                    break
            for l in st.ascii_lowercase:
                if l in password:
                    lFlag=True
                    break
            if lFlag and uFlag and dFlag and pFlag:
                print('\t\t Your {} Character Password is: {}'.format(pLen,password))
                break
        break
    elif len(ui)==0:
        print("\t Please enter any Positive Integer greater than or equal to 12")
    else:
        print("\t Length of Password must be Positive Integer")
