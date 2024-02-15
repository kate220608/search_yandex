def parametrs(response):
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    toponym_corners = toponym["boundedBy"]["Envelope"]
    lower_corner = toponym_corners['lowerCorner'].split(" ")
    upper_corner = toponym_corners['upperCorner'].split(" ")
    spn = [str(float(upper_corner[0]) - float(lower_corner[0])), str(float(upper_corner[1]) - float(lower_corner[1]))]

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join(spn),
        "l": "map",
        "pt": ",".join([toponym_longitude, toponym_lattitude])
    }
    return map_params

