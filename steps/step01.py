class Variable:
    def __init__(self, data):
        self.data = data


if __name__ == "__main__":
    import numpy as np

    data = np.array(1.6)
    x = Variable(data)
    print(x.data)
    print(type(x.data))