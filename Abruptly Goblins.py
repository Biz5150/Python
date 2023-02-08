gamers = []


# gamer should be a dictionary like {"name": "[gamer_name]", "availability": "[days of week]"}
def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Gamer missing information")


#list of gamers with availability
kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

#print(gamers)

#Table to establish what days are most people available on
def build_daily_frequency_table():
    return {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0, 
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0,
    }

count_availability = build_daily_frequency_table()

#Fuction to take a gamer's availability and add it to a table to find best availability
def calculate_availabilty(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

#Will add to count_availability table
calculate_availabilty(gamers, count_availability)

#print(count_availability)


#Takes an availability table and finds the day most people can game
def find_best_night(availability_table):
    start_num = 0
    for day, num in availability_table.items():
        if num > start_num:
            start_num = num
            best_day = day
    return best_day


game_night = find_best_night(count_availability)

#print(game_night)


#Takes a night and returns a table of gamers who are available on that night
def available_on_night(gamers_list, night):
    available_gamers = []
    for gamer in gamers_list:
        if night in gamer['availability']:
            available_gamers.append(gamer['name'])
        else:
            continue

    return available_gamers


attending_game_night = available_on_night(gamers, game_night)

print(attending_game_night)

#Built another table to get 2nd best night
second_night_availabilty = build_daily_frequency_table()

#Email form to send to gamers whom are available for a game night
form_email = """
Hey {name},

It looks like we're going to be playing {game} on {day_of_week}.
Let me know if there's anything you want in terms of snacks and I'll look to pick them up.
See ya there, gamer!

From, Biz"""

#Only sends email to those who can attend
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer,game=game,day_of_week=day))



#send_email(attending_game_night, game_night, "Abruptly Goblins")


#List of those unable to attend the best night
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]

#Make table for those not attending best night
second_night_availabilty = build_daily_frequency_table()


calculate_availabilty(unable_to_attend_best_night, second_night_availabilty)

#Attempting to find best 2nd night
second_night = find_best_night(second_night_availabilty)

print(second_night)


available_second_game_night = available_on_night(gamers, second_night)


send_email(available_second_game_night, second_night, "Abruptly Goblins")





    
