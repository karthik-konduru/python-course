#if elif conditonal Statement
# Correct Priority Order
marks=int(input())
if marks>=90:
    print('A Grade')
elif marks>=75:
    print('B Grade')
elif marks>=50:
    print('C Grade')
elif marks>=35:
    print('D Grade')
else:
    print('Fail')
## Suppose Priority Order Changes
marks=int(input())
if marks>=35:
    print('A Grade')
elif marks>=50:
    print('B Grade')
elif marks>=75:
    print('C Grade')
elif marks>=90:
    print('D Grade')
else:
    print('Fail') # Output comes without error but values is wrong because Condition priority order is wrong
