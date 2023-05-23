# Import packages
from joblib import Parallel, delayed

import utils

# Input parameters
country_codes = ['ESP', 'USA', 'EST', 'ETH']
dem_names = ['AW3D30', 'COP30', 'HydroSHEDS', 'MERIT', 'NASADEM', 'TanDEM']

# Calculate sinuosity in parallel
Parallel(n_jobs=4)(
    delayed(
        utils.get_sinuosity_stats
    )(country_code=country_code, dem_name=dem_name) for country_code in country_codes for dem_name in dem_names)
