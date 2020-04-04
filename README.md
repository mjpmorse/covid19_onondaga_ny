# covid19_onondaga_ny
municipality level covid19 time series case data for Onondaga NY


This github contains:

onondaga_plotter.py
    python program which plots the csv data for a given municipality
    $ python onondaga_plotter.py Clay

onondaga_time_series
    Time series data starting April 3rd. Tracks covid 19 cases in the following municipalities:
      Syracuse, Clay, DeWitt, Camillus, Salina, Cicero, Manlius, Onondaga, Pompey,
      Geddes, Lysander, Skaneateles, Van Buren, LaFayette, Marcellus,
      Otisco, Tully, Fabius, Spafford, Elbridge, Onondaga Nation
    The data is scraped from: https://socpa.maps.arcgis.com/apps/opsdashboard/index.html#/7bd218bc8be04b209c0b80a83fc2eba5
    at 6pm each night

scraper.py
    python program which scrapes https://socpa.maps.arcgis.com/apps/opsdashboard/index.html#/7bd218bc8be04b209c0b80a83fc2eba5 and generates the onondaga_time_series.csv

LICENSE
    GNU GENERAL PUBLIC LICENSE
