# Import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

import utils

# Read statistics and create DataFrame
country_codes = ['ESP', 'USA', 'EST', 'ETH']
dem_names = ['AW3D30', 'COP30', 'HydroSHEDS', 'MERIT', 'NASADEM', 'TanDEM']
df_list = []
for country_code in country_codes:
    for dem_name in dem_names:
        df = pd.read_csv(f'D:/dem_comparison/data/{country_code}/stats/{country_code}_{dem_name}_sinuosity.csv')
        df_list.append(df)
stats_df = pd.concat(df_list).reset_index(drop=True)
stats_df['Catchment name'] = utils.get_catchment_name(country_code)
stats_df = stats_df.sort_values(['Catchment name', 'DEM'])

# Calculate absolute sinuosity difference by DEM and write to CSV
grouped = stats_df.groupby('DEM')['Absolute difference'].describe().reset_index()
grouped = grouped.sort_values('mean').reset_index(drop=True)
grouped.to_csv(f'D:/dem_comparison/data/abs_sinuosity.csv', index=False)

# Create figure and save as PNG
sns.set_palette(sns.color_palette([utils.get_hex_code(dem_name) for dem_name in dem_names]))
fig, ax = plt.subplots(1, 1, figsize=(12, 6))
sns.barplot(y='Difference', x='Country', data=stats_df, hue='DEM', ax=ax)
ax.set_xticklabels([utils.get_catchment_name(country_code) for country_code in country_codes], fontsize=16)
ax.set_xlabel(None)
ax.set_ylabel('${S_{Diff}}$ (%)', fontsize=16)
for container in ax.containers:
    ax.bar_label(container, fontsize=16)
handles, labels = ax.get_legend_handles_labels()
labels[-1] = 'TanDEM-X'
plt.legend(handles, labels, bbox_to_anchor=(1, 1), loc=2, title_fontsize=16, fontsize=16)
plt.tight_layout()
plt.savefig(f'D:/dem_comparison/figures/sinuosity_by_catchment.png', dpi=300)
