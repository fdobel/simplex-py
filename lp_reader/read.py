def parse_number(number_string):
    try:
        return int(number_string)
    except ValueError:
        pass

    return float(number_string)
    #if number_string.isdigit():
    #    return int(number_string)
    #return float(number_string)


def read(filepath):
    with open(filepath, "r") as f:
        deserialized = [l.strip() for l in f.readlines()]

        objective =  deserialized[0]
        constraints = deserialized[1:]

        assert objective.startswith("obj")

        parsed_objective = [parse_number(n) for n in objective.split(" ")[1:]]
        for c in constraints:
            assert c.startswith("constraint")

        var_count = objective.split(" ").__len__() - 1

        parsed_constraints = []
        for c  in constraints:
            tmp = c.split(" ")
            assert tmp[0] == "constraint"
            assert tmp.__len__() - 3 == var_count
            left_side = [parse_number(n) for n in tmp[1:var_count + 1]]
            ctype = tmp[-2]  # == -2 == var_count + 2
            assert ctype in {'<=', '>=', '=='}
            right_side = parse_number(tmp[-1])
            parsed_constraints.append((left_side, ctype, right_side))

        return parsed_objective, parsed_constraints




