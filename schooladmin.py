import csv
print("Welcome to SchoolHandler")
n = input("Please enter your Name: ")
print("Welcome " +n)

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        

        if csv_file.tell() == 0: 
            writer.writerow(["Name", "Age", "Cont Num", "Emai Id"])
       

            writer.writerow(info_list)


if __name__=='__main__':
    cond = True

    while(cond):
        stu_i = input("Enter info in the format (Name Age Cont_Num Email_ID): ")
        print("Entered Info: " +stu_i)

        stu_i_l = stu_i.split(' ')
        print("Entered split up info is: " + str(stu_i_l))
        

        print("\nThe entered info is -\nName: {}\nAge: {}\nCont_Num: {}\nEmail_ID: {}"
                .format(stu_i_l[0], stu_i_l[1], stu_i_l[2], stu_i_l[3]))

        choice_check = input("Is it correct (y/n): ")
        if choice_check == "yes":
            write_into_csv(stu_i_l)

        cond_check = input("Do you want to continue (y/n): ")
        if cond_check == "y":
            cond = True
        elif cond_check == "n":
            cond = False
            print("Thank you for using SchoolHandler")
