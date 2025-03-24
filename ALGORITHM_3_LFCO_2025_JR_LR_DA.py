
# Define PDA transitions
transitions = [
    [[0, 'σ', 'γ'], [0, 'σγ']],
    [[0, '', 'γ'], [1, 'γ']],
    [[0, 'σ', 'γ'], [1, 'γ']],
    [[1, 'σ', 'σ'], [1, '']],
]

starting_state = 0
final_state = 1

# Dictionary mapping transitions to rule descriptions.
TRANSITION_RULES = {
    ((0, 'σ', 'γ'), (0, 'σγ')): "Push symbol (like S -> σSσ)",
    ((0, '', 'γ'), (1, 'γ')):   "Epsilon to state 1",
    ((0, 'σ', 'γ'), (1, 'γ')):  "Transition to state 1 reading symbol",
    ((1, 'σ', 'σ'), (1, '')):   "Pop matching symbol",
}

# Pushdown Automaton (PDA) function with step tracking and rule logging
def PDA(string, index=0, stack=['⊥'], state=starting_state, steps=None, rule="Start"):
    if steps is None:
        steps = []  # Initialize step list

    # Store the current configuration with the applied rule
    steps.append((state, string[index:], stack.copy(), rule))

    # Acceptance condition
    if index == len(string) and state == final_state:
        return stack == ['⊥'], steps  # Return result and steps

    for transition in transitions:
        [current_state, input_symbol, stack_top], [next_state, stack_action] = transition

        if state == current_state:
            if input_symbol == 'σ' and index < len(string):
                current_symbol = string[index]

                if stack_top == 'γ':
                    if stack_action == 'σγ' and current_symbol is not None:
                        new_stack = stack.copy()
                        new_stack.append(current_symbol)
                        key = (tuple([current_state, input_symbol, stack_top]),
                               tuple([next_state, stack_action]))
                        new_rule = TRANSITION_RULES.get(key, "Unknown")
                        is_accepted, new_steps = PDA(string, index + 1, new_stack, next_state, steps, new_rule)
                        if is_accepted:
                            return True, new_steps

                    elif stack_action == 'γ':
                        new_stack = stack.copy()
                        key = (tuple([current_state, input_symbol, stack_top]),
                               tuple([next_state, stack_action]))
                        new_rule = TRANSITION_RULES.get(key, "Unknown")
                        is_accepted, new_steps = PDA(string, index + 1, new_stack, next_state, steps, new_rule)
                        if is_accepted:
                            return True, new_steps

                elif stack_top == 'σ' and stack[-1] == current_symbol:
                    new_stack = stack.copy()
                    new_stack.pop()
                    key = (tuple([current_state, input_symbol, stack_top]),
                           tuple([next_state, stack_action]))
                    new_rule = TRANSITION_RULES.get(key, "Unknown")
                    is_accepted, new_steps = PDA(string, index + 1, new_stack, next_state, steps, new_rule)
                    if is_accepted:
                        return True, new_steps

            elif input_symbol == '':
                key = (tuple([current_state, input_symbol, stack_top]),
                       tuple([next_state, stack_action]))
                new_rule = TRANSITION_RULES.get(key, "Unknown")
                is_accepted, new_steps = PDA(string, index, stack.copy(), next_state, steps, new_rule)
                if is_accepted:
                    return True, new_steps

    return False, steps  # Return steps even if the string is not accepted