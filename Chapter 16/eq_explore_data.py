from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    print(lons[:5])
    print(lats[:5])

# Create a more readable version of the data file.
path = Path("eq_data/eq_data_1_day_m1.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)
