# Given scores of two students in the class a, b, the teacher want to check if these students can be sent to same class. They can be sent to same class if the difference between their scores is <=10.
# Print "YES" if they can be sent to same class else "NO".
# Input

a= int(input());
b= int(input());
check1 = a-b;
check2 = abs(check1);

if check2 <= 10:
    print("YES");
else: 
    print("NO");