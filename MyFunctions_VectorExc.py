#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def GeocodePlacenameToGDF(placename='AOI', EPSGcode='28992'):
    """This function uses the OSMNX package to extract a geometry 
    representing the placename provided as input and transforms to 
    the required projection (EPSG code)"""
    import osmnx as ox
    PlaceGDF = ox.gdf_from_place(placename)
        
    # check first whether there is any output to return
    if len(PlaceGDF) == 1:
        # project GDFs to the required projection
        crs = 'epsg:'+EPSGcode
        try: PlaceGDF = PlaceGDF.to_crs({'init': crs})
        except: print("Given EPSG-code doesn't exist")
        else: return PlaceGDF
    else:
        print("We're sorry, but the given placename is not found within OpenStreetMap. Check for typos or try another placename")

def BAGtoGeoDataFrame(bbox=(174000, 174500, 444000, 444500)):
    """This function extracts building features for a given bbox within the 
    Netherlands. Results are saved as GML file and function returns a GDF of
    the buildings geometries within the given extent."""
    import geopandas as gpd
    from requests import Request
    from owslib.wfs import WebFeatureService
    from matplotlib import pyplot as plt
    # extract only buildings on and around AOI
    url = 'https://geodata.nationaalgeoregister.nl/bag/wfs'
    layer = 'bag:pand'
    # speciy the boundary box for extracting
    bb = ','.join(map(str, bbox)) # string needed for the request
    # Specify the parameters for fetching the data
    params = dict(service='WFS', version="2.0.0", request='GetFeature',
          typeName=layer, outputFormat='text/xml; subtype=gml/3.2',
          srsname='urn:ogc:def:crs:EPSG::28992', bbox=bb)
    # Parse the URL with parameters
    q = Request('GET', url, params=params).prepare().url
    # Read data from URL
    BuildingsGDF = gpd.read_file(q)
    
    try: 
        BuildingsGDF = gpd.read_file(q)
        return BuildingsGDF
    except:
        print("Oh Oh! something went wrong...")

        
def CalculatePercentageArea(DomainGDF, ObjectGDF):
    """This function calucates the percentage coverage of the objects within 
    the given focus area"""
    import geopandas as gpd
    OverlapGDF = gpd.overlay(DomainGDF, ObjectGDF, how="intersection")
    DomainArea = sum(DomainGDF.area)
    ObjectsArea = sum(OverlapGDF.area)
    PercentageObjectCoverage = (ObjectsArea/DomainArea)*100
    print("The total domain has a total surface area of "
          + str(round(DomainArea/10000, 2)) + " ha. Within this domain, the objects cover a total of "
          + str(round(ObjectsArea)) + " m2, "
          + str(round(PercentageObjectCoverage, 1)) + "% of the domain area.")
    return OverlapGDF, ObjectsArea, PercentageObjectCoverage
    
    
