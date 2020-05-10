from enum import Enum

class NodeType(enum):
    HIDDEN = 0
    VISIBLE = 1
    INPUT = 2

class Node:
    def __init__(self,uid,nodeType = NodeType.VISIBLE, activation = 0):
        self.uid = uid
        self.nodeType = nodeType
        self.activation = activation
        self.touched = False

#class to store a activation function and its derivative
#with convenient application syntax and overriding ~ for the derivative
class Activation:
    def __init__(self,activation,derivative):
        self.activation = activation
        self.derivative = derivative

    def __call__(self,activity):
        self.activation(activity)

    def __invert__(self):
        self.derivative

#network class, takes an activity and a list of edges with the initial weights as input
class Network:
    def __init__(self,activity,edges = []):
        self.forwardMap = {e[0] : e for e in edges}
        self.backMap = {e[2] : e for e in edges}

    def _stepForward(self,node):
        pass

    #step the network forward by starting at the output nodes and traversing the graph backward
    #as far as possible without looping this should be the expected evaluation order for most cases
    def stepForward(self,inputs):
        pass


def main():
    print("hello world")

if __name__ == "__main__":
    main()
