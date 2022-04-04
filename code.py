p2 = input("What did you get in MCQ? (paper 2 is out of 40) :")
p4 = input("What did you get in Theory? (paper 4 is out of 80) :")

def cal(p2,p4):
    wp2 = int(p2) * 1.5
    wp4 = int(p4) * 1.25
    total = wp4 + wp2
    percent = (total/160) *100
    print(f"Your total marks out of 160 are: {total}")
    print(f"As a percentage: {percent}")
    if percent > 95:
        print("Great job!")
cal(p2,p4)
