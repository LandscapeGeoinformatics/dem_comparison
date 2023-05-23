# Import packages
import glob
from pathlib import Path
from joblib import Parallel, delayed

import utils

# List of paths
paths = []
for fp in glob.glob(f'D:/dem_comparison/data/*/*/*.*'):
    if 'Ref' not in fp and Path(fp).suffix in ['.gpkg', '.shp']:
        paths.append(fp)

# Process points in parallel
Parallel(n_jobs=4)(delayed(utils.process_points)(path) for path in paths)
