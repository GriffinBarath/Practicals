__author__ ='Griffin Barath'
def main():
    score = float(input("Enter score: "))
    score = validateScore(score)
    print(score)

def validateScore(grade):
    if grade < 0 or grade > 100:
        grade = "Invalid score"
    elif grade > 90:
        grade = "Excellent"
    elif grade > 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade

main()