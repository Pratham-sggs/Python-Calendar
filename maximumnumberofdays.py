from isLeapYear import is_leap_year;

def maxm_days_in_month(month,year) :
    list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    list_of_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if(month=="February"):
        if(is_leap_year(year)):
            return 29;
        return 28;
    return int(list_of_days[list_of_months.index(month)])