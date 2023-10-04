def main():
    mass = int(input('m: '))

    speed_of_light = 300000000
    energy = mass * (speed_of_light ** 2)

    # Energy in joules
    print('E: ' + str(energy))

main()