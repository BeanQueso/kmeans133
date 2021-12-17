from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import csv

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
    solar_mass.append(star_data[6])
    solar_radius.append(star_data[7])

solar_mass.sort()

new_mass = []
new_radius = []

for star_data in solar_radius:
    star_data.replace("''", '')
    star_data.replace(',', '')
    if '-' in star_data == True:
        val1 = star_data.split("–")[0]
        val2 = star_data.split("–")[1]
        finalv = float(val1) - float(val2)
        new_radius.append(finalv)
    else:
        new_radius.append(star_data)


for star_data in solar_mass:
    star_data.replace("''", '')
    star_data.replace(',', '')
    if '-' in star_data == True:
        val1 = star_data.split("–")[0]
        val2 = star_data.split("–")[1]
        finalv = float(val1) - float(val2)
        new_mass.append(finalv)
    else:
        new_mass.append(star_data)



X = []

for index, star_data in enumerate(new_mass):
  temp_list = [new_radius[index], star_data]
  X.append(temp_list)

wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

plt.figure(figsize = (10,5))

sns.lineplot(range(1,11), wcss, marker = 'o', color = 'red')
plt.title('The elbow method')
plt.xlabel('number of clusters')
plt.ylabel('wcss')
plt.show() 
