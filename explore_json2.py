import json

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

infile = open('eq_data_30_day_m1.json', 'r')
outfile = open('readable_eq_data2.json', 'w')

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent = 5)

# Type of object
print(type(eq_data))

# Number of eqs
#print(len(eq_data["features"]))
list_of_eqs = eq_data["features"]
print(len(list_of_eqs))

# Empty lists
mags, lons, lats, hover_text  = [], [], [], []


for i in list_of_eqs:
    if i["properties"]["mag"] > 5:
        mags.append(i["properties"]["mag"])
        lons.append(i["geometry"]["coordinates"][0])
        lats.append(i["geometry"]["coordinates"][1])
        hover_text.append(i["properties"]["title"])

#print(mags[:10])
#print(lons[:10])
#print(lats[:10])

#my_data = Scattergeo(lon = lons, lat = lats)

my_data = [
    {
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_text,
    'marker' : {
    'size' : [5*mag for mag in mags],
    'color' : mags,
    'colorscale' : 'Viridis',
    'reversescale' : True,
    'colorbar' : {'title' : 'Magnitude'} 
    }
    }
]
my_layout = Layout(title = 'Global Earthquakes')

fig = {'data' : my_data, 'layout': my_layout}

offline.plot(fig, filename= 'global_earthquakes2.html')
