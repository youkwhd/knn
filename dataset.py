from os import PathLike
from typing import Callable, Any
import csv, math

def load(path: str | PathLike = "dataset/iris.csv"):
    dataset = []

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            dataset.append(row)
    
    # Remove the header
    dataset.pop(0)

    # TODO: this good?
    def parse(data: list[str]) -> list[Any]:
        _data: list[Any] = data

        for i in range(len(_data)):
            try:
                _data[i] = int(_data[i])
            except:
                try:
                    _data[i] = float(_data[i])
                except:
                    pass

        return _data

    return [parse(data) for data in dataset]

def split(dataset: list[list[Any]], target_idx: int = -1, n: int = 10) -> tuple[list[list[Any]], list[list[Any]]]:
    assert n >= 0

    train = sorted(dataset, key=lambda data: data[target_idx]) # TODO: make sure string is lowered
    test = []

    def index(lst: list, value: Callable[[Any], bool]):
        for i, val in enumerate(lst):
            if value(val):
                return i

        return -1

    targets = list(set([data[target_idx] for data in train]))
    targets = sorted(targets) # TODO: preserve index
    n_target_to_add = math.ceil(n / len(targets))

    for target in targets:
        n_target_to_add = min(n_target_to_add, n)

        idx = index(train, lambda data: data[target_idx] == target)
        for i in range(n_target_to_add):
            test.append(train.pop(idx + i))

        n -= n_target_to_add

    return (train, test)

def enumize(dataset: list[list[Any]]) -> list[list[int | float | complex]]:
    for i, v in enumerate(dataset[0]):
        if not isinstance(v, str):
            continue

        categories = {}
        for j, category in enumerate(set([data[i] for data in dataset])):
            categories[category] = j + 1

        for j in range(len(dataset)):
            dataset[j][i] = categories[dataset[j][i]]

    return dataset
