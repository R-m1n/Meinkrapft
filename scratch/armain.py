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

        self.weights = np.random.normal(loc=0, scale=0.01, size=(1, n_features))
        self.bias = np.float64(0)

        self.__net_input = lambda x: x @ self.weights.T + self.bias
        self.__activation = lambda x: np.where(x > 0, 1, 0)

    def fit(self, eta: float, epoch: int):
        
        confusions = np.empty(epoch)

        for i in range(epoch):
            net_input = self.__net_input(self.train_features)

            activated = self.__activation(net_input)

            error = (self.train_targets - activated)

            self.weights += eta * (self.train_features.T @ error).T
            self.bias += eta * error.sum()

            confusions[i] = self.__test()

        return confusions
    
    def predict(self, x: np.ndarray):
        net_input = self.__net_input(x)

        prediction = self.__activation(net_input)

        return prediction
    
    def __test(self):
        net_input = self.__net_input(self.test_features)

        activated = self.__activation(net_input)

        error = self.test_targets - activated

        return np.count_nonzero(error)

class Adeline:
    def __init__(self, features: pd.DataFrame, targets: pd.DataFrame, random_state: int = 42, train_size: float = 0.9):
        sample_size = features.shape[0]
        n_features = features.shape[1]

        self.__rng = np.random.default_rng(seed=random_state)

        self.__shuffle = lambda x: self.__rng.permutation(range(len(x)))

        self.features = features.to_numpy()[self.__shuffle(features), :]
        self.targets = targets.to_numpy()[self.__shuffle(targets)]

        self.train_size = int(sample_size * train_size)

        self.train_features = self.features[:self.train_size, :]
        self.train_targets = self.targets[:self.train_size].reshape(-1, 1)

        self.test_features = self.features[self.train_size:, :]
        self.test_targets = self.targets[self.train_size:].reshape(-1, 1)

        self.weights = np.random.normal(loc=0, scale=0.01, size=(1, n_features))
        self.bias = np.float64(0)

        self.__net_input = lambda x: x @ self.weights.T + self.bias
        self.__activation = lambda x: x
        self.__threshold = lambda x: np.where(x >= 0.5, 1, 0)

    def fit(self, eta: float, epoch: int, batch_cut: int = 1):

        batch_size = len(self.train_features) // batch_cut

        train_loss, test_loss = np.empty(epoch), np.empty(epoch)
        
        for i in range(epoch):
            self.train_features = self.train_features[self.__shuffle(self.train_features), :]
            self.train_targets = self.train_targets[self.__shuffle(self.train_targets)]

            errors = np.empty(batch_cut)

            batch_counter = 0
            for j in range(0, len(self.train_features), batch_size):
                net_input = self.__net_input(self.train_features[j: j + batch_size + 1, :])

                activated = self.__activation(net_input)

                error = (self.train_targets[j: j + batch_size + 1, :] - activated)

                self.weights += eta * ((self.train_features[j: j + batch_size + 1, :].T @ error) / self.train_size).T
                self.bias += eta * error.mean()

                errors[batch_counter] = error.sum()
                batch_counter += 1

            train_loss[i] = np.mean(np.square(errors)) / 2
            test_loss[i] = self.__test()

        return train_loss, test_loss
    
    def predict(self, x: np.ndarray):
        net_input = self.__net_input(x)

        activated = self.__activation(net_input)

        prediction = self.__threshold(activated)

        return prediction
        
    def __test(self):
        net_input = self.__net_input(self.test_features)

        errors = (self.test_targets - net_input)

        test_loss = np.mean(np.square(errors)) / 2

        return test_loss