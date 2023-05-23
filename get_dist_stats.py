# Import packages
from joblib import Parallel, delayed

import utils

# List of paths
country_codes = ['ESP', 'EST', 'ETH', 'USA']
dem_names = ['AW3D30', 'COP30', 'HydroSHEDS', 'MERIT', 'NASADEM', 'TanDEM']
feature_types = ['basin', 'stream']
paths = []
for country_code in country_codes:
    for dem_name in dem_names:
        for feature_type in feature_types:
            paths.append(
                utils.get_fp_to_points(country_code=country_code, dem_name=dem_name, feature_type=feature_type)
            )

# Get distance statistics in parallel
Parallel(n_jobs=4, prefer='threads')(delayed(utils.get_dist_stats)(path, 'dist_to_ref') for path in paths)
