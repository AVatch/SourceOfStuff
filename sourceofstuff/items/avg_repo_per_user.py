from scrape_repos import get_repos
import random

sampling_percentage = 0.00001

user_count = 0
repos_count = 0

with open('data/github_user_list.csv', 'rb') as f:
    for index, line  in enumerate(f.xreadlines()):
        roll = random.random()

        if roll < sampling_percentage:
            user_count += 1
            username = line.split(",")[0].rstrip()
            repos_count += len(get_repos(username))

print "*"*50
print "Done:\tTotal Users:\t", user_count, "\tAvg Repos/User:\t", repos_count / user_count
