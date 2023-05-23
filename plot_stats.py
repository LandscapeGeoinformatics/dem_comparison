# Import packages
import sys

import utils

# Name of statistic to plot
stat_name = sys.argv[1]

# Input parameters
country_codes = ['ESP', 'USA', 'EST', 'ETH']
dem_names = ['AW3D30', 'COP30', 'HydroSHEDS', 'MERIT', 'NASADEM', 'TanDEM']
feature_types = ['basin', 'stream']

# Create and save plots based on input statistic
for feature_type in feature_types:
    utils.subplots_to_png(country_codes, dem_names, feature_type, stat_name, utils.plot_stat_vs_dist)
    utils.subplots_to_png(country_codes, dem_names, feature_type, stat_name, utils.plot_hist)
    utils.plot_stat_vs_dist_by_class(country_codes, dem_names, feature_type, stat_name)
