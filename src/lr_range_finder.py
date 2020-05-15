#
# Copyright (c) 2020. Asutosh Nayak (nayak.asutosh@ymail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#

import pickle
import numpy as np
from matplotlib import pyplot as plt

class LrRangeFinder:
    def __init__(self, num_batches, **kwargs):
        if 'x' in kwargs and 'y' in kwargs:
            self.x = kwargs['x']
            self.y = kwargs['y']
        else:
            if 'data_path' not in kwargs:
                raise ValueError("Either x and y ndarrays or (x, y) tuple dump path is needed")
            self.data_path = kwargs['data_path']
            data = pickle.load(open(self.data_path, 'rb'))
            if type(data) is not tuple:
                raise ValueError('Saved data must be a tuple of form (x, y)')
            self.x, self.y = data

        self.iterations = 0
        self.lr_low = kwargs['lr_low']
        self.lr_high = kwargs['lr_high']
        self.lr_step = (self.lr_high/self.lr_low)**(1/num_batches)
        self.losses = []
        self.lrs = []
        self.best_loss = np.inf

    def get_next_lr(self, loss):
        self.iterations += 1   
        if self.iterations == 1:
            # no loss expected for first iter
            lr = self.lr_low*(self.lr_step**self.iterations)
            self.lrs.append(lr)
            return lr
        if loss==None:
            raise ValueError("'loss' is required, except for first iteration")
        if loss < self.best_loss:
            self.best_loss = loss
        if loss == np.nan or loss > 5*self.best_loss:
            return None
        self.losses.append(loss)  # this is loss for previous lr
        lr = self.lr_low*(self.lr_step**self.iterations)
        self.lrs.append(lr)
        return lr

    def plot_lr(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.lrs[:-1], self.losses)  # last loss would be the once which caused exit condition
        plt.xticks(np.arange(min(self.lrs[:-1]), max(self.lrs[:-1]), 0.0001))
        plt.title('LR range plot')
        plt.xlabel('Learning rates')
        plt.ylabel('Losses')
        plt.show()