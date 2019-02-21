import  pandas
import folium
#Web MAp project using python 3.6
#the project uses Folium and Pandas lib

# First Pandas is used o parse the csv file and get teh required headers in a seprate variables
data = pandas.read_csv("Volcanoes_of_the_World.csv")
long = list(data["long"])
lat = list(data["lat"])
elev = list(data["ELEV"])
name= list(data["NAME"])
type = list(data["TYPE"])

#function to determine the color of marker based on mountain hieght
def color_prod(elv):
    if elv < 1000:
        return 'green'
    elif 1000 <= elv < 3000:
        return 'orange'
    else:
        return 'red'
#A instance of folium mao is created with a random coordinates and stamen Terrain tiles
map = folium.Map(location=[-70,-20],zoom_start=6,tiles='Stamen Terrain')
#the first group of markers is created To contain all the mmakers of mountains
vgrp = folium.FeatureGroup(name="Volcanoes of The World")
#Lopping through all csv data each line contains a name and elvation of mountain along with latitude and Longtitude
#each iterationa  marker is created with name and elevation in popup (folium.Popup is used becouse some of the mountain names contain qoutation marks " ' ")
#makers color is determined and added to teh parameters
#Finally every iteration a child marker is added tot eh markers group
for ln,lat,nm, el in zip(long,lat,name,elev):
    vgrp.add_child(folium.CircleMarker(location=[ln, lat], radius = 6, popup=folium.Popup(nm + ":" + str(el) + "m",parse_html=True),
    fill_color=color_prod(el), fill=True,  color = 'grey', fill_opacity=0.7))
#second group to contain the polgon shapes for countries and their color according to their population
wgrp = folium.FeatureGroup(name="Population Of Countries")
#A JSON file that contains all countries coordinates with their population as of 2005
#The anonymous function is used to loop throught the features of each country , filling a color according to said country population
#populaton is stored in pop2005 attribute in the properties of each country by comparing them each country gets a assigned a color
wgrp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
#Adding every feature group created
map.add_child(wgrp)
map.add_child(vgrp)
#Layers Controll allos user to switch between the feature groups on the map , turing any off at will
map.add_child(folium.LayerControl())
#Map is saved with the specified Name
map.save('Map1.html')

#Yikes THat took time but was Fun tho !! :)
