from day import get_week_day;
from isLeapYear import is_leap_year;
from maximumnumberofdays import maxm_days_in_month;

ongoing_literal = 0; #defining global variable to keep track of ongoing month
ongoing_line=3;     #defining global variable to keep track of ongoing line means ongoing month for 3x4 layout



def print_layout() :


    global ongoing_literal;
    global ongoing_line;
    list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    string_of_Week = "Su Mo Tu We Th Fr Sa      "
    layout_size = 3;

    #while loop to print layout means to print months name
    while ongoing_literal < ongoing_line :
        length_of_month = len(list_of_months[ongoing_literal])
        first_spaces = (20-length_of_month) // 2;
        last_spaces = 20-first_spaces-length_of_month;
        print(" "*first_spaces + list_of_months[ongoing_literal] + " "*last_spaces + " "*6,end="")
        ongoing_literal +=1;
    

    ongoing_line = ongoing_line + layout_size;
    # To Break last end="" from last print in while loop
    print(); 
    # To print week days short form of 3x4 layout
    print(string_of_Week*3)



def print_year(year) :

    # to print year number at the first line centre 
    year_string = str(year)
    if(len(year_string)<=2):
        print(" "*35 + year_string);
    else :
        print(" "*34 + year_string);
    print();
    print();


def print_dates(year) :
    global ongoing_literal;
    list_of_day = ["Sunday", "Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    date_of_first_month = 1;
    date_of_second_month = 1;
    date_of_third_month = 1;
    day_on_first_month = list_of_day.index(get_week_day(ongoing_literal-2,year))
    day_on_second_month = list_of_day.index(get_week_day(ongoing_literal-1,year))
    day_on_third_month = list_of_day.index(get_week_day(ongoing_literal,year))
    literal1=day_on_first_month
    literal2=day_on_second_month
    literal3=day_on_third_month
    space1 = 1;
    space2 = 1;
    space3 = 1;
    maximum_days_first_month = maxm_days_in_month(list_of_months[ongoing_literal-3],year)
    maximum_days_second_month = maxm_days_in_month(list_of_months[ongoing_literal-2],year)
    maximum_days_third_month = maxm_days_in_month(list_of_months[ongoing_literal-1],year)
    space31 = 1;
    space32 = 1
    space33 = 1
    kount = 0;
    kount1 = 0
    kount2=0
    count1=0;
    count2=0
    count3=0

    


    while(maximum_days_first_month or maximum_days_second_month or maximum_days_third_month) :


        # To print first line of the first month of the row
        if(maximum_days_first_month) :
            for i in range (0,7-day_on_first_month) :
                kount +=1
                if kount == 1 : 
                    if "Saturday" == get_week_day(ongoing_literal-2,year) :
                        space31 = 0;
                print(" "*(literal1*3) + " "*space1 + str(date_of_first_month) + " "*space31,end="")
                count1 = i+1;
                if i == 0 :
                    literal1 = 0;
                date_of_first_month += 1;
                if  len(str(date_of_first_month))==2 :
                    space1 = 0;
                if maximum_days_first_month+1 == date_of_first_month :
                    maximum_days_first_month = 0;
                    print("   "*(6-count1),end="")
                    if(6-count1>=0) :
                        print("  ",end="")
                    break;
                if (i == (5-day_on_first_month)) :
                    space31=0
            print(" "*6,end="")
            space31 = 1;
            day_on_first_month = 0;
        else :
            print(" "*26,end="");
        

        #to print first line of the second month of row 
        if (maximum_days_second_month) :
            for i in range (0,7-day_on_second_month) :
                kount1 +=1
                if kount1 == 1 : 
                    if "Saturday" == get_week_day(ongoing_literal-1,year) :
                        space32 = 0;
                print(" "*(literal2*3) + " "*space2 + str(date_of_second_month)+ " "*space32,end="")
                count2=i+1;
                if i == 0 :
                    literal2 = 0;
                date_of_second_month += 1;
                if  len(str(date_of_second_month))==2 :
                    space2 = 0;
                if maximum_days_second_month+1 == date_of_second_month :
                    maximum_days_second_month = 0;
                    print("   "*(6-count2),end="")
                    if(6-count2>=0) :
                        print("  ",end="")
                    break;
                if i == (5-day_on_second_month) :
                    space32 =0
            print(" "*6,end="")
            space32 = 1;
            day_on_second_month = 0;
        else :
            print(" "*26,end="");
            
        

        if(maximum_days_third_month) :
            #to print first line of the third month of row 
            for i in range (0,7-day_on_third_month) :
                kount2 +=1
                if kount2 == 1 : 
                    if "Saturday" == get_week_day(ongoing_literal,year) :
                        space33 = 0;
                
                print(" "*(literal3*3) + " "*space3 + str(date_of_third_month)+ " "*space33 ,end="")
                count3=i+1
                if i == 0 :
                    literal3 = 0;
                date_of_third_month += 1;
                if  len(str(date_of_third_month))==2 :
                    space3 = 0;
                if maximum_days_third_month+1 == date_of_third_month :
                        maximum_days_third_month = 0;
                        print("   "*(6-count3),end="")
                        if(6-count3>=0) :
                            print("  ",end="")
                        break
                if i == (5-day_on_third_month) :
                    space33 = 0;
            print(" "*6,end="")
            space33 = 1;
            day_on_third_month = 0;
        print(); # to break the end="" in last print
