from day import get_week_day;
from maximumnumberofdays import maxm_days_in_month;
from get_number_of_rowsandcolumns import get_rows_columns_list;

ongoing_month = 0;
month_number = [];
month = 1;

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

def print_dates(symbol, year, layout):
    date_of_months = []
    global month
    symbol_true = True
    spaces = []
    maxm_days_in_month_number = []
    
    list_of_months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    list_of_rc = get_rows_columns_list(layout)
    list_of_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    for i in range(list_of_rc[1]):
        maxm_days_in_month_number.append(maxm_days_in_month(list_of_months[i + month-1], year))
        spaces.append(list_of_day.index(get_week_day(1, i + month, year)))
        date_of_months.append(1)

    while any(maxm_days_in_month_number):
        for i in range(list_of_rc[1]):
            if maxm_days_in_month_number[i] != 0:
                if i == 0:
                    symbol_true = True
                else:
                    symbol_true = False
                print(symbol * symbol_true + "  " + "   " * spaces[i], end="")
                for k in range(7 - spaces[i]):
                    day_str = str(date_of_months[i]).rjust(2)
                    print(day_str + " ", end="")
                    date_of_months[i] += 1
                    if date_of_months[i] > maxm_days_in_month_number[i]:
                        maxm_days_in_month_number[i] = 0
                        print(" " * ((6 - k) * 3), end="")
                        break
                
                # Reset symbol_true for next iteration
                symbol_true = False
                print(" " + symbol, end="")
                spaces[i] = 0
            else:
                if i == 0 :
                    print(symbol + " " * 24 + symbol,end="")
                else :
                    print (" "*24 + symbol , end="")
        
        print("")
        symbol_true = False
    for i in range (0,list_of_rc[1]) :
        if i == 0 :
            print(symbol + " "*24 + symbol,end="");
        else :
            print(" "*24 + symbol,end="")
    print("");
    print(symbol + symbol * ((24 * list_of_rc[1] // len(symbol)) + (list_of_rc[1] - 1)) + symbol)
    month += list_of_rc[1]