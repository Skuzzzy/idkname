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

# def and_gen(index_one, index_two):
    # return lambda vals: vals[index_one] and vals[index_two]
# def nand_gen(index_one, index_two):
    # return lambda vals: not (vals[index_one] and vals[index_two])
# def or_gen(index_one, index_two):
    # return lambda vals: vals[index_one] or vals[index_two]
# def flip_index(index):
    # return lambda vals: not vals[index]
# def xor_gen(index_one, index_two):
    # return lambda vals: ((not vals[index_one]) and vals[index_two]) or (vals[index_one] and (not vals[index_two]))
# def pt_gen(index):
    # return lambda vals: vals[index]

# def xor_helper(a,b):
    # return ((not a) and b) or (a and (not b))
# def or_helper(a,b):
    # return a or b
# def and_helper(a,b):
    # return a and b

def and_type(a,b):
    return lambda vals: a(vals) and b(vals)
def nand_type(a,b):
    return lambda vals: not(a(vals) and b(vals))
def xor_type(a, b):
    return lambda vals: ((not a(vals)) and b(vals)) or (a(vals) and (not b(vals)))
def or_type(a, b):
    return lambda vals: a(vals) or b(vals)
def not_type(a):
    return lambda vals: (not a(vals))
def inx(index): # inx unwraps the values at a selected index given a list
    return lambda vals: vals[index]
def ninx(index):
    return lambda vals: not vals[index]

# Full adder
# A = 0, B = 1, Cin = 2, S, = 3, Cout = 4
full_adder = [inx(0), inx(1), inx(2), xor_type(xor_type(inx(0), inx(1)), inx(2)), or_type(and_type(xor_type(inx(0),inx(1)), inx(2)), and_type(inx(0),inx(1)))]
full_adder_relation = Relation(full_adder, [True, False, True, False, False, False])
for x in xrange(1):
    full_adder_relation = full_adder_relation.next_relation()
    print(str(([x for x in full_adder_relation.vals])))

d_ff = [inx(0), inx(1), nand_type(inx(3), nand_type(inx(0), nand_type(inx(1), inx(1)))), nand_type(inx(2), nand_type(inx(0), inx(1)))]
d_ff_relation = Relation(d_ff, [True, True, False, True])
for x in xrange(5):
    d_ff_relation = d_ff_relation.next_relation()
    print(str(([x for x in d_ff_relation.vals])))
    d_ff_relation = d_ff_relation.next_relation()
    print(str(([x for x in d_ff_relation.vals])))
    d_ff_relation = d_ff_relation.next_relation()
    print(str(([x for x in d_ff_relation.vals])))
    d_ff_relation = d_ff_relation.next_relation()
    print(str(([x for x in d_ff_relation.vals])))
    d_ff_relation = d_ff_relation.next_relation()
    print(str(([x for x in d_ff_relation.vals])))
    d_ff_relation.funcs[1] = ninx(1)
    d_ff_relation = d_ff_relation.next_relation()
    print(str(([x for x in d_ff_relation.vals])))
    d_ff_relation.funcs[1] = inx(1)
# adder = [pt_gen(0), pt_gen(1), xor_gen(0,1), and_gen(0,1)]
# half_adder = Relation(adder, [True, False, False, False])

# for x in xrange(1):
    # half_adder = half_adder.next_relation()
    # print(str(([x for x in half_adder.vals])))

# simple_relation = [RelationConst(True), flip_index(1), and_gen(0,1)]

# test_gate = Relation(simple_relation)
# test_gate.update_relation([False, False, False])
# test_gate = test_gate.next_relation()

# # print (and_gen(0,1)([True, False]))
# for x in xrange(15):
    # test_gate = test_gate.next_relation()
    # print ([x for x in test_gate.vals])
