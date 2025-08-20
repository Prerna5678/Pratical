teacher=[]
student=[]
add_quest=[]
marks=[]

print("_"*70)
print("\n 1.Teacher \n 2.Student \n 0.Exit")
a=int(input("\n Enter your choice"))
b=[]
c=[]
print("_"*70) 
while True:
    if a==1:
        print("\nYour are welcome in teacher")
        print("_"*70)
        print("\n 1.login \n 2.Registration \n 0.Exit")
        b=int(input("\n Enter your choice "))
        print("_"*70)         
        if b==1:
            # Login form for teacher
            username=input("Enter your name")
            password=input("Enter your password")
            Teach_login={'username':username,'password':password}
            flag=False
            for teach in teacher:
                print(teach)
                if Teach_login==teach:
                    print("You login Sucessfully",Teach_login)
                    flag=True
                else:
                    print("Please try again",Teach_login)
                    flag=Flase
            print(teacher)
            add_quest=[]
            print("_"*70)
            # teacher option
            while flag==True:
                print("\n 1.Add Question \n 2.Update Question \n 3.Delete Question \n 4.Display Question \n 0.Exit")
                a=int(input("\n Enter your choice"))
                if a==1:
                    # Add Question
                    n=int(input("Enter the question requirement:"))
                    add_quest=[]
                    for i in range(n):
                        print("You can Add the Question")
                        print(f"\nQuestion {i + 1}:")
                        ques=input("Enter Question")
                        opt_A=input("A:")
                        opt_B=input("B:")
                        opt_C=input("C:")
                        opt_D=input("D:")
                        ans=input("answer")
                        for correct in ("A", "B", "C", "D"):
                                new_q = {
                                    "question": Que,
                                    "options": ("A."+ opt_a, "B." +opt_b, "C." +opt_c, "D." +opt_d),
                                    "answer": correct
                                }
                                question.append(new_q)
                                print("Question added successfully.")
                                print(question)
                         
                        print("_"*70)
                elif a==2:
                    # Update Question
                    print(add_quest)
                    for i in range(len(add_quest)):
                        value=input("Enter the value")
                        add_quest[i]=value
                    print(add_quest)
                    print("_"*70)   
                            
                elif a==3:
                    # Delete Question
                        print("You can Delete Question")
                        remove=int(input("Enter the question no."))
                        
                        for remove in add_quest:
                            add_quest.remove(remove)
                            print("update question",add_quest)
                            break
                        print("_"*70)   
                elif a==4:
                    # Display Question
                    for i in add_quest:
                        print(i)
                    print("_"*70)
                elif a==0:
                    # Exit
                    print("Exit")
                    break;
                    print("_"*70)
                else:
                    print("Enter proper Number")
                    print("_"*70)
        elif b==2:
            print("\nRegistration Form")
            print("_"*70)
            # Registration for teacher
            reg_username=input("Enter your name")
            reg_password=input("Enter your password")
            teacher.append({
                'username': reg_username,
                'password': reg_password
            })
            print(teacher)
            print("Your Registration sucessfully")
            print("_"*70)
        else:
            print("exit")
            print("_"*70)
    elif a==2:
        print("\n Your are welcome in student")
        print("_"*70)
        print("\n 1.login \n 2.Registration \n 0.Exit")
        c=int(input("\n Enter your choice"))
        print("_"*70)
        if c==1:
            # Login form for student
            username=input("Enter your name")
            password=input("Enter your password")
            Stud_login={'username':username,'password':password}
            flag=False
            for stud in teacher:
                print(teacher)
                if Stud_login==teach:
                    print("You login Sucessfully",Stud_login)
                    flag=True
                else:
                    print("Please try again",Stud_login)
                    flag=Flase
            print(student)
            print("_"*70)
            while flag==True:
                print("\n 1.Display Question \n 2.Result \n 0.Exit")
                a=input("Enter the choice")
                print("_"*70)
                if a==1:
                    # Display Question
                    print(add_quest)
                    print("_"*70)
                elif a==2:
                    # Result 
                    marks=add_quest/10
                    print(marks)
                    print("_"*70)
                elif a==0:
                    # Exit
                    print(exit)
                    break
                    print("_"*70)
                else:
                    print("Enter vaild no.")
                    print("_"*70)
                    flag=False
        elif c==2:
            # Registration for student
            print("\n Registration Form")
            stud_username=input("Enter your name")
            stud_password=input("Enter your password")
            student.append({
                'username': stud_username,
                'password': stud_password
            })
            print(student)
            print("Your Registration sucessfully")
            print("_"*70)
        else:
            # Exit
            print("Exit")
            print("_"*70)
    elif a==0:
        # Exit
        print("Exit")
        break
        print("_"*70)
    else:
        # Exit
        print("Exit")
        break
        print("_"*70)
