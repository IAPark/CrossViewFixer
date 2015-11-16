from pybrain import TanhLayer
from pybrain.datasets import ClassificationDataSet
from pybrain.supervised import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.xml import NetworkWriter, NetworkReader
import training_set
from converter.CV import split, get_net_input

ds = ClassificationDataSet.loadFromFile("data2")


#net = buildNetwork(27, 100, 100, 100, 100, 100, 100, 2, bias=True, outclass=TanhLayer)

print("training")

net = NetworkReader.readFrom("net")
trainer = BackpropTrainer(net, ds, learningrate=0.01)

trainer.trainUntilConvergence(verbose=True, maxEpochs=500)

'''for i in range(1000):
    r = trainer.train()
    if i % 10 == 0:
        print(i, r)
'''

NetworkWriter.writeToFile(net, "net")
print("saved")
sum = 0
wrong = 0
attempted = 0
for u in training_set.l:
    right, left = split(u)
    data = get_net_input(right, left)
    activation = net.activate(data)

    print(u + ": cv " + str(activation))
    sum += activation
    attempted += 1
    if activation[0] > 0.5 or activation[1] < 0.5:
        wrong += 1
        print(u + ": is wrong")


print(sum)
sum = 0

for u in training_set.l:
    left, right = split(u)
    data = get_net_input(right, left)
    activation = net.activate(data)

    print(u + ": pv " + str(activation))
    sum += activation
    attempted += 1
    if activation[0] < 0.5 or activation[1] > 0.5:
        wrong += 1
        print(u + ": is wrong when inverted")
print(sum)
print(float(wrong)/attempted)

wrong = 0
attempted = 0
for inpt, target in ds:
    activation = net.activate(inpt)
    if target[0] == 1:
        if activation[0] < 0.5 or activation[1] > 0.5:
            wrong += 1
    else:
        if activation[0] > 0.5 or activation[1] < 0.5:
            wrong += 1
    attempted += 1

print(float(wrong)/attempted)
