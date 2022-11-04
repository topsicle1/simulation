print(".. SIMULATION OF TIME TO COMPLETE TASKS")

data_collectors = 14
sprints_per_dc = 2.5
current_devs = {"lando": .3, "paz": 1, "arvin": 1}
mphasis_devs_boost = 5

total_devs_per_sprint = sum(current_devs.values()) * mphasis_devs_boost
total_sprints = (data_collectors * sprints_per_dc)/total_devs_per_sprint
total_months = total_sprints/2

print(f"Number of Data Collectors = {data_collectors}")
print(f"Sprints per Data Collector = {sprints_per_dc}")
print(f"Dev per Sprint = {total_devs_per_sprint} (w/ mPhasis = {mphasis_devs_boost})")
print(f"Total Springs = {total_sprints}")
print(f"Total Months = {total_months}")


