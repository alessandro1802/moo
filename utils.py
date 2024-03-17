import os
import glob

import gpytorch
import torch
import numpy as np


class Index:
    def __init__(self,name,runx,runy):
        self.name = name
        self.datax = runx
        self.datay = runy
        self.increase = 0
        self.pred_datax = []
        self.pred_datay = []

    def __str__(self) -> str:
        return self.name

class PredictorGP(gpytorch.models.ExactGP):
    def __init__(self, x_train, y_train, likelihood):
        super(PredictorGP, self).__init__(x_train, y_train, likelihood)
        self.mean = gpytorch.means.ConstantMean()
        self.cov = gpytorch.kernels.SpectralMixtureKernel(num_mixtures=9)
        self.cov.initialize_from_data(x_train, y_train)

    def forward(self, x):
        # Evaluate the mean and kernel function at x
        mean_x = self.mean(x)
        cov_x = self.cov(x)
        return gpytorch.distributions.MultivariateNormal(mean_x, cov_x)


def readData(dataPath):
    stock_data=[]
    for file in glob.glob(os.path.join(dataPath, "*.txt")):
        with open(file,'r') as rf:
            data = rf.readlines()
            stock_data.append(Index(data[0],
                                    [float(i.split()[0]) for i in data[2:]],
                                    [float(i.split()[1]) for i in data[2:]]))
    return stock_data

def getPredictions(stock_data):
    confidences = dict()
    for company_idx, company in enumerate(stock_data):
        # Initialize the likelihood and model
        x = torch.Tensor(company.datax)
        y = torch.Tensor(company.datay)
        likelihood = gpytorch.likelihoods.GaussianLikelihood()
        model = PredictorGP(x, y, likelihood)
        model.train()
        likelihood.train()

        optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
        mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model)

        n_iter = 1200
        for i in range(n_iter):
            optimizer.zero_grad()
            output = model(x)
            loss = -mll(output, y)
            loss.backward()
            optimizer.step()
        x_test = torch.linspace(0, 200, 200)

        model.eval()
        likelihood.eval()

        with torch.no_grad(), gpytorch.settings.fast_pred_var():
            observed_pred = likelihood(model(x_test))
            lower, upper = observed_pred.confidence_region()
            confidences[company.name] = (lower.numpy(), upper.numpy())

            company.pred_datax=list(x_test.numpy())
            company.pred_datay=list(observed_pred.mean.numpy())
        company.increase = (company.pred_datay[-1] - company.datay[-1]) / company.datay[-1]
    return stock_data, confidences

def getRiskMatrix(stock_data):
    return [[np.cov(np.stack((stock_data[i].datay, stock_data[j].datay),
                             axis=0))[0][1] for i in range(len(stock_data))] for j in range(len(stock_data))]
