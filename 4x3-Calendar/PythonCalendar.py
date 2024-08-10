from printCalendar import *;

year = int(input("Enter The Year :"))
if(year <= 0 or year > 9999) :
        print("Enter Valid Year!")
else :
        print_year(year);
        for i in range (0,4) :
                print_layout();
                print_dates(year);
                print();