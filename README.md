# py4stat

K-Nearest Neighbors Python Library

## Getting Started

This project is simply implementation of K-Nearest Neighbors algorithm in python programming language.

### Prerequisites

This Project Has No Prerequisites


### Installing

The easiest way to install py4knn is using pip

```
pip install py4knn
```

### Usage
Coming Soon
```
from py4knn.k_nearest_neighbors import knn
classifier = knn()
x_train=[[0.23,0.54],[0.45,1.23],[1.54,0.23],[0.93,0.535]]
t_train=[0,1,0,1]
x_test=[[0.34,0.65],[0.90,0.50]]
y=classifier.predict(x_train,t_train,x_test,1,'eclidean')
```
