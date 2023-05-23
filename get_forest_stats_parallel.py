# Import packages
from joblib import Parallel, delayed

import utils

# Get input dictionary for forest statistics
country_codes = ['ESP', 'EST', 'ETH', 'USA']
dem_names = ['AW3D30', 'COP30', 'HydroSHEDS', 'MERIT', 'NASADEM', 'TanDEM']
feature_types = ['basin', 'stream']
stats_input = []
for country_code in country_codes:
    stats_input.append(
        utils.get_forest_stats_input(country_code=country_code, dem_names=dem_names, feature_types=feature_types)
    )

# Get forest statistics in parallel
Parallel(n_jobs=4)(
    delayed(
        utils.get_forest_stats
    )(
        fp_to_buffers, fp_to_slope, 'forest_pct'
    ) for input_dict in stats_input for fp_to_buffers, fp_to_slope in input_dict.items()
)
