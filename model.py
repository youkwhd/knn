class Model:
    dataset: list[list[int | float | complex]]
    target: list[any]

    def __init__(self):
        pass

    def __init__(self, dataset: list[list[int | float | complex]], target: list[any]):
        self.fit(dataset, target)

    def fit(self, dataset: list[list[int | float | complex]], target: list[any]):
        self.dataset = dataset
        self.target = target
    
    def classify(self, data: list[int | float | complex]):
        pass
