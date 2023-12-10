
def load_input(filename):
    fd = open(filename,'r')
    return [line.strip() for line in fd.readlines()]


def find_digits(string): #First exercise
    return int(''.join([x for x in string if not x.isalpha()]))

def find_digits(string):

    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    left_digit = None
    right_digit = None
    #left side:
    nearest_index = len(string) #default latest index is farthest
    for key,value in digits.items():
        found_index_word = string.find(key)
        if found_index_word != -1:
            print(f"\Word {key} found on index [{found_index_word}]")
            if found_index_word <= nearest_index:
                nearest_index = found_index_word
                left_digit = value


        found_index_digit = string.find(value)
        if found_index_digit != -1:
            print(f"\Digit {value} found on index [{found_index_digit}]")
            if found_index_digit <= nearest_index:
                nearest_index = found_index_digit
                left_digit = value
    

    #right side:
    nearest_index = 0 #default first index is closest
    for key,value in digits.items():
        found_index_word = string.rfind(key)
        if found_index_word != -1:
            print(f"\Word {key} found on index [{found_index_word}]")
            if found_index_word >= nearest_index:
                nearest_index = found_index_word
                right_digit = value


        found_index_digit = string.rfind(value)
        if found_index_digit != -1:
            print(f"\Digit {value} found on index [{found_index_digit}]")
            if found_index_digit >= nearest_index:
                nearest_index = found_index_digit
                right_digit = value

    return int(str(left_digit) + str(right_digit))

def main():

    input_data = load_input('day1_input')
    # numbers = [get_number(x) for x in input_data]
    numbers2 = [find_digits(x) for x in input_data]
    print(numbers2)
    # # # print(numbers)
    print(sum(numbers2))


if __name__ == '__main__':
    main()