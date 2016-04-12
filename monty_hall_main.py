
import random


def is_guess_correct(car, contestant_door_choice):
    if car == contestant_door_choice:
        return True
    elif car != contestant_door_choice:
        return False


def calculate_win_percentage(win_count, number_of_simulations):
    return win_count / number_of_simulations


def print_percentage(change_door_percentage_win,
                     no_door_change_percentage_win):
    print('change door win percentage: {0:.1f}%'.format(
        change_door_percentage_win*100))
    print('not changing door win percentage: {0:.1f}%'.format(
        no_door_change_percentage_win*100))


def main():

    number_of_simulations = int(input('How many simulations would you like to '
                                'run?'))

    count = 0
    change_door_win_count = 0
    no_door_change = 0

    while count < number_of_simulations:

        doors = ['a', 'b', 'c']

        car = random.choice(doors)

        contestant_door_choice = random.choice(doors)

        if is_guess_correct(car, contestant_door_choice):
            no_door_change += 1
        else:
            change_door_win_count += 1

        count += 1
        print(count)

    change_door_percentage_win = calculate_win_percentage(
                                                         change_door_win_count,
                                                         number_of_simulations)

    no_door_change_pct_win = calculate_win_percentage(no_door_change,
                                                      number_of_simulations)

    print_percentage(change_door_percentage_win, no_door_change_pct_win)


if __name__ == "__main__":
    main()
