#CTI-110
#P3HW1-Age Classifier
#Debbie Hinton
#June 22, 2018

def main():

    userage=int(input('Please enter your age:'))
    
    if userage <=1:
         print('You are an infant')

    elif userage <13:
        print ('You are a child')

    elif userage <20:
        print ('You are a teenager')

    else:
        print ('You are an adult')

main()
