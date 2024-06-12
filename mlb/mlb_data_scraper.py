import re           # regex
import requests     # webpage requests
import csv

hitting = 'https://www.mlb.com/stats/team'
pitching = 'https://www.mlb.com/stats/team/pitching'
user_agent_1 = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
header = {'User-Agent': user_agent_1}

def get_hitting_data():
    r = requests.get(hitting, headers=header)
    with open("hitting_data.html", "w") as text_file:
        text_file.write(r.text)

    hitting_data_helper(r)
    
    # make csv
    fields = ['rank', 'team', 'league', 'games_played', 'at_bats', 'runs', 'hits', '2B', '3B', 
              'HR', 'RBI', 'BB',   'SO', 'SB', 'CS', 'AVG', 'OBP', 'SLG', 'OPS']
    csv_filename = 'hitting.csv'
    with open(csv_filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # write fields
        csvwriter.writerow(fields)
        # write data rows

def hitting_data_helper(r):
    NUM_TEAMS = 30
    mlb_data = []
    
    # team rankings
    for i in range(NUM_TEAMS):
        mlb_data.append([i + 1])

    teams = get_team_names(r)
    we = get_whatever(r)
    pass

    # for i in range(18):
    #     # get team name
        
    #     if i == 0:
    #         get_team_name(r)
    #         pass

    #     current_row = []
    #     for j in range(30):
    #         str = f'data-col="{i}" data-row="{j}"'
    #         current_row.append(j)
    #     matrix.append(current_row)

def get_team_names(r):
    pattern = 'class=\"short-IiSPVSQp\">([^<]*)'
    teams_in_ranked_order = re.findall(pattern=pattern, string=r.text)
    return(teams_in_ranked_order)
def get_whatever(r):
    pattern = 'data-col=\"[^\"]*\" data-row=\"3\">([^<]*)'
    whatever = re.findall(pattern, r.text)
    return(whatever)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_hitting_data()
    pass
