
from ALGORITHM_2_LFCO_2025_JR_LR_DA import PDA
from ALGORITHM_1_LFCO_2025_JR_LR_DA import generate

def print_configurations_table(input_string):
    """
    Runs the PDA on 'input_string' and prints a table of configurations
    for each step in the computation, including the applied rule.
    The table is printed only if the string is accepted by the PDA.
    """
    accepted, steps = PDA(input_string)

    if not accepted:
        return

    print(f'\nConfigurations on input "{input_string}":')
    print('-' * 89)
    print(f"|{' ' * 6}|{'CFG G':^30}|{'PDA M':^49}|\n|{'-' * 6}+{'-' * 30}+{'-' * 49}|\n"
          f"|{'Rule':^6}|{'Derivation in G':^30}|{'State':^7}|{'String':^20}|{'Stack':^20}|\n"
          f"|{'-' * 6}+{'-' * 30}+{'-' * 7}+{'-' * 20}+{'-' * 20}|")
    for i, (rule, state, string, stack) in enumerate(steps):
        derivation = f"{input_string[:(len(input_string) - len(string))]}{stack}"
        derivation = derivation if derivation else 'ε'
        string = string if string else 'ε'
        stack = stack if stack else 'ε'
        print(f"|{rule:^6}|{derivation:^30}|{state:^7}|{string:^20}|{stack:^20}|")
    print('-' * 89)

def tree():
    strings = generate()
    for s in strings:
        print_configurations_table(s)

if __name__ == "__main__":
    tree()