import matplotlib.pyplot as plt
import csv


def read_csv_file(file_path):
    global data
    with open(file_path, "r") as f:
        csv_reader = csv.reader(f)
        data = [row for row in csv_reader]
    return data


def display_pie_chart():
    global data
    data = data[1:]
    data_by_parks = {}
    for row in data:
        park = row[4]
        rates = int(row[1])
        if park in data_by_parks:
            data_by_parks[park] += rates
        else:
            data_by_parks[park] = rates
    labels = list(data_by_parks.keys())
    sizes = list(data_by_parks.values())
    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels)
    plt.title("Most Reviewed Park")
    plt.show()


def display_bar_chart():
    global data
    data = data[1:]
    score = {}
    count = {}
    for row in data:
        park = row[4]
        rates = int(row[1])
        if park in score:
            score[park] += rates
            count[park] += 1
        else:
            score[park] = rates
            count[park] = 1
    x = list(score.keys())
    y = [score[park] / count[park] for park in score]
    plt.xlabel("Parks")
    plt.ylabel("Average Reviews ")
    plt.bar(x, y)
    plt.show()


def park_ranking_by_nationality(park):
    global data
    data = data[1:]
    temp = {}
    p = {}
    for n in data:
        if park.lower() in n[4].lower():
            location = (n[3])
            score = float(n[1])
            if location not in temp:
                temp[location] = []
            temp[location].append(score)
            p[location] = sum(temp[location]) / len(temp[location])
    sort_b = sorted(p.items())
    pk_in = sort_b[::-1]
    top_10 = pk_in[:10]
    locations = []
    rates = []
    for item in top_10:
        location, rate = item
        locations.append(location)
        rates.append(rate)
    plt.figure(figsize=(14, 6))
    plt.bar(locations, rates)
    plt.xlabel("Locations")
    plt.ylabel("Average rates")
    plt.xticks(fontsize=6)
    plt.title(f"Top 10 Locations for {park}")
    plt.show()


def most_popular_month_by_park(park):
    global data
    data = data[1:]
    months = {month: [] for month in range(1, 13)}
    for row in data:
        if park.lower() in row[4].lower():
            if '-' in row[2]:
                month = int(row[2].split('-')[1])
                rate = float(row[1])
                months[month].append(rate)
    average = {month: sum(months[month]) / len(months[month]) for month in months if months[month]}
    months = list(average.keys())
    avg_ratings = list(average.values())
    plt.bar(months, avg_ratings, tick_label=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                                             'Nov', 'Dec'])
    plt.xlabel('Month')
    plt.ylabel('Average Rating')
    plt.title(f'Average Ratings for {park} by Month')
    plt.show()


data = read_csv_file("data\\disneyland.csv")