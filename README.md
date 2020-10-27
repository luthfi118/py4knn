# py4knn

K-Nearest Neighbors Python Library

## Getting Started

This project is simply an implementation of K-Nearest Neighbors algorithm in python programming language.

### Prerequisites

This Project Has No Prerequisites


### Installing

The easiest way to install py4knn is by using pip

```
pip install py4knn
```

### Usage
There is only 1 public method of knn class. It is predict method, it takes 5 argument namely ```x_train```, ```t_train```, ```x_test```, ```k```, and ```distance``` calculation method. We provide 6 distances namely euclidean, squared_euclidean, manhattan, canberra, chebyshev, and bray_curtis.
```
from py4knn.k_nearest_neighbors import knn
classifier = knn()
x_train = [[0.23,0.54],[0.45,1.23],[1.54,0.23],[0.93,0.535]]
t_train = [0,1,0,1]
x_test = [[0.34,0.65],[0.90,0.50]]
y = classifier.predict(x_train,t_train,x_test,1,'euclidean')
```
