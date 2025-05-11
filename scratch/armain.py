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

    def fit(self, eta: float, epochs: int):
        
        confusions = np.empty(epochs)

        for i in np.arange(epochs):
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

        self.__shuffle_indexes = lambda x: self.__rng.permutation(np.arange(len(x)))

        indexes = self.__shuffle_indexes(features)

        self.features = features.to_numpy()[indexes, :]
        self.targets = targets.to_numpy()[indexes]

        self.train_size = int(sample_size * train_size)

        self.train_features = self.features[:self.train_size, :]
        self.train_targets = self.targets[:self.train_size].reshape(-1, 1)

        self.test_features = self.features[self.train_size:, :]
        self.test_targets = self.targets[self.train_size:].reshape(-1, 1)

        self.weights = self.__rng.normal(loc=0, scale=0.01, size=(1, n_features))
        self.bias = np.float64(0)

        self.__net_input = lambda x: x @ self.weights.T + self.bias
        self.__activation = lambda x: x
        self.__threshold = lambda x: np.where(x >= 0.5, 1, 0)

    def fit(self, eta: float, epochs: int, batch_cut: int = 1):

        batch_size = len(self.train_features) // batch_cut

        train_loss, test_loss = np.empty(epochs), np.empty(epochs)

        for i in np.arange(epochs):
            indexes = self.__shuffle_indexes(self.train_features)

            self.train_features = self.train_features[indexes, :]
            self.train_targets = self.train_targets[indexes]

            batch_loss = np.float64(0)

            for j in np.arange(0, len(self.train_features), batch_size):
                features_batch = self.train_features[j: j + batch_size, :]
                targets_batch = self.train_targets[j: j + batch_size, :]

                net_input = self.__net_input(features_batch)

                activated = self.__activation(net_input)

                error = (targets_batch - activated)

                self.weights += eta * ((features_batch.T @ error) / batch_size).T
                self.bias += eta * error.mean()

                batch_loss += np.mean(np.square(error)) / 2

            train_loss[i] = batch_loss / batch_cut
            test_loss[i] = self.__test()

        return train_loss, test_loss
    
    def predict(self, x: np.ndarray):
        net_input = self.__net_input(x)

        activated = self.__activation(net_input)

        prediction = self.__threshold(activated)

        return prediction
        
    def __test(self):
        net_input = self.__net_input(self.test_features)

        error = (self.test_targets - net_input)

        test_loss = np.mean(np.square(error)) / 2

        return test_loss

class LogisticRegression:
    def __init__(self, features: pd.DataFrame, targets: pd.DataFrame, random_state: int = 42, train_size: float = 0.9):
        sample_size = features.shape[0]
        n_features = features.shape[1]

        self.__rng = np.random.default_rng(seed=random_state)

        self.__shuffle_indexes = lambda x: self.__rng.permutation(np.arange(len(x)))

        indexes = self.__shuffle_indexes(features)

        self.features = features.to_numpy()[indexes, :]
        self.targets = targets.to_numpy()[indexes]

        self.train_size = int(sample_size * train_size)
        self.test_size = sample_size - self.train_size

        self.train_features = self.features[:self.train_size, :]
        self.train_targets = self.targets[:self.train_size].reshape(-1, 1)

        self.test_features = self.features[self.train_size:, :]
        self.test_targets = self.targets[self.train_size:].reshape(-1, 1)

        self.weights = self.__rng.normal(loc=0, scale=0.01, size=(1, n_features))
        self.bias = np.float64(0)

        self.__epsilon = 1e-15

        self.__net_input = lambda x: x @ self.weights.T + self.bias

        self.__activation = lambda x: np.clip(1. / (1. + np.exp(-np.clip(x, -250, 250))), self.__epsilon, 1 - self.__epsilon)
        
        self.__threshold = lambda x: np.where(x >= 0.5, 1, 0)

    def fit(self, eta: float, epochs: int, *, batch_cut: int = 1, l2: float = 0):

        batch_size = len(self.train_features) // batch_cut

        train_loss, test_loss = np.empty(epochs), np.empty(epochs)

        for i in np.arange(epochs):
            indexes = self.__shuffle_indexes(self.train_features)

            self.train_features = self.train_features[indexes, :]
            self.train_targets = self.train_targets[indexes]

            batch_loss = np.float64(0)
            for j in np.arange(0, len(self.train_features), batch_size):
                features_batch = self.train_features[j: j + batch_size, :]
                targets_batch = self.train_targets[j: j + batch_size, :]

                net_input = self.__net_input(features_batch)

                activated = self.__activation(net_input)

                error = targets_batch - activated

                regularization_term = (l2 * self.weights) / batch_size

                self.weights += eta * ((features_batch.T @ error) / batch_size).T + regularization_term
                self.bias += eta * error.mean()
                
                batch_loss += -np.sum(((targets_batch * np.log(activated))) + (((1 - targets_batch) * np.log(1 - activated)))) / batch_size
                batch_loss += (l2 / (2 * batch_size)) * (np.sum(np.square(self.weights)))

            train_loss[i] = batch_loss / batch_cut
            test_loss[i] = self.__test(l2)

        return train_loss, test_loss
    
    def predict(self, x: np.ndarray):
        net_input = self.__net_input(x)

        activated = self.__activation(net_input)

        prediction = self.__threshold(activated)

        return prediction
        
    def __test(self, l2: float = 0):
        net_input = self.__net_input(self.test_features)

        activated = self.__activation(net_input)

        test_loss = -np.sum((self.test_targets * np.log(activated)) + ((1 - self.test_targets) * np.log(1 - activated))) / self.test_size

        test_loss += (l2 / (2 * self.test_size)) * (np.sum(np.square(self.weights)))

        return test_loss