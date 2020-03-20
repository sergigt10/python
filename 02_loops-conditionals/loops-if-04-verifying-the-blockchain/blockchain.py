# Initializing our (empty) blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)

# Comprovamos si la cadena a sido modificada
def verify_chain():
    # index del for
    block_index = 0
    is_valid = True
    for block in blockchain:
        print(block)
        # [[[[1], 10.0], 25.0], 50.0]
        print(blockchain)
        # [[[1], 10.0], [[[1], 10.0], 25.0], [[[[1], 10.0], 25.0], 50.0]]
        # Con esto obviamos la primera posición de la lista
        if block_index == 0:
            block_index += 1
            continue
        # Comparamos una posición que no sea la primera con la anterior
        # block[0] -> una posición que no sea la primera (de dentro este block escogemos su primera posicion) | blockchain[block_index - 1] -> con su anterior
        # [[[1], 50.0], [[[1], 50.0], 90.0], [[[[1], 50.0], 90.0], 100.0]]
        # Ejemplo:
        # block -> [[[[1], 50.0], 90.0], 100.0]]
        # block[0] -> escogemos su primera posicion de este block: [[[1], 50.0], 90.0] y blockchain[block_index - 1] la lista anterior -> [[[1], 50.0], 90.0]
        # [[[1], 50.0], blockchain[block_index - 1] -> [[[1], 50.0], 90.0], block -> [ block[0]-> [[[1], 50.0], 90.0] , 100.0]]
        elif block[0] == blockchain[block_index - 1]:
            print(block[0])
            print(blockchain[block_index - 1]) # blockchain[block_index - 1] -> valor anterior de la lista respecte block[0]
            is_valid = True
        else:
            print(block[0])
            # [[1], 20.0]
            print(blockchain[block_index - 1])
            # [2]
            is_valid = False
            break
        block_index += 1
    return is_valid

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print('Invalid blockchain!')
        break


print('Done!')
