import sys


def main():
# tuple doesn't change value in it 
    coordinate_tuple = (42.376, -71.115) # is a tuple
    coordinate_list = [42.376, -71.115]
    latitude, longitude = coordinate_tuple
    
    print(f'Latitude: {coordinate_tuple[0]}')
    print(f'Longitude: {coordinate_tuple[1]}')
    print(f'Latitude: {latitude}')
    print(f'Latitude: {longitude}')
    print(f'{sys.getsizeof(coordinate_tuple)} bytes')
    print(f'{sys.getsizeof(coordinate_list)} bytes')
main() 