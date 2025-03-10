def convert_celsium_temp_to_kelvin():
    celsiumTemp = float(input("Enter The Temparature: "))
    kelvin = celsiumTemp + 273.15
    return round(kelvin,2)  # Result will rounded but also to Two digits after . will appear

print(convert_celsium_temp_to_kelvin())