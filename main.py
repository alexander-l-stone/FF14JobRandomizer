import json
import random
import argparse

def sortPlayers(element): 
    return len(element["available_jobs"])

def sortByJob(element):
    if 'tank' in element['role']:
        return 0
    elif 'healer' in element['role']:
        return 1
    elif 'melee' in element['role']:
        return 2
    elif 'caster' in element['role']:
        return 3
    elif 'ranged' in element['role']:
        return 4

def openFile(filepath):
    content = None
    with open(filepath, 'r+') as file:
        content = file
    return content

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("role_set")
    ap.add_argument("teamname")
    args = ap.parse_args()
    with open("json/teams.json", "r+") as file:
        teams = json.load(file)
    if args.teamname in teams:
        team = teams[args.teamname]
    with open("json/players.json", "r+") as file:
        players = json.load(file)
    teamplayers = []
    for player in players:
        if player["name"] in team:
            teamplayers.append(player)
    teamplayers.sort(key=sortPlayers)
    jobs = {}
    with open("games/ff14.json", "r+") as file:
        jobs = json.load(file)
    player_role = []
    available_roles = []
    with open("json/compositions.json", "r+") as file:
        roles_file = json.load(file)
        available_roles = roles_file[args.role_set]
    for player in teamplayers:
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
