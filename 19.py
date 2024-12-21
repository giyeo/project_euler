#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
numberToDays = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

leap_years = []
for year in range(1899, 2001):
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		leap_years.append(year)

def getDaysGivenMonthAndYear(month, year):
	if year in leap_years:
		if month == 2:
			return numberToDays[2] + 1
	return numberToDays[month]

days_of_week = ["Tue","Wed","Thu","Fri","Sat","Sun","Mon"] #i know that 1/1/1901 is a tuesday

def days_from_to_starting_at_01_01_1900(target_day, target_month, target_year):
	day = 1
	month = 1
	year = 1901

	day_count = 0
	count_sundays_in_jan = 0
	while year != target_year or month != target_month or day != target_day:
		if day > getDaysGivenMonthAndYear(month, year):
			day = 1
			month += 1
			if month > 12:
				month = 1
				year += 1
		else:
			if(day == 1 and days_of_week[day_count % 7] == "Sun"):
				count_sundays_in_jan += 1
			day += 1
			day_count += 1
			
			
		
	print(day_count)
	print(days_of_week[day_count % 7])
	print(count_sundays_in_jan)


days_from_to_starting_at_01_01_1900(31,12,2000)

