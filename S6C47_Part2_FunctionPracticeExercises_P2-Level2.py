''' Function Practice Exercises - Level 2'''
# Problems are arranged in increasing difficulty:

# Warmup - these can be solved using basic comparisons and methods
# Level 1 - these may involve if/then conditional statements and simple methods
# Level 2 - these may require iterating over sequences, usually with some kind of loop
# Challenging - these will take some creativity to solve


# LEVEL 2 PROBLEMS

# FIND 33:
print('\n*** F1 FIND 33: ***')
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False


def has_33_v1(num_list):
    print(f"\tThe list of numbers: {num_list}")
    for i in range(1, len(num_list)):
        if (num_list[i] == 3) and (num_list[i - 1] == 3):
            return print(f"\tThe array contains a 3 next to a 3 at positions: {i-1} and {i}\n--- ")
        else:
            continue
    return print(f"\tThe array does not contain a 3 next to a 3\n--- ")


print(f"\tVERSION 1")

has_33_v1([1, 3, 3])
has_33_v1([1, 3, 1, 3])
has_33_v1([3, 1, 3])


def has_33_v2(num_list):
    print(f"\tThe list of numbers: {num_list}")
    return print(f"\tIs there a 3 next to a 3 in this list? {'33' in ''.join(map(str, num_list))}\n--- ")


print(f"\tVERSION 2")

has_33_v2([1, 3, 3])
has_33_v2([1, 3, 1, 3])
has_33_v2([3, 1, 3])


# PAPER DOLL:
print('\n*** F2 PAPER DOLL: ***')
# Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(in_string):
    out_string = ''
    for i in range(len(in_string)):
        out_string = out_string + 3 * in_string[i]
    return print(f"\tIs there a 3 next to a 3 in this list? {out_string}\n--- ")


paper_doll('Hello')
paper_doll('Mississippi')

# BLACKJACK:
print('\n*** F3 BLACKJACK: ***')
# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


def blackjack(card_1, card_2, card_3):
    deck_list = [card_1, card_2, card_3]
    deck_sum = sum(deck_list)
    if (deck_sum <= 21):
        return print(f"\t You're at: {deck_sum} - {deck_list}\n--- ")
    elif (deck_sum > 21):
        if deck_list.count(11) == 1:
            deck_sum = deck_sum - 10
            return print(f"\t You're at: {deck_sum} - {deck_list}\n--- ")
        else:
            return print(f"\t You're 'BUST'! {deck_sum} - {deck_list}\n--- ")


blackjack(5, 6, 7)
blackjack(9, 9, 9)
blackjack(9, 9, 11)

# SUMMER OF '69:
print("\n*** F4 SUMMER OF '69: ***")
# Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer_69(years):

    years_sum = 0
    # check 6 exists in the list
    if years.count(6) != 0:
        # check 9 exists in the list
        if years.count(9) == 1:

            # get their positions
            start_out = years.index(6)
            stop_out = years.index(9)
            print(f"\tStart index: {start_out} - Stop_index: {stop_out}")

            # sum before 6
            for i in range(start_out):
                years_sum = years_sum + years[i]

            # sum after 9
            for i in range(stop_out + 1, len(years)):
                years_sum = years_sum + years[i]
            return print(f"\tYears list: {years} - sum: {years_sum}\n--- ")

        # more than one 9
        elif years.count(9) >= 1:
            return print(f"\tYears list: {years}\n\tWARNING: Too many '9's!\n--- ")
        # 9 is missing
        else:
            return print(f"\tYears list: {years}\n\tWARNING: There is no summer of 69 without the '9'!\n--- ")
    # 6 does not exist in the list
    else:
        for i in range(len(years)):
            years_sum = years_sum + years[i]
        return print(f"\tYears list: {years} - sum: {years_sum}\n--- ")


summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])
summer_69([4, 9, 5, 6, 7, 8, 9])
summer_69([4, 5, 6, 7, 8])
summer_69([])


def summer_69_v2(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print('\n--- THEND ---')
