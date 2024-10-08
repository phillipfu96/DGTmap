import folium
import requests
from folium.plugins import MarkerCluster

# Fetch camera data
url = 'https://geoportal.valencia.es/apps/OpenData/Trafico/tra_camaras.json'
response = requests.get(url)
data = response.json()

# Initialize the map
m = folium.Map(location=[39.4677, -0.3774], zoom_start=12, tiles="CartoDB dark_matter")

# Create a marker cluster
marker_cluster = MarkerCluster().add_to(m)

# Add custom CSS to the map
custom_css = """
<style>
    /* Custom Leaflet Popup Styles */
    .leaflet-popup-content {
        background-color: #333; /* Change this to your desired background color */
        color: #fff; /* Change text color for better contrast */
        padding: 0px; /* Add some padding for aesthetics */
        border-radius: 5px; /* Optional: round the corners */
    }

    .leaflet-popup-content-wrapper {
        background-color: #333; /* Same as above for consistency */
    }

    .leaflet-popup-tip {
        background-color: #333; /* Change the triangle tip color if needed */
    }

    /* Optional: Adjust the border of the popup */
    .leaflet-popup {
        border: 2px solid #fff; /* Change this to your desired border color */
    }
</style>
"""

# Add the custom CSS to the map's HTML
m.get_root().html.add_child(folium.Element(custom_css))

# Add markers to the map
for feature in data['features']:
    if feature['geometry']:
        location = [feature['geometry']['coordinates'][1], feature['geometry']['coordinates'][0]]
        if feature['properties']['idcamara'] and feature['properties']['url']:
            camera_id = feature['properties']['idcamara']
            popup_html = f"""
                <div>
                    <a href='camera_preview?id={camera_id}' 
                       target='_blank' 
                       style='display: inline-block; margin-bottom: 10px; padding: 5px; background-color: #007bff; color: black; text-decoration: none; border-radius: 4px;'>
                        Open Camera
                    </a>
                    <iframe 
                        src='camera_preview?id={camera_id}' 
                        width='400' 
                        height='320' 
                        style='border:none;'>
                    </iframe>
                </div>
            """
        else:
            popup_html = None

        folium.Marker(location=location, popup=popup_html, icon=folium.Icon(icon="camera", prefix="fa")).add_to(
            marker_cluster)

# Save the map to an HTML file
m.save('templates/map.html')
