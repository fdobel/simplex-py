

def read(filepath):
    with open(filepath, "r") as f:
        deserialized = [l.strip() for l in f.readlines()]

        objective =  deserialized[0]
        constraints = deserialized[1:]

        assert objective.startswith("obj")
        for c in constraints:
            assert c.startswith("constraint")

        var_count = objective.split(" ").__len__() - 1
        for c  in constraints:
            assert c.split(" ").__len__() - 2 == var_count

        return objective, constraints




