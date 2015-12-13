def uncomment(line):
    return line.split('#')[0]


with open("CIRC.dss") as circ_file:
    lines = circ_file.read().splitlines()
    circ_file.close()
    clean_input = [uncomment(x).strip() for x in lines if (not x.strip() == '')]

    current_line = 0

    while clean_input[current_line] != "@MACRO":
        current_line += 1

    while clean_input[current_line] != "@INIT":
        # Handle Macros here
        current_line += 1

    current_line += 1 # move past init

    variable_id = 0
    variables = {}
    while clean_input[current_line] != "@TICK":
        # Handle Init here
        cur_split = clean_input[current_line].split("=")
        variables[cur_split[0].strip()] = (variable_id, True if cur_split[1].strip() == "TRUE" else False)
        variable_id += 1
        current_line += 1

    print variables
    current_line += 1 # move past tick

    code = [None] * variable_id
    sym_map = {
        "OR" : "or_type"
    }
    while current_line < len(clean_input):
        cur_split = clean_input[current_line].split("=")
        LHS = cur_split[0].strip()
        RHS = cur_split[1].strip()

        index = variables.get(LHS)[0]
        default = variables.get(LHS)[1]
        def expr(token):
            three_tokens = token[token.index('(')+1:token.rindex(')')].split()
            return sym_map[three_tokens[0]] + "(" + handle_token(three_tokens[1]) + ", " + handle_token(three_tokens[2]) + ")"

        def handle_token(token):
            if token[0] == "(":
                return expr(token)
            else:
                t_index = variables.get(token)[0]
                return "inx(" + str(t_index) + ")"
        code[index] = (handle_token(RHS), default)
        # Handle tick here
        current_line += 1
    print "[" + ", ".join(map(lambda li: li[0], code)) + "]"
    print "[" + ", ".join(map(lambda li: str(li[1]), code)) + "]"

