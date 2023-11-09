# Introduction to Data Visualization with Matplotlib.

## Chapter-1 : Introduction.

_This chapter introduces the Matplotlib visualization library and demonstrates how to use it with data._

<h3> Importing essential Libraries.<h3>
  
```

# Importing the course packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the course datasets 
climate_change = pd.read_csv('datasets/climate_change.csv', parse_dates=["date"], index_col="date")
medals = pd.read_csv('datasets/medals_by_country_2016.csv', index_col=0)
summer_2016 = pd.read_csv('datasets/summer2016.csv')
austin_weather = pd.read_csv("datasets/austin_weather.csv", index_col="DATE")
weather = pd.read_csv("datasets/seattle_weather.csv", index_col="DATE")

# Some pre-processing on the weather datasets, including adding a month column
seattle_weather = weather[weather["STATION"] == "USW00094290"] 
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] 
seattle_weather["MONTH"] = month 
austin_weather["MONTH"] = month
  
```
  
  (i) <ins>Using the matplotlib.pyplot interface</ins>
  
  <h3> CODE </h3>
 ```
  # Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()


# Call the show function to show the result
plt.show()
  ```
  
  OUTPUT : 
  ![image](https://user-images.githubusercontent.com/77969007/234915057-aad4925e-5f06-427d-8d67-7dba6bb29a87.png)

  (ii.) <ins>Adding data to an Axes object</ins> 
  
  <h3>CODE:</h3>
  ```
  
  # Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Plot MLY-PRCP-NORMAL from seattle_weather against MONTH
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Call the show function
plt.show()
  
  ```
  
  _output:_
  
  ![image](https://user-images.githubusercontent.com/77969007/234919682-254238aa-be99-44ce-a50e-b225e25453ed.png)

   (iii.) <ins>Customizing data appearance </ins>

  <h3>CODE:</h3>
  
  
  ```
  # Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"],
        color='b', marker='o', linestyle='--')

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"],
        color='r', marker='v', linestyle='--')

# Call show to display the resulting plot
plt.show()
  ```
  
  _OUTPUT:_
  
  ![image](https://user-images.githubusercontent.com/77969007/234920212-493821c0-6b98-46db-9543-3254d782d36f.png)
  
  (iv.) <ins> Customizing axis labels and adding titles </ins>
  
  _INSTRUCTIONS:_
  
  <h3> CODE : </h3>
  
  ```
  
  ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel("Time (months)")

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.show()
  
  ```
  _Output:_
  
  ![image](https://user-images.githubusercontent.com/77969007/234926828-023a952c-5e53-448a-9880-3b417ccf37d0.png)
  
  
  
  
(v.)  <ins>Creating small multiples with plt.subplots</ins>
  
  <h3> CODE : </h3>
  
  ```
  
  # Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2,2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather["MONTH"],seattle_weather["MLY-PRCP-NORMAL"])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather["MONTH"],seattle_weather["MLY-TAVG-NORMAL"])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1, 0].plot(austin_weather["MONTH"],austin_weather["MLY-PRCP-NORMAL"])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1, 1].plot(austin_weather["MONTH"],austin_weather["MLY-TAVG-NORMAL"])
plt.show()
  
  ```
_Output:_
  
  ![image](https://user-images.githubusercontent.com/77969007/234927749-b345cc40-0642-480b-962a-3ad349b60578.png)
  
  
  (vi.) <ins> Small multiples with shared y axis </ins>
  
  
  <h3>CODE:</h3>
  
  ```
  
          # Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation in the top axes
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color='b', linestyle='--')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], color='b', linestyle='--')

# Plot Austin precipitation in the bottom axes
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color='r', linestyle='--')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color='r', linestyle='--')

plt.show()
  ```
  
  _Output:_
  
  ![image](https://user-images.githubusercontent.com/77969007/234928181-e5e18f3b-39e9-4d56-aad8-3320f8707d90.png)

  
  
  # In The Next Chapter : Plotting Time Series we will be learning to record Time series and plot them accordingly on a Graph for purpose of Visualization. Time series data is data that is recorded. Visualizing this type of data helps clarify trends and illuminates relationships between data.Use the below Link to directly open the Repository.
  
  
  # 🔗 LINK : https://github.com/Darshan0902/Plotting-time-series 
  
  
  



  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
  
