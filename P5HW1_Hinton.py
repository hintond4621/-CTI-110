#The Test Grades function is to calculate an average and a letter grade.
#July 7, 2018
#CTI-110 P5HW1-TestAverage and Grade
#Debbie Hinton


def calc_average(test1, test2, test3, test4, test5):
    average = (test1 + test2 + test3 + test4 + test5)/5
    return average

def determine_grade(testScore):
    if (testScore > 90):
        return "A"
    elif (testScore > 80):
        return "B"
    elif (testScore > 70):
        return "C"
    elif (testScore > 60):
        return "D"
    else:
        return "F"
def whataretheScores():
    test1 = float(input('Enter test 1:'))
    test2 = float(input('Enter test 2:'))
    test3 = float(input('Enter test 3:'))
    test4 = float(input('Enter test 4:'))
    test5 = float(input('Enter test 5:'))

    return test1, test2, test3, test4, test5

def printTableOfResults( test1, test2, test3, test4, test5 ):
    print('Your average is', calc_average(test1,test2,test3,test4,test5))
    print( "Score\tLetterGrade")
    
    
    print(str( test1 ) +'\t' + determine_grade( test1 ),\
          str( test2 ) +'\t' + determine_grade( test2 ),\
          str( test3 ) +'\t' + determine_grade( test3 ),\
          str( test4 ) +'\t' + determine_grade( test4 ),\
          str( test5 ) +'\t' + determine_grade( test5 ),sep = '\n')

def main():
    test1, test2, test3, test4, test5 = whataretheScores()
    printTableOfResults( test1, test2, test3, test4, test5 )

           
main()
