import geopandas as gpd
from shapely.geometry import Point
import pyproj

# Load MultiPolygon data from a GeoJSON file
geojson_file = '21_01.json'  # Update with your file path
gdf = gpd.read_file(geojson_file)

# Assuming the MultiPolygon is in the first row of the GeoDataFrame
multi_polygon = gdf.geometry.iloc[0]

# Define your point in EPSG:4326 (longitude, latitude)
point_4326 = Point(-122.4194, 37.7749)  # Example coordinates (San Francisco)

# Transform point from EPSG:4326 to EPSG:3857
transformer = pyproj.Transformer.from_crs(4326, 3857, always_xy=True)
x_3857, y_3857 = transformer.transform(point_4326.x, point_4326.y)
point_3857 = Point(x_3857, y_3857)

# Check if the transformed point is within the MultiPolygon
is_inside = point_3857.within(multi_polygon)

if is_inside:
    print("The point is inside the MultiPolygon.")
else:
    print("The point is outside the MultiPolygon.")
