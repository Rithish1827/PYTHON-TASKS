def pass_fail(total):
    average=total/5
    if sub1<33 or sub2<33 or sub3<33 or sub4<33 or sub5<33 or average<40:
        return "Fail"
    else:
        return "Pass"
    
sub1=int(input("Enter marks of subject 1: "))   
sub2=int(input("Enter marks of subject 2: "))
sub3=int(input("Enter marks of subject 3: "))
sub4=int(input("Enter marks of subject 4: "))
sub5=int(input("Enter marks of subject 5: "))
total=sub1+sub2+sub3+sub4+sub5
result=pass_fail(total)
print("Total marks:", total)
print("Result:", result)