from lesson_26.hotels_collection import HotelsCollection

hotels = HotelsCollection('turkey_hotels')

# insert a single hotel
hotel_id = hotels.insert_hotel({'name': 'Kilikiya', 'location': 'Antalya', 'rating': 1})
print(f'Inserted hotel with ID: {hotel_id}')

# insert multiple hotels
hotels = hotels.insert_hotels([
    {'name': 'BarutHemera', 'location': 'Manavgat', 'rating': 3},
    {'name': 'PineHouse', 'location': 'Camyva', 'rating': 3},
    {'name': 'MardanPalace', 'location': 'Lara', 'rating': 7},
    {'name': 'Titanic', 'location': 'Lara', 'rating': 4}
])
print(f'Inserted hotels with IDs: {hotels}')

# find a single hotel
# hotel = hotels.find_one_by_name('PineHouse')
# print(f'Found hotel: {hotel["name"]} with ID - {hotel["_id"]}')

# # find all by locations
# hotels = hotels.find_many_by_location('Manavgat')
# for find_location_record in hotels:
#     print('_id:', find_location_record['_id'], 'location:', find_location_record['location'])

# find hotels with min.rating
# hotels = hotels.find_many_by_rating(3)
# for hotel_with_min_rating in hotels:
#     print(hotel_with_min_rating)
#
# # delete hotel by ID
# deleted_hotel = hotels.delete_one_hotel_by_id("ObjectId('644da46dbde8142c7d273352'")
# print(f'Hotel deleted')

# delete all hotels
# result = hotels.delete_all_hotels()
# print(f'Deleted all hotels')

# find all hotels
# hotels = hotels.find_all_hotels()
# for hotel in hotels:
#     print(hotel)
