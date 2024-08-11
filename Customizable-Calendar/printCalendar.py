from day import get_week_day;
from maximumnumberofdays import maxm_days_in_month;
from get_number_of_rowsandcolumns import get_rows_columns_list;

ongoing_month = 0;
month = 1

week_layout = "  Su Mo Tu We Th Fr Sa  "
list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def print_year(symbol,year,layout) :
    list_of_rc = get_rows_columns_list(layout);
    spaces = 24*list_of_rc[1] + len(symbol)*(list_of_rc[1]-1) - len(str(year));
    print(symbol + symbol*((24*list_of_rc[1]//len(symbol))+(list_of_rc[1]-1)) + symbol)
    print(symbol + " "*len(symbol)*((24*list_of_rc[1]//len(symbol))+(list_of_rc[1]-1)) + symbol)

    print(symbol + " "*(spaces//2) + str(year) +  " "*(spaces-(spaces//2))  + symbol)
    
    print(symbol + " "*len(symbol)*((24*list_of_rc[1]//len(symbol))+(list_of_rc[1]-1)) + symbol)
    print(symbol + symbol*((24*list_of_rc[1]//len(symbol))+(list_of_rc[1]-1)) + symbol)


def print_month_week (symbol,layout) :

    global ongoing_month ;
    list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    list_of_rc = get_rows_columns_list(layout)
    column_count = 1
    for i in range (0,list_of_rc[1]) :
        print(symbol*column_count + " "*24 + symbol,end="")
        if i == 0 :
            column_count =0
    print("")

    
    column_count = 1
    for a in range(0,list_of_rc[1]) :
        
        length_of_month = len(list_of_months[ongoing_month])
        first_spaces = (24-length_of_month) // 2;
        second_spaces = 24 - first_spaces - length_of_month;
        print(symbol*column_count + " "*first_spaces + list_of_months[ongoing_month] + " "*second_spaces + symbol,end="")
        if a == 0 :
            column_count= 0;
        ongoing_month = ongoing_month + 1;
    print("")



    column_count = 1
    for a in range(0,list_of_rc[1]) :
        print(symbol*column_count + "  Su Mo Tu We Th Fr Sa  " + symbol,end="")
        if a == 0 :
            column_count = 0;
    print("")

def print_dates (symbol,year,layout) :
    global month;
    column_count = 1
    list_of_rc = get_rows_columns_list(layout)
    list_of_day = ["Sunday", "Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    day_of_week = (list_of_day.index(get_week_day(1,month,year)))

    for i in range (0,list_of_rc[1]) :
        print(symbol*column_count + "  " + " "*3*day_of_week + " " + symbol,end="");
        if i == 0 :
            column_count = 0;
    print("");





















print_year("----",2024,"4x3")
print_month_week("----","4x3")
print_dates("----",2024,"4x3")