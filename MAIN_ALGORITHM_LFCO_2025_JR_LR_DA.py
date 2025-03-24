from ALGORITHM_3_LFCO_2025_JR_LR_DA import PDA
from ALGORITHM_1_LFCO_2025_JR_LR_DA import generate

def print_configurations_table(input_string):
    """
    Runs the PDA on 'input_string' and prints a table of configurations
    for each step in the computation, including the applied rule.
    The table is printed only if the string is accepted by the PDA.
    """
    accepted, steps = PDA(input_string)

    if not accepted:
        print(f"\nString '{input_string}' was REJECTED. Skipping tree generation.\n")
        return

    print(f"\nConfigurations of M on input '{input_string}':")
    print("-" * 100)
    print(f"{'Step':^5} | {'State':^5} | {'Remaining Input':^20} | {'Stack':^20} | {'Rule':^30}")
    print("-" * 100)

    for i, (state, remaining, stack, rule) in enumerate(steps):
        remaining_str = remaining if remaining else 'ε'
        stack_str = ''.join(stack) if stack else 'ε'
        print(f"{i:^5} | q{state:^4} | {remaining_str:^20} | {stack_str:^20} | {rule:^30}")

    print("-" * 100),
    print("Result: ACCEPTED")
    print("-" * 100)

def tree():
    strings = generate()
    for s in strings:
        print_configurations_table(s)

if __name__ == "__main__":
    tree()