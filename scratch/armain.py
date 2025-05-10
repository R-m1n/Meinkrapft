import numpy as np
import pandas as pd

class Perceptron:
    def __init__(self, features: pd.DataFrame, targets: pd.DataFrame):
        sample_size = features.shape[0]
        n_features = features.shape[1]

        train_size = int(sample_size * 0.9)

        self.features, self.targets = features.to_numpy(), targets.to_numpy()

        self.train_features = self.features[:train_size, :]
        self.train_targets = self.targets[:train_size].reshape(-1, 1)

        self.test_features = self.features[train_size:, :]
        self.test_targets = self.targets[train_size:].reshape(-1, 1)

        self.weights = np.random.normal(loc=0, scale=0.01, size=(n_features, 1))
        self.bias = np.float64(0)

        self.__activation = lambda x: np.where(x > 0, 1, 0)

    def fit(self, eta: float, epoch: int):
        
        errors = np.empty(epoch)

        for i in range(epoch):
            prediction = (self.train_features @ self.weights) + self.bias

            activated = self.__activation(prediction)

            error = (self.train_targets - activated)

            self.weights += eta * (self.train_features.T @ error)
            self.bias += eta * error.sum()

            errors[i] = self.__test()


        return errors
    
    def __test(self):
        prediction = (self.test_features @ self.weights) + self.bias

        activated = self.__activation(prediction)

        error = self.test_targets - activated

        return np.count_nonzero(error)

class Adeline:
    def __init__(self, features: pd.DataFrame, targets: pd.DataFrame, random_state: int = 42):
        sample_size = features.shape[0]
        n_features = features.shape[1]

        self.train_size = int(sample_size * 0.9)

        self.features, self.targets = features.to_numpy(), targets.to_numpy()

        self.train_features = self.features[:self.train_size, :]
        self.train_targets = self.targets[:self.train_size].reshape(-1, 1)

        self.test_features = self.features[self.train_size:, :]
        self.test_targets = self.targets[self.train_size:].reshape(-1, 1)

        self.weights = np.random.normal(loc=0, scale=0.01, size=(n_features, 1))
        self.bias = np.float64(0)

        self.__activation = lambda x: np.where(x >= 0.5, 1, 0)
        self.__rng = np.random.default_rng(seed=42)

    def fit(self, eta: float, epoch: int, batch_size: int = 1):

        batch_size = len(self.train_features) // batch_size

        errors, losses = np.empty(epoch), np.empty(epoch)
        
        for i in range(epoch):
            shuffle = self.__rng.permutation(range(len(self.train_features)))

            self.train_features = self.train_features[shuffle, :]
            self.train_targets = self.train_targets[shuffle]

            for j in range(0, len(self.train_features), batch_size):
                prediction = (self.train_features[j: j + batch_size + 1, :] @ self.weights) + self.bias

                error = (self.train_targets[j: j + batch_size + 1, :] - prediction)

                self.weights += eta * ((self.train_features[j: j + batch_size + 1, :].T @ error) / self.train_size)
                self.bias += eta * error.mean()

            errors[i] = self.__test()
            losses[i] = np.mean(np.square(error)) / 2

        return errors, losses
    
    def __test(self):
        prediction = (self.test_features @ self.weights) + self.bias

        activated = self.__activation(prediction)

        error = (self.test_targets - activated)

        return np.count_nonzero(error)