from os import PathLike
from typing import Callable
import csv, math

def load(parse: Callable[[list[str]], list[any]], path: PathLike = "dataset/iris.csv"):
    dataset = []

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            dataset.append(row)
    
    dataset.pop(0)
    return [parse(data) for data in dataset]

def split(dataset: list[list[any]], target_idx: int = -1, n: int = 10) -> tuple[list[list[any]], list[list[any]]]:
    assert n >= 0

    train = sorted(dataset, key=lambda data: str.lower(data[target_idx]))
    test = []

    def index(lst: list, value: Callable[[any], bool]):
        for i, val in enumerate(lst):
            if value(val):
                return i

        return -1

    targets = list(set([data[target_idx] for data in train]))
    targets = sorted(targets, key=str.lower) # TODO: preserve index
    n_target_to_add = math.ceil(n / len(targets))

    for target in targets:
        n_target_to_add = min(n_target_to_add, n)

        idx = index(train, lambda data: data[target_idx] == target)
        for i in range(n_target_to_add):
            test.append(train.pop(idx + i))

        n -= n_target_to_add

    return (train, test)
