from datetime import datetime as dt
"""
Hi Candidate,
Please find below our coding exercise. You can use whatever programming language you 
feel most comfortable in (replace “Python datetime” with whatever the native object 
is in the language to express a Date & Time). Given the attached CSV data file, write 
a function find_open_restaurants(csv_filename, search_datetime) which takes as 
parameters a filename and a Python datetime object and returns a list of restaurant 
names which are open on that date and time. Optimized solutions are nice, but 
correct solutions are more important!

Assumptions:
* If a day of the week is not listed, the restaurant is closed on that day
* All times are local — don’t worry about timezone-awareness
* The CSV file will be well-formed
If you have any questions, let me know. Submit your solution as a ZIP file at the link below.
Rod.
"""

CSV_NAME = 'rest_hours.csv'

def parse_datetime(dt_string):
    """
    dt_string will be in form:
    Mon, Wed-Fri 11am - 6:30 pm 
    Mon-Thu, Sun 11 am - 10 pm
    Sun 12 pm - 10 pm
    Mon-Sun 11:30 am - 9 pm
    -hours are in 12h fmt not always in colon fmt
    """
    if dt_string[4] == "," and dt_string[8] == '-': 
        #case: Mon, Wed-Fri[...]
        range_second_case(dt_string)
    elif dt_string[7] == ',' and dt_string[3] == '-': 
        #case: Mon-Fri, Sat[...]
        range_first_case(dt_string)
    elif dt_string[4] == ' ': 
        #case: Mon [...]
        single_day_case(dt_string)
    else: 
        #case: Mon-Fri [...]
        single_range_case(dt_string)

def range_second_case(dt_string):
    assert dt_string[4] == ',' and dt_string[8] == '-'

def range_first_case(dt_string):
    assert dt_string[7] == ',' and dt_string[3] == '-'

def single_day_case(dt_string):
    assert dt_string[4] == ''

def single_range_case(dt_string):
    assert dt_string[3] == '-' and dt_string[7] == ' '
    datetime_object = dt.strptime(dt_string, '%a-%a %I %p - ')

def parse_csv(csv_filename):
    open_adjacency_list = dict()
    for line in open(csv_filename):
        try:
            name, open_hours = line[:-1].split('","')
            open_adjacency_list[name[1:]] = open_hours[:-1].split(' / ')
        except:
            print("errored on line: {}".format(line))
    return open_adjacency_list

def find_open_restaurants(csv_filename, search_datetime):
    pass

parse_csv(CSV_NAME)
