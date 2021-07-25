def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_and_days = {
        "january": 31, 
        "feburary": 28, 
        "march": 31, 
        "april": 30, 
        "may": 31, 
        "june": 30, 
        "july": 31, 
        "august": 31, 
        "september": 30, 
        "ocotober": 31, 
        "novemeber": 30, 
        "december": 31
    }
    
    statement = f"In the year {year}, there are {month_and_days[month]} days in {month.title()}."

    if month == "feburary":
        leap_year = is_leap(year)
        if leap_year:
            return f"In the year {year}, there are 29 days in {month.title()}."
        elif leap_year == False:
            return statement
    else:
        return statement


  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = input("Enter a month: ").lower()
days = days_in_month(year, month)
print(days)