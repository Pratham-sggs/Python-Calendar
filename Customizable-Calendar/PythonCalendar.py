from printCalendar import *;
from is_layout_correct import *;

year = int(input("Enter The Year :"))
if(year <= 0 or year > 9999) :
        print("Enter Valid Year!")
else :
        layout = input("Enter layout :")
        if is_layout_correct(layout) :
                symbol = input("Enter Sepration Symbol :")
                if len(symbol) <= 4 :
                        list_of_rc = get_rows_columns_list(layout)

                        print_year(symbol,year,layout)
                        for i in range(0,list_of_rc[0]) :

                                print_month_week(symbol,layout)
                                print_dates(symbol,year,layout)
                else :
                        print("Enter Valid Symbol")
        else :
                print("Enter Valid Layout")