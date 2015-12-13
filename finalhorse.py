from __future__ import print_function

class Relation:
    def __init__(self, p_funcs, p_init_state):
        if p_init_state:
            self.vals = p_init_state
        else:
            self.vals = [False] * len(p_funcs)
        self.funcs = p_funcs

    def add_func(self, func):
        self.funcs.append(func)

    def update_relation(self, p_vals):
        self.vals = []
        for n, func in enumerate(self.funcs):
            self.vals.append(func(p_vals))

    def next_relation(self):
        rel_next = Relation(self.funcs, None)
        rel_next.update_relation(self.vals)
        return rel_next

    def relval(self):
        self.update_relation()
        return self.vals[0]

class RelationConst:
    def __init__(self, truthy):
        self.const_relval = True if truthy else False

    def __call__(self, ignore):
        return self.relval()

    def update_relation(self):
        pass

    def relval(self):
        return self.const_relval

def and_gen(index_one, index_two):
    return lambda vals: vals[index_one] and vals[index_two]
def flip_index(index):
    return lambda vals: not vals[index]
def xor_gen(index_one, index_two):
    return lambda vals: ((not vals[index_one]) and vals[index_two]) or (vals[index_one] and (not vals[index_two]))
def pt_gen(index):
    return lambda vals: vals[index]

adder = [pt_gen(0), pt_gen(1), xor_gen(0,1), and_gen(0,1)]
half_adder = Relation(adder, [True, False, False, False])

for x in xrange(1):
    half_adder = half_adder.next_relation()
    print(str(([x for x in half_adder.vals])))

# simple_relation = [RelationConst(True), flip_index(1), and_gen(0,1)]

# test_gate = Relation(simple_relation)
# test_gate.update_relation([False, False, False])
# test_gate = test_gate.next_relation()

# # print (and_gen(0,1)([True, False]))
# for x in xrange(15):
    # test_gate = test_gate.next_relation()
    # print ([x for x in test_gate.vals])
