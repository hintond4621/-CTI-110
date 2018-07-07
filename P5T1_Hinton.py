#CTI-110
#P5T1-Kilometer Converter
#Debbie Hinton
#July 7, 2018


Conversion_Formula = 0.6214

def main():
    kilometers = float(input('Enter the distance in kilometers: '))
    show_miles(kilometers)
    
def show_miles(km):
    
    miles = km * Conversion_Formula
    
    print(km, 'kilometers equal', miles, 'miles.' )

main()

