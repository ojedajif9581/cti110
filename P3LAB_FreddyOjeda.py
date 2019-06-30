# I was supposed to put a comment here
# My OJEDA FREDDY
def main():
# This program takes a number grade and outputs a letter grade.
# System uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    F_score = 60
# TO DO: define the rest of the scores
score = input('Enter grade: ')

if score >= '90':
    print('Your grade is: A')
elif score >= '80':
    print('Your grade is: B')
elif score >= '70':
    print('Your grade is: C')
elif score <= '60':
    print('Your grade is: F')
main()
