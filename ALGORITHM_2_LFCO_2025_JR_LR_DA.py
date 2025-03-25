from ALGORITHM_1_LFCO_2025_JR_LR_DA import generate

initial_stack_symbol = 'Ψ'      # Initial stack symbol
starting_state = 'q'              # Starting state
final_state = 'q'                 # Final state

# ω ∈ Σ = {a,b,c, ..., z}         Σ <- input alphabet
# Ω ∈ Γ = {Ψ, A, B, C, ..., Z}    Γ <- stack alphabet

transitions = [                         #  |         |      CFG      |              PDA             |
    [['q', 'ω', 'Ψ'], ['q', 'ΨΩ']],     #  |     I.  |    Ψ -> ωΨΩ   |     (q, ω, Ψ) -> (q, ΨΩ)     |
    [['q', 'ω', 'Ψ'], ['q', '']],       #  |    II.  |    Ψ -> ω     |     (q, ω, Ψ) -> (q, ε)      |
    [['q', '', 'Ψ'], ['q', '']],        #  |   III.  |    Ψ -> ε     |     (q, ε, Ψ) -> (q, ε)      |
    [['q', 'ω', 'Ω'], ['q', '']]        #  |    IV.  |    Ω -> ω     |     (q, ω, Ω) -> (q, ε)      |
]

"""
This transitions apply to all the strings in the language, where Ψ is the initial stack symbol,
ε is the empty string, and ω is a symbol from the input alphabet. Ω is specifically a symbol
from the stack alphabet Γ that corresponds to ω in the input alphabet Σ, meaning it is not any
arbitrary symbol but rather a respective uppercase version of ω.
"""

def PDA(string, index=0, stack=initial_stack_symbol, state=starting_state, steps = [], rule = ""):

    new_steps = steps.copy()
    new_steps.append((rule, state, string[index:], stack))

    if index == len(string) and state == final_state and stack == "":
        return  True, new_steps

    for transition in transitions:
        [current_state, input_symbol, stack_top], [next_state, stack_action] = transition

        if state == current_state:

            if input_symbol == 'ω' and index < len(string):
                if stack_top == 'Ψ' and stack and stack[0] == 'Ψ':
                    # I
                    if stack_action == 'ΨΩ' and string[index] is not None:
                        new_stack = 'Ψ' + string[index].upper() + stack[1:]
                        next_test, successful_steps = PDA(string, index + 1, new_stack, next_state, new_steps, " I")
                        if next_test:
                            return True, successful_steps

                    # II
                    elif stack_action == '' and stack:
                        new_stack = stack[1:]
                        next_test, successful_steps = PDA(string, index + 1, new_stack, next_state, new_steps, "II")
                        if next_test:
                            return True, successful_steps

                # IV
                elif stack_top == 'Ω' and stack and stack[0] == string[index].upper():
                    new_stack = stack[1:]
                    next_test, successful_steps = PDA(string, index + 1, new_stack, next_state, new_steps, "IV")
                    if next_test:
                        return True, successful_steps
            # III
            elif input_symbol == '' and stack and stack[0] == 'Ψ':
                new_stack = stack[1:]
                next_test, successful_steps = PDA(string, index, new_stack, next_state, new_steps, "III")
                if next_test:
                    return True, successful_steps
    return False, steps


def mainPDA():
    strings = generate()
    print("\nStrings Accepted and Rejected by the PDA:")
    accepted = []
    rejected = []
    for string in strings:
        if PDA(string)[0]:
            accepted.append(string)
        else:
            rejected.append(string)

    print('-' * 63)
    print(f"|{'ACCEPTED':^30}|{'REJECTED':^30}|\n"
          f"|{'-' * 30}+{'-' * 30}|")

    for i in range(max(len(accepted), len(rejected))):
        string_accepted = accepted[i] if i < len(accepted) else ''
        string_accepted = 'ε' if not string_accepted and i < len(accepted) else string_accepted
        string_rejected = rejected[i] if i < len(rejected) else ''
        print(f"|{string_accepted:^30}|{string_rejected:^30}|")
    print('-' * 63)

if __name__ == "__main__":
    mainPDA()

