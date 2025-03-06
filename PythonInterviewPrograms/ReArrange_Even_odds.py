def rearrange_even_odds(input_list):
    even_numbers = []
    odd_numbers = []

    for num in input_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers+ odd_numbers


re_arrangedArray = rearrange_even_odds([1, 0, 3, 4, 5, 6, 9, 8, 9, 7])
print(f" Printing the arrnged array is {re_arrangedArray}")
