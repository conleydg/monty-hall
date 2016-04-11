import random


def host_opens_door(car, contestant_door_choice, number_of_doors,
                    doors_duplicate):
    doors_duplicate.remove(car)
    try:
        doors_duplicate.remove(contestant_door_choice)
    except:
        pass
    return random.choice(doors_duplicate)


def main():

    number_of_doors = int(input('How many doors would you like to play with?'))

    number_of_simulations = int(input('How many simulations would you like to '
                                'run?'))

    while int(number_of_doors) > 2:
        count = 0
        change_door_win_count = 0
        no_door_change = 0

        while count < number_of_simulations:
            doors = list(range(0, int(number_of_doors)))
            doors_duplicate = list(range(0, int(number_of_doors)))

            car = random.choice(doors)

            contestant_door_choice = random.choice(doors)

            host_door = host_opens_door(car, contestant_door_choice,
                                        number_of_doors, doors_duplicate)

            if car == contestant_door_choice:
                no_door_change += 1
            doors.remove(contestant_door_choice)
            doors.remove(host_door)
            contestant_second_guess = random.choice(doors)
            if car == contestant_second_guess:
                change_door_win_count += 1

            count += 1
        print(number_of_doors)
        change_door_percentage_win = (change_door_win_count / (
            number_of_simulations))

        no_door_change_percentage_win = no_door_change / number_of_simulations

        print('change door win percentage: {0:.1f}%'.format(
            change_door_percentage_win*100))

        print('not changing door win percentage: {0:.1f}%'.format(
            no_door_change_percentage_win*100))
        number_of_doors -= 1


if __name__ == "__main__":
    main()
