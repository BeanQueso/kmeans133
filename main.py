import csv
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data = []

solar_mass = []
solar_radius = []
solar_gravity = []

with open("new_merged.csv", 'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data.append(i)

star_data_rows = data[1:]

for star_data in star_data_rows:
    solar_mass.append(star_data[2])
    solar_radius.append(star_data[3])
    solar_gravity.append(star_data[8])

solar_mass.sort()
solar_radius.sort()
solar_gravity.sort()


plt.scatter(solar_mass, solar_radius)
plt.title('Mass, Radius')
plt.xlabel('Mass')
plt.ylabel('Radius')

plt.show()

plt.scatter(solar_mass, solar_gravity)
plt.title('Mass, Gravity')
plt.xlabel('Mass')
plt.ylabel('Gravity')

plt.show()

