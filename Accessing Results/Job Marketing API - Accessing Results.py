from jobicy_data import response

senior_roles = []
manager_roles = []

jobs = response['jobs']

for job in jobs:
    if 'Senior' in job['jobTitle']:
        senior_roles.append(job['jobTitle'])
    elif 'Manager' in job['jobTitle']:
         manager_roles.append(job['jobTitle'])


print('manager_roles:', manager_roles)
print('senior_roles:', senior_roles)