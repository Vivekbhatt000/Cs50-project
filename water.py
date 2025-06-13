from soil import sample


def main():
    moisture = sample()
    day = 0
    print (f'Moisture is {moisture}%')

    while moisture > 20:
        moisture = sample()
        day += 1
        print(f'Day {day}: Moisture is {moisture}%')
    print('Time to water')
main()

# Don't have the soil library
