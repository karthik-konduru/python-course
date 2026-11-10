import random
roll=0
count=0
while True:
    input('click Enter to throw dice')
    dice=random.randint(1,6)
    print(f'Current dice value {dice}')
    if count+dice<=100:
        count+=dice
    roll+=1
    if count==100:
        print(f' You reached  the top in {roll} rolls')
        break
    print(f' For {roll} rolls you are at {count} position')