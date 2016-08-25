__author__ ='Griffin Barath'
def main():
    score = float(input("Enter score: "))
    score = validateScore(score)
    print(score)

def validateScore(score):
    if score < 0 or score > 100:
        grade = "Invalid score"
    elif score > 90:
        grade = "Excellent"
    elif score > 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade

main()