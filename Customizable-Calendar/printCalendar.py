from day import get_week_day;
from maximumnumberofdays import maxm_days_in_month;
from get_number_of_rowsandcolumns import get_rows_columns_list;

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