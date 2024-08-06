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


def print_dates(year) :
    global ongoing_literal;
    list_of_day = ["Sunday", "Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    date_of_first_month = 1;
    date_of_second_month = 1;
    date_of_third_month = 1;
    day_on_first_month = list_of_day.index(get_week_day(ongoing_literal-3,year))
    day_on_second_month = list_of_day(get_week_day(ongoing_literal-2,year))
    day_on_third_month = list_of_day.index(get_week_day(ongoing_literal-1,year))
    literal1=day_on_first_month
    literal2=day_on_second_month
    literal3=day_on_third_month
    space1 = 1;
    space2 = 1;
    space3 = 1;
    maximum_days_first_month = maxm_days_in_month(list_of_months[ongoing_literal-3],year)
    maximum_days_second_month = maxm_days_in_month(list_of_months[ongoing_literal-2],year)
    maximum_days_third_month = maxm_days_in_month(list_of_months[ongoing_literal-1],year)

    while(maximum_days_first_month or maximum_days_second_month or maximum_days_third_month) :


        # To print first line of the first month of the row
        if(maximum_days_first_month) :
            for i in range (0,7-day_on_first_month) :
                print(" "*(literal1*3) + " "*space1 + str(date_of_first_month) + " ",end="")
                if i == 0 :
                    literal1 = 0;
                date_of_first_month += date_of_first_month;
                if  len(str(date_of_first_month) == 2) :
                    space1 = 0;
                if maximum_days_first_month+1 == date_of_first_month :
                    maximum_days_first_month = 0;
        

        #to print first line of the second month of row 
        if (maximum_days_second_month) :
            for i in range (0,7-day_on_second_month) :
                print(" "*(literal2*3) + " "*space2 + str(date_of_second_month) + " ",end="")
                if i == 0 :
                    literal2 = 0;
                date_of_second_month += date_of_second_month;
                if  len(str(date_of_second_month) == 2) :
                    space2 = 0;
                if maximum_days_second_month+1 == date_of_first_month :
                    maximum_days_second_month = 0;
        else :
            
        

        if(maximum_days_third_month) :
            #to print first line of the third month of row 
            for i in range (0,7-day_on_third_month) :
                print(" "*(literal3*3) + " "*space3 + str(date_of_third_month) + " ",end="")
                if i == 0 :
                    literal3 = 0;
                date_of_third_month += date_of_third_month;
                if  len(str(date_of_third_month) == 2) :
                    space2 = 0;
                if maximum_days_third_month+1 == date_of_first_month :
                        maximum_days_second_month = 0;
        print(" "); # to break the end="" in last print