from rosreestr2coord import Area
import folium


def get_coordinates(number):
    points = []
    area = Area(number, media_path='media_files')
    coordinates = area.get_coord()
    for coordinate in coordinates:
        for addresses in coordinate:
            map_image = folium.Map((addresses[0][1], addresses[0][0]), zoom_start=16)

            for pt in addresses:
                place_lat = [pt[1] for pt in addresses]
                place_lng = [pt[0] for pt in addresses]

                for i in range(len(place_lat)):
                    points.append([place_lat[i], place_lng[i]])

                folium.PolyLine(points, color='red').add_to(map_image)
            map_image.save('webapp/templates/our_map.html')
