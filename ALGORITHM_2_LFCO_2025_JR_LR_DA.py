transitions = [
    [[0, 'σ', 'γ'], [0, 'σγ']],
    [[0, '', 'γ'], [1, 'γ']],
    [[0, 'σ', 'γ'], [1, 'γ']],
    [[1, 'σ', 'σ'], [1, '']],
]

starting_state = 0
final_state = 1

def PDA(string, index=0, stack=['⊥'], state=starting_state):

    if index == len(string) and state == final_state:
        return  stack == ['⊥']

    for transition in transitions:
        [current_state, input_symbol, stack_top], [next_state, stack_action] = transition

        if state == current_state:
            if input_symbol == 'σ' and index < len(string):
                current_symbol = string[index]

                if stack_top == 'γ':
                    if stack_action == 'σγ' and current_symbol is not None:
                        new_stack = stack.copy()
                        new_stack.append(current_symbol)
                        if PDA(string, index + 1, new_stack, next_state):
                            return True

                    elif stack_action == 'γ':
                        if PDA(string, index + 1, stack.copy(), next_state):
                            return True

                elif stack_top == 'σ' and stack[-1] == current_symbol:
                    new_stack = stack.copy()
                    new_stack.pop()
                    if PDA(string, index + 1, new_stack, next_state):
                        return True

            elif input_symbol == '':
                if PDA(string, index, stack.copy(), next_state):
                    return True

    return False


string = ("yohagoyogahoy")
print(PDA(string))