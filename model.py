class Model:
    dataset: list[list[int | float | complex]]
    target: list[any]

    def __init__(self, dataset: list[list[int | float | complex]] = [], target: list[any] = []):
        self.fit(dataset, target)

    def fit(self, dataset: list[list[int | float | complex]], target: list[any]):
        assert len(dataset) == len(target)

        self.dataset = dataset
        self.target = target
    
    def classify(self, data: list[int | float | complex]) -> any:
        dataset: list[list[any]] = []

        for i in range(len(self.dataset)):
            data = self.dataset[i].copy()
            data.append(self.target[i])
            dataset.append(data)

        for i, v in enumerate(self.dataset):
            zipped = zip(data, v[:-1])
            dataset[i].append(sum(map(lambda val: abs(val[0] - val[1]), zipped)) / len(data))

        dataset.sort(key=lambda data: data[-1])

        hmap = {}
        for i in range(5):
            key = dataset[i][-2]

            if key not in hmap:
                hmap[key] = 0
            
            hmap[key] += 1

        predicted = None
        mmax = 0
        for k, v in hmap.items():
            if v > mmax:
                predicted = k

            mmax = max(mmax, v)

        return predicted
