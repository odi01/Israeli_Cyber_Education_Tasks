import functools


# Extra
class StopIteration(Exception):
    def __str__(self):
        return "Out of range"


# Extra function to check invalid ID number input
def check_id_input_valid(id_number):
    """
    Receive an ID number (str) and returns a True value if vaild, or False if not.
    False if the len of the number is more or less than 9 digits, or id number isn't an int,
    otherwise return True.

    :param id_number: An ID number.
    :type id_number: str
    :return: True - Valid ID number, False - Not valid.
    :rtype: Boolean
    """
    if len(id_number) == 9:
        try:
            id_number = int(id_number)
            if id_number < 100000000 or id_number == 999999999:
                raise StopIteration
            else:
                return True
        except ValueError:
            return False
    else:
        return False


# Q1
def check_id_valid(id_number):
    """
    Receive an ID number and returns a True value if it is vaild, or a False value if not.
    First, the function multiply every even index by 2.
    Second iterate each number in the list to check if it's bigger than 9,
    if so then adding the two digits number together (i.e: 12 is 1 + 2 = 3).
    Third, sum all the numbers in the list.
    Fourth, check if the sum number is divisible by 10 without a remainder,
    If so, the ID number is correct, otherwise incorrect.

    :param id_number: An ID number with a length of nine digits.
    :type id_number: int
    :return: True - Valid ID number, False - Not valid.
    :rtype: Boolean
    """

    # Step 1 - multiply every even index by 2
    multiply_nums = [int(num) * 2 if index % 2 == 0 else int(num) for index, num in enumerate(str(id_number), 1)]

    # Step 2 - check if each number is bigger than 9, if so sum the number digits together.
    adding_nums = [int(str(num)[0]) + int(str(num)[1]) if num > 9 else num for num in multiply_nums]

    # Step 3 - sum all the numbers in the list.
    sum_nums = functools.reduce(lambda x, y: x + y, adding_nums)

    # Step 4 - check if the sum number is divisible by 10 without a remainder
    if sum_nums % 10 == 0:
        return True
    else:
        return False


# Q2
class IDIterator:
    """
    Generating an iterator that create an ID number between 100 to 999 million
    one after the other.
    """

    def __init__(self, id_number = 100000000):
        """
        Receive an ID number with default value of 100 million.
        :param _id: An ID number with a length of nine digits.
        :param id_number: Save the value of the ID number from the iteration.
        :type _id: int
        :type id_number: int
        """
        self._id = [id_number, 999999999]
        self.id_num_saved = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Iterate over a ID numbers between 100 to 999 million,
        and save the value to id_number variable.
        """
        # if input is smaller than 100 million
        # or iteration number is bigger than 900 million, raise an exception
        if self.id_num_saved >= self._id[1]:
            raise StopIteration
        self.id_num_saved = self._id[0]
        self._id[0] += 1
        return self.id_num_saved


# Q 3.5
def id_generator(id_number):
    for number in range(id_number, 999999999):
        yield number


# Q3
def main():
    # Check if the id number input is 9 digits number and also an int, if True break.
    while True:
        id_input = input("Enter ID: ")
        if check_id_input_valid(id_input):
            id_input = int(id_input)
            break

    id_gen = id_generator(id_input) # Generator
    id_iter = IDIterator(id_input)  # Class
    user_choice = ""

    # Check if the input is either a "gen" or "it", otherwise reenter another input.
    while True:
        gen_or_iter = input("Generator or Iterator? (gen/it)?: ")
        if gen_or_iter == "gen":
            user_choice = id_gen
            break
        elif gen_or_iter == "it":
            user_choice = id_iter
            break
        else:
            print("ERROR, try again")

    count_valid_iter = 0
    for id_number in user_choice:
        if count_valid_iter < 10:  # Limit to 10 valid ID number outputs.
            if id_number == id_input:  # Don't count if the user ID input is a valid ID number (check_id_valid == True)
                pass
            elif check_id_valid(id_number):
                print(id_number)
                count_valid_iter += 1
        else:
            print("~ Finished ~")
            break


if __name__ == '__main__':
    main()
