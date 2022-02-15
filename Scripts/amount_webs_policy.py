# Script for calculete the percentage of webs with policys and the percentage of webs that allow
# web scraping

from os import listdir # Library used for iterate through
import matplotlib.pyplot as plt # Matplotlib library used for make graphics


plt.rc('font', size=20)          # controls default text sizes
plt.rc('legend', fontsize=18)    # legend fontsize

# Calculate the percentage of webs with and without policys
cantidad1 = [(77*100/139),(62*100/139)]
# legends of the chart
nombres1 = ["Sitios web CON \npolíticas de privacidad","Sitios web SIN \npolíticas de privacidad"]
# Graph pie chart
plt.pie(cantidad1, startangle=145, autopct="%0.1f %%")
# configure the position of the legend
plt.legend(nombres1, bbox_to_anchor=(0.85,1.025), loc="upper left")
plt.show()


# Calculate the percentage of webs that allow automatic downloads
cantidad2 = [(67*100/139),(10*100/139)]
# legends of the chart
nombres2 = ["Sitios web SI \npermiten descarga automatizada","Sitios web NO \npermiten descarga automatizada"]
# Graph pie chart
plt.pie(cantidad2, startangle=145, autopct="%0.1f %%")
# configure the position of the legend
plt.legend(nombres2, bbox_to_anchor=(0.85,1.025), loc="upper left")
plt.show()


