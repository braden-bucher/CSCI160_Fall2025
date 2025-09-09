cloudTemp = int (input ("Enter cloud temp in C (no units): "))
tempAloft = int (input ("Enter temp aloft in C (no units): "))
surfaceTemp = int (input ("Enter surface temp in C (no units): "))
if (0 <= cloudTemp <= 50 and 1 <= tempAloft <= 50 and 1 <= surfaceTemp <= 50):
    print ("Rain!")
elif (-10 < cloudTemp <= -5 and 5 < tempAloft <= 15 and -10 < surfaceTemp <= 0):
    print ("Freezing Rain!")
elif (-15 < cloudTemp <= -10 and -5 <= tempAloft <= 5 and -10 <= surfaceTemp <= -5):
    print ("Sleet!")
elif (-25 <= cloudTemp <= -15 and -20 <= tempAloft <= -10 and -15 <= surfaceTemp <= -5):
    print ("Snow!")
else:
    print ("Your guess is as good as mine!")
#Tune for edge values