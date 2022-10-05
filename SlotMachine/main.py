import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "#": 4,
    "@": 4,
    "%": 3,
    "*": 2,
    "$": 1,
    "7": 1
}

symbol_values={
    "#": 2,
    "@": 2,
    "%": 5,
    "*": 10,
    "$": 100,
    "7": 77
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    if lines == 1:
        symbol = columns[0][1]
        for column in columns:
            symbol_to_check = column[1]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
    else:
        for line in range(ROWS):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += values[symbol] * bet
        if lines == 3:
            symbol = columns[0][0]
            for i in range(3):
                symbol_to_check = columns[i][i]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += values[symbol] * bet
            symbol = columns[0][2]
            for i in range(3):
                symbol_to_check = columns[i][2-i]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += values[symbol] * bet
    return winnings

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns =[]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_spin(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row])

def deposit():
    while True:
        amt = input("What would you like to eposit? $")
        if amt.isdigit():
            amt = int (amt)
            if amt > 0:
                break
            else:
                print("Amount must greater than 0.")
        else:
            print("Please enter a number.")
    return(amt)

def get_n_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int (lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return(lines)

def get_bet():
    while True: 
        amt = input("What would you like to bet on each line? $")
        if amt.isdigit():
            amt = int (amt)
            if MIN_BET <= amt <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return(amt)


def game(balance):
    lines = get_n_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet what amount, your current balance is: ${balance}.")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_spin(slots)
    winnings = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        if balance == 0:
            break
        spin = input("Press enter to play (q to quit).")
        if spin == 'q':
            break
        balance += game(balance)
    print(f"\nYou left with ${balance}\nThank you.")

main()