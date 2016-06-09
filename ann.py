import loader
import network2

training_data, test_data = loader.load_data_wrapper()

net = network2.Network([90,90], cost=network2.QuadraticCost)
net.large_weight_initializer()

evaluation_cost, evaluation_accuracy, training_cost, training_accuracy =\
    net.SGD(training_data[:1000], 30, 10, 0.5,
        evaluation_data=test_data, lmbda = 0.1,
        monitor_evaluation_cost=True, monitor_evaluation_accuracy=True,
        monitor_training_cost=True, monitor_training_accuracy=True)

print training_accuracy
print "\n"
print evaluation_accuracy
print "\n"
# import matplotlib.pyplot as plt
# import numpy as np
#
# training_accuracy = np.array([24146, 19740, 11306, 3595, 21213, 14844, 3593, 9908, 12481, 17614, 32015, 13160, 32208, 12579, 24630, 12128, 20511, 7014, 26218, 11787, 20669, 7055, 25695, 16553, 31979, 13903, 31048, 29503, 32423, 10164]).astype(float)
# evaluation_accuracy = np.array([2757, 2162, 1249, 436, 2210, 1595, 337, 1067, 1390, 2075, 3687, 1353, 3640, 1415, 2674, 1420, 2081, 828, 2847, 1405, 2157, 792, 2728, 1789, 3584, 1539, 3479, 3241, 3688, 1009]).astype(float)
#
# training_accuracy   /= 463715
# evaluation_accuracy /= 51630
#
# plt.plot(xrange(0,30),training_accuracy,label="Training Acc.")
# plt.plot(xrange(0,30),evaluation_accuracy,label="Test Acc.")
# plt.legend(loc=0)