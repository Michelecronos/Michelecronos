import process
import visual


def main():
    title = "Disneyland Review Analyser"
    print("-" * len(title))
    print(title)
    print("-" * len(title))
    process.read_csv()


def rows_in_data(count):
    print(f"Finished reading the dataset.\nTotal records loaded: {count}")
    main_menu()


def main_menu():
    choice = input("\nPlease enter the letter which corresponds with your desired menu choice:\n"
                   "[A] View Data\n"
                   "[B] Visualise Data\n"
                   "[X] Exit\n")
    process.first_menu(choice)


def submenu():
    print("You have chosen option A - View Data")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per year  by Park")
    print("[D] Average Score per Park by Reviewer Location")
    option = input("Enter your choice: ")
    process.submenu_one(option)


def view_reviews(review):
    print(review[1], end=" ")


def invalid_opt():
    print("Invalid Option, please try again!!! ")
    main_menu()


def location_park():
    park = input("Which park would you like to see the review? ")
    location = input("Which location? ")
    process.number_of_reviews_by_park_and_reviewer_location(park, location)


def total_reviews(count):
    print(f"Total of reviews {count}")


def average_score_year():
    park = input("Which park's average would you like to see? ")
    year = input("The year that would you like to see? ")
    process.average_score_per_year_by_park(park, year)


def average_by_year(average):
    print(f"The average rate is {average:.2f}")


def all_avg(park, location, average):
    print(f"Park: {park}")
    print(f"Location: {location}")
    print(f"Average: {average}\n")


def submenu2():
    print("You have chosen option B - Visualise Data")
    print("[A] Most Reviewed Parks")
    print("[B] Average Score")
    print("[C] Park Ranking by Nationality")
    print("[D] Most Popular Month by Park")
    option = input("Enter your choice: ")
    process.submenu_two(option)


def park_rates():
    park = input("Enter the park for see the top 10 location: ")
    visual.park_ranking_by_nationality(park)


def month_rates():
    park = input("Enter the park for the average rates by months?\n")
    visual.most_popular_month_by_park(park)
