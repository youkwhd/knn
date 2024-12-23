from collections import Counter
from typing import Any

class Model:
    dataset: list[list[int | float | complex]]
    target: list[Any]
    distance: int

    def __init__(self, distance: int = 5, dataset: list[list[int | float | complex]] = [], target: list[Any] = []):
        self.distance = distance
        self.fit(dataset, target)

    def fit(self, dataset: list[list[int | float | complex]], target: list[Any]):
        assert len(dataset) == len(target)

        self.dataset = dataset
        self.target = target
    
    def classify(self, data: list[int | float | complex]) -> Any:
        dataset: list[list[Any]] = []

        for i in range(len(self.dataset)):
            _data = self.dataset[i].copy()
            _data.append(self.target[i])
            dataset.append(_data)

        for i in range(len(dataset)):
            zipped = zip(data, dataset[i][:-1])
            dataset[i].append(sum(map(lambda val: abs(val[0] - val[1]), zipped)) / len(data))

        dataset.sort(key=lambda data: data[-1])
        predictions = Counter([data[-2] for data in dataset[:self.distance]])
        return predictions.most_common(1)[0][0]
