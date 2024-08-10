from day import get_week_day;
from maximumnumberofdays import maxm_days_in_month;

def print_upper_box (symbol,year,layout) :
        length = len(str(year))
        const=0
        if(length%2==1) :
                const = 1
        print(symbol*((layout*25)-5));
        print(symbol+ " "*((layout*25)-7) +symbol);
        print(symbol+ " "*(((layout*25)-7)//2-(length//2)-(const)) + str(year) + " "*(((layout*25)-7)-(((layout*25)-7)//2)-(length//2)) +symbol);
        print(symbol+ " "*((layout*25)-7) +symbol);
        print(symbol*((layout*25)-5))

print_upper_box("'",32525,3)