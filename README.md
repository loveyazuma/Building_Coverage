# Building Coverage
The aim of this project was to extract building features and calculate the percentage it covers within the Area of Interest (AOI).


### Details
* The folder works with a project structure and well-structured scripts were created with one main script. A main.py module was made that imports functions from another Python module called 'MyFunctions_3.py'. 
* The OpenStreetMap data was utilised. The OSMNX package developed by [Geoff Boeing](https://geoffboeing.com/), was employed and the documentation can be found here; [osmnx documentation](https://osmnx.readthedocs.io/en/stable/osmnx.html).

### Processes
- MyFunctions_VectorExc.py was written and three functions to extract the AOI, building geometries and calculate the percentage area were defined
- A main script was created where the functions from MyFunctions_VectorExc.py were imported
- The AOI was visualised with the folium library and saved as `.html` file