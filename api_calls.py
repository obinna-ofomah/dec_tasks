######################################################################
# Task 1 - Extract all the senior and managerial roles 

import requests 
roles_url = 'https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo'
response = requests.get(roles_url)
roles_data = response.json()['jobs']

managerial_roles = []
senior_roles = []

for role in roles_data:
    if 'Manager' in role['jobTitle']:
        managerial_roles.append(role['jobTitle'])

    if 'Senior' in role['jobTitle'] or 'Sr.' in role['jobTitle']:
        senior_roles.append(role['jobTitle'])


print(managerial_roles)
print(senior_roles)


###############################################################################
# Task 2 - Extract all the competitions from the api

football_api = 'http://api.football-data.org/v4/competitions/'
football_response = requests.get(football_api)
competitions_data = football_response.json()['competitions']

competition_list = []

for competition in competitions_data:
    competition_list.append(competition['name'])



###############################################################################
# Task 3 -  Extract all the male and female profiles into different lists

profiles_url = 'https://randomuser.me/api/?results=500'
profiles_data = requests.get(profiles_url).json()['results']

males_profile = []
females_profile = []
dates_of_birth = []
full_names = []

for profile in profiles_data:
    # appending the dates_of_birth for each profile
    dates_of_birth.append(profile['dob']['date'])

    # appending the concatenated full name into a list
    first_name = profile['name']['first']
    last_name = profile['name']['last']
    full_name = first_name + ' ' + last_name
    full_names.append(full_name)

    # Spliting the profiles into males and females
    if profile['gender'] == 'female':
        females_profile.append(profile)
    elif profile['gender'] == 'male':
        males_profile.append(profile)