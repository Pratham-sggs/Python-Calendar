def get_week_day(date,month,year) :
    #Here We are calculating Year using Zeller’s Congruence

    if month == 1 :
        month = 13;
        year = year - 1;
    if month == 2 :
        month = 14
        year = year - 1;
    last_two_digit_of_year = year%100
    first_two_digit_of_year = year//100;

    day = (date+((13*(month+1))//5)+last_two_digit_of_year+(last_two_digit_of_year//4)+(first_two_digit_of_year//4)+5*first_two_digit_of_year)
    day = day%7;
    list=["Saturday", "Sunday", "Monday", "Tuesday","Wednesday","Thursday","Friday"]
    return list[day] # we are returning the string name of the day on the specific date