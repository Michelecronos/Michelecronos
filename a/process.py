import csv
import tui
import visual


def read_csv_file(file_path):
    global data
    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)
        data = [row for row in csv_reader]
    return data


def read_csv():
    global data
    data = data[1:]  # Skip the first row
    count = len(data)  # Count the remaining rows
    tui.rows_in_data(count)


def first_menu(choice):
    while True:
        if choice.upper() != "X":
            choice_input(choice)
            tui.main_menu()
        else:
            tui.invalid_opt()
            break


def choice_input(choice):
    if choice.upper() == "A":
        tui.submenu()
    elif choice.upper() == "B":
        tui.submenu2()


def submenu_one(option):
    global data
    if option.upper() == "A":
        print("You Have Chosen Option A - View Reviews By Park ")
        reviews_for_specific_park()
    elif option.upper() == "B":
        print("You have Chosen Option B - Number of Reviews by Park and Reviewer Location")
        tui.location_park()
    elif option.upper() == "C":
        print("You Have Chosen Option C - Average Score per Year by Park")
        tui.average_score_year()
    elif option.upper() == "D":
        print("You Have Chosen Option D - Average Score per Park by Reviewer Location")
        average_score_per_park_by_reviewer_location()
    else:
        print("Invalid Option, please start again!")


def submenu_two(option):
    if option.upper() == "A":
        print("You Have Chosen Option A-Most Reviewed Parks")
        visual.display_pie_chart()
    elif option.upper() == "B":
        print("You have Chosen Option B-Average Scores")
        visual.display_bar_chart()
    elif option.upper() == "C":
        print("You Have Chosen Option C-Park Ranking by Nationality")
        tui.park_rates()
    elif option.upper() == "D":
        print("You Have Chosen Option D-Most Popular Month by Park")
        tui.month_rates()
    else:
        tui.invalid_opt()


def reviews_for_specific_park():
    global data
    park_name = input("For which Park would you like to see the reviews: ")
    for review in data:
        if park_name.upper() in review[4].upper():
            tui.view_reviews(review)


def number_of_reviews_by_park_and_reviewer_location(park, location):
    count = 0
    for row in data:
        if park.lower() in row[4].lower() and location.lower() in row[3].lower():
            count = count + 1
    tui.total_reviews(count)


def average_score_per_year_by_park(park, year):
    average = 0
    rates = 0
    count = 0
    for row in data:
        if park.lower() in row[4].lower() and year in row[2]:
            rates += int(row[1])
            count += 1
            average = rates / count
    tui.average_by_year(average)


def average_score_per_park_by_reviewer_location():
    global data
    data = data[1:]
    count = {}
    score = {}
    for row in data:
        rate = int(row[1])
        park = row[4]
        location = row[3]
        park_location = (park, location)
        if park_location not in score:
            score[park_location] = rate
            count[park_location] = 1
        else:
            score[park_location] += rate
            count[park_location] += 1
    avg = {}
    for park_location in score:
        avg[park_location] = score[park_location] / count[park_location]
    for park_location, average in avg.items():
        park, location = park_location
        tui.all_avg(park, location, average)


data = read_csv_file("data\\disneyland.csv")
