import json
import random

def sortPlayers(element): 
    return len(element["available_jobs"])

def sortByJob(element):
    if 'tank' in element['role']:
        return 0
    elif 'healer' in element['role']:
        return 1
    elif 'melee' in element['role']:
        return 2
    elif 'magic' in element['role']:
        return 3
    elif 'ranged' in element['role']:
        return 4

if __name__ == "__main__":
    players = []
    with open("players/players.json", "r+") as file:
        players = json.load(file)
    players.sort(key=sortPlayers)
    jobs = {}
    with open("jobs/ff14.json", "r+") as file:
        jobs = json.load(file)
    #TODO: Load avaialble roles from a file at some point
    player_role = []
    available_roles = ["tank", "tank", "regen", "shield", "melee", "magic", "ranged", "dps"]
    for player in players:
        completed = False
        while(not completed):
            random_job = player["available_jobs"][random.randint(0, len(player["available_jobs"])-1)]
            if (random_job in jobs):
                role_found = False
                for role in jobs[random_job]["role"]:
                    if (role in available_roles):
                        available_roles.remove(role)
                        role_found = True
                        break
                if role_found:
                    player_role.append({
                        "name": player["name"],
                        "job_abr": random_job,
                        "job_full": jobs[random_job]["full"],
                        "role": jobs[random_job]["role"],
                    })
                    jobs.pop(random_job)
                    completed = True
            else:
                player["available_jobs"].remove(random_job)
                if (len(player["available_jobs"]) < 1):
                    print("Your static is dumb and stupid")
                    quit()
    player_role.sort(key=sortByJob)
    print_string = ''
    for player in player_role:
        print_string = f"{print_string}{player['name']}: {player['job_full']}\n"
    print(print_string)
