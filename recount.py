# https://open.kattis.com/problems/recount
import collections

name = input().strip()
votes = collections.defaultdict(int)
greatest_votes = 1
people_with_most_votes = []
while name != "***":
  votes[name] += 1
  if votes[name] == greatest_votes:
  	people_with_most_votes.append(name)
  elif votes[name] > greatest_votes:
    greatest_votes = votes[name]
    people_with_most_votes = [name]
  name = input().strip()
if len(people_with_most_votes) == 1:
  print(people_with_most_votes[0])
else:
  print('Runoff!')