
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def get_them(list_of_lists):
    """A very poor example of a function. This code is NOT clean.
    This is not clean for many reasons. Mostly that we have to know what list_of_lists is composed of in order to decipher it.
    What things are in the list?
    What is the 0th index of an item in the list about?
    What does 4 mean?
    How can I use the returned list?
    """
    to_return = []
    for l in list_of_lists:
        if l[0] == 4:
            to_return.append(l)
    return to_return


def get_flagged_cells(gameboard):
    """This is clean code that does the same as the above example, except it is understandable throughout."""
    flagged_cells = []
    for cell in gameboard:
        if cell[STATUS_VALUE] == FLAGGED:
            flagged_cells.append(cell)
    return flagged_cells


def get_flagged_cells(gameboard):
    """This is another example that is written through the use of a cell class."""
    flagged_cells = []
    for cell in gameboard:
        if cell.is_flagged():
            flagged_cells.append(cell)
    return flagged_cells

    # consider
    def copy_string(a1, a2)

    # vs
    def copy_string(source, destination)

    # how can you tell the difference in these function calls by how they are named?
    get_account()
    get_accounts()
    get_account_info()
    # a renaming of these functions is almost necessary for other programmers to use them

    # use searchable names
    WORK_DAYS_PER_WEEK = 5

    # it is much easier to searh for WORK_DAYS_PER_WEEK than it is to search for the number 5

    # forget about prefixes, consider the two ways to name this string variable of Part
    class Part:
        __init__(self, description):
        self.m_desc = description
        self.description = description


# classes should be nouns, functions should be verbs
first_floor = Blueprint()
scan_blueprint(first_floor)

# say what you mean
whack()
vs
kill()
gtfo()
vs
abort()

# don't use the same thing for different things, consider
Cumulator.add(num)
Accounts.add(account)
# one of these should be renamed so that they aren't confused. A good option is to rename Accounts.add() to
Accounts.append(account)

# Add context to your variables, consider
state
addrState
sysState
address.state
system.state