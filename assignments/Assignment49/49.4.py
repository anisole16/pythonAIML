# Confusion Matrix Sumss

actual = [1,1,1,1,0,0,0,0]

predicted = [1,1,0,1,0,1,0,0]

TP = TN = FN = FP = 0

for a , p in zip(actual , predicted):
    if a == 1 and p == 1:
        TP += 1
    if a == 0 and p == 1:
        FP += 1  
    if a == 1 and p == 0:
        FN += 1
    if a == 0 and p == 0:
        TN += 1

print("True Positive: ",TP)
print("True Negative: ", TN)
print("False Positive: ",FP)
print("False Negative: ",FN)

