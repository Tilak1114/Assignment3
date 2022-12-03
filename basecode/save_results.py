import json


class ExperimentResult:
    def __init__(self, c, acc):
        self.c_val = c
        self.accuracy = acc


def save_results(result: list[ExperimentResult]):
    jsonStr = json.dumps([obj.__dict__ for obj in result])
    f = open("results.json", "w")
    f.write(jsonStr)
    f.close()
