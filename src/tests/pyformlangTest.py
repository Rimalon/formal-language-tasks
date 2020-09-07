import unittest
from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.finite_automaton import State
from pyformlang.finite_automaton import Symbol
from pyformlang.finite_automaton import TransitionFunction

state0 = State(0)
state1 = State(1)
state2 = State(2)
state3 = State(3)
state00 = State('0; 0')
state22 = State('2; 2')

symb_a = Symbol("a")
symb_b = Symbol("b")
symb_c = Symbol("c")
symb_d = Symbol("d")
symb_e = Symbol("e")

dfa1_transition_function = TransitionFunction()
dfa1_transition_function.add_transition(state0, symb_b, state1)
dfa1_transition_function.add_transition(state0, symb_c, state2)
dfa1 = DeterministicFiniteAutomaton(states={state0, state1, state2},
                                    input_symbols={symb_a, symb_b, symb_c},
                                    transition_function=dfa1_transition_function,
                                    start_state=state0,
                                    final_states={state1, state2})

dfa2_transition_function = TransitionFunction()
dfa2_transition_function.add_transition(state0, symb_c, state2)
dfa2_transition_function.add_transition(state0, symb_d, state1)
dfa2_transition_function.add_transition(state1, symb_d, state2)
dfa2 = DeterministicFiniteAutomaton(states={state0, state1, state2},
                                    input_symbols={symb_c, symb_d},
                                    transition_function=dfa2_transition_function,
                                    start_state=state0,
                                    final_states={state2})

dfa1_and_dfa2_transition_function = TransitionFunction()
dfa1_and_dfa2_transition_function.add_transition(state00, symb_c, state22)
dfa1_and_dfa2 = DeterministicFiniteAutomaton(states={state00, state22},
                                             input_symbols={symb_a, symb_b, symb_c, symb_d},
                                             transition_function=dfa1_and_dfa2_transition_function,
                                             start_state=state00,
                                             final_states={state22})

dfa3_transition_function = TransitionFunction()
dfa3_transition_function.add_transition(state0, symb_d, state3)
dfa3_transition_function.add_transition(state0, symb_e, state1)
dfa3_transition_function.add_transition(state1, symb_e, state0)
dfa3_transition_function.add_transition(state0, symb_c, state1)
dfa3 = DeterministicFiniteAutomaton(states={state0, state1, state3},
                                    input_symbols={symb_c, symb_d, symb_e},
                                    transition_function=dfa3_transition_function,
                                    start_state=state0,
                                    final_states={state3})


class PyformlangTestCase(unittest.TestCase):
    def test_normal_and(self):
        result = dfa1 & dfa2
        self.assertFalse(dfa1.is_equivalent_to(result))
        self.assertFalse(dfa2.is_equivalent_to(result))
        self.assertTrue(dfa1_and_dfa2.is_equivalent_to(result))

    def test_empty_result_and(self):
        self.assertTrue((dfa1 & dfa3).is_empty)

    def test_self_and(self):
        self.assertTrue(dfa1.is_equivalent_to(dfa1 & dfa1))

    def test_with_empty_and(self):
        self.assertTrue((dfa1 & DeterministicFiniteAutomaton()).is_empty)


if __name__ == '__main__':
    unittest.main()
