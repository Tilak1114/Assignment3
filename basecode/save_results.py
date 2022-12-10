import json


class ExperimentResult:
    def __init__(self, c, acc):
        self.c_val = c
        self.accuracy = acc


class TotalError:
    def __init__(self, error):
        self.error = error


def save_results(result: list[ExperimentResult]):
    jsonStr = json.dumps([obj.__dict__ for obj in result])
    f = open("results.json", "w")
    f.write(jsonStr)
    f.close()


def save_total_errors(result: list[TotalError]):
    jsonStr = json.dumps([obj.__dict__ for obj in result])
    f = open("total_error.json", "w")
    f.write(jsonStr)
    f.close()
