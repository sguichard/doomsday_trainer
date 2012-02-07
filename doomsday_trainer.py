import datetime
import random
import sys

days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

def ordinal(beg,end):
    #Return a random date between two given years (inclusive)
    b=datetime.date(beg,1,1).toordinal()
    e=datetime.date(end,12,31).toordinal()
    return datetime.date.fromordinal(random.randint(b,e))

def random_date():
    #Return a random date, with preference to nearby dates
    rand = random.random()
    this_year = datetime.datetime.now().year
    if rand < 0.1:
        return ordinal(1700,2200)
    elif rand < 0.2:
        return ordinal(1900,2100)
    elif rand < 0.4:
        return ordinal(this_year - 50, this_year + 20)
    elif rand < 0.6:
        return ordinal(this_year - 2, this_year + 1)
    else:
        return ordinal(this_year, this_year)

def not_leap(year):
    if year%100==0:
        return year%400 
    else:
        return year%4 

def doomsday_century(century):
    days=[2,0,5,3]
    return days[century%4]

def doomsday_year(year,century_day):
    year=year%100
    year=(year+(year%2)*11)/2
    year=7-(year+(year%2)*11)%7
    return (year+century_day)%7

def doomsday_month(month,leap):
    if not leap:
        days=[3,28]
    else:
        days=[4,29]
    days.extend([7,4,9,6,11,8,5,10,7,12])
    return days[month-1]

def check(field,answer):
    print 'Enter the ' + field
    response='The %s is %d' % (field,answer)
    if str(answer)==raw_input():
        print 'Correct, %s\n' % response
    else:
        print 'Incorrect, the answer is %s\n' % response

def weekday(date):
    #Takes a Date object and returns the weekday number, converting to Doomsday type
    return (date.weekday()+1)%7

def doomsday_walkthrough(date):
    #Run if user guesses wrong date. Asks for date for each step
    year=date.year
    century_day=doomsday_century(year/100)
    fields=['Century Day',century_day, \
    'Year Day',doomsday_year(year,century_day), \
    'Month Day',doomsday_month(date.month,not_leap(year)), \
    'Day',weekday(date)]
    for i in range(0,8,2):
        check(fields[i],fields[i+1])

def run_test():
    date=random_date()
    print 'What day of the week is '+str(date)
    guess =raw_input()
    if guess==str(weekday(date)):
        print 'Correct! \n'
        return True
    else:
        print "\nIncorrect, let's start from the beginning"
        doomsday_walkthrough(date)
        return False

def main():
    if len(sys.argv) > 1:
        if not sys.argv[1].isdigit() or int(sys.argv[1]) < 1:
            print 'Please enter a valid number of trials as the first (and only) argument'
            return
        trials = int(sys.argv[1])
    else:
        trials = 1
    correct = 0
    for i in range(trials):
        correct += run_test()
        print 'You have answered {0} out of {1} trial(s) correctly'.format(correct, trials)

if __name__=='__main__':
    main()

