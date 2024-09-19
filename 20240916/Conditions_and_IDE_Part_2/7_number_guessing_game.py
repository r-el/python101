import random

random_number = random.randint(1, 100)
attempts = 3

print("ברוך הבא למשחק הניחושים! יש לך 3 ניסיונות לנחש את המספר בין 1 ל-100.")

while attempts > 0:
    guess = int(input("הכנס את הניחוש שלך: "))
    
    if guess == random_number:
        print("כל הכבוד! ניחשת את המספר הנכון!")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print(f"נגמרו לך הניסיונות. המספר הנכון היה {random_number}.")
        else:
            if guess > random_number:
                print("המספר שלך גדול מדי.")
            else:
                print("המספר שלך קטן מדי.")
            
            if attempts == 2:
                if random_number % 2 == 0:
                    print("רמז: המספר הוא זוגי.")
                else:
                    print("רמז: המספר הוא אי זוגי.")
            elif attempts == 1:
                if random_number < 10:
                    print("רמז: המספר הוא רק אחדות.")
                else:
                    print(f"רמז: הספרה האחרונה של המספר היא {random_number % 10}.")

print("תודה ששיחקת!")