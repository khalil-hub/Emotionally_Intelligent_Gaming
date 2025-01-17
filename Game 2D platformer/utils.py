import csv

def log_data(player_id, level, retries, completion_time):
    with open ("player_data.csv", "a") as file:
        writer=csv.writer(file)
        writer.writerow([player_id, level, retries, completion_time])