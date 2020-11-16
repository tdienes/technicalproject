import math
import matplotlib.pyplot as plt
import numpy

def calcDH2(H, T):
    total = 0
    vals = numpy.linspace(0, 1, 100)
    for i in vals:
        theta = i
        hpart = math.pow(theta, H)
        tpart = math.pow(float(1.0-theta), T)
        total += hpart*tpart*0.01
    return total

def calcLogRatio(H, T, h1, h2):
    DH1 = (0.5)**(H+T)
    DH2 = calcDH2(H, T)
    return math.log(DH1/DH2)+math.log(h1/h2)

def logTransform(H, T, a, b, h1, h2):
    innerVal = -a*calcLogRatio(H,T,h1,h2)+b
    expVal = math.exp(innerVal)
    return 1/(1+expVal)

vals = dict()

part1 = [1,5,7,1,6,7,2,6,7]
part2 = [1,6,7,1,6,7,3,5,7]
me1 = [3,4,4,4,4,6,3,4,5]
me2 = [2,3,3,3,3,5,2,3,4]
h1 = 0.5
h2 = 1-h1

for a in [0.8]:
    for b in [1]:
        temp = []
        temp.append(7-logTransform(3, 2, a, b, h1, h2)*7)
        temp.append(7-logTransform(1, 4, a, b, h1, h2)*7)
        temp.append(7-logTransform(5, 0, a, b, h1, h2)*7)
        temp.append(7-logTransform(4, 6, a, b, h1, h2)*7)
        temp.append(7-logTransform(8, 2, a, b, h1, h2)*7)
        temp.append(7-logTransform(0, 10, a, b, h1, h2)*7)
        temp.append(7-logTransform(10, 16, a, b, h1, h2)*7)
        temp.append(7-logTransform(21, 5, a, b, h1, h2)*7)
        temp.append(7-logTransform(26, 0, a, b, h1, h2)*7)
        print(temp)
        vals[(a,b)] = temp
        plt.plot(part1, temp, 'ro', label = "participant 1")
        plt.plot(me1, temp, 'g^', label = "my data")
        part1fit = numpy.polyfit(part1, temp, 1)
        me1fit = numpy.polyfit(me1, temp, 1)
        part1fitliney = []
        me1fitliney = []

        for i in range(len(part1)):
            part1fitliney.append(part1fit[0]*part1[i]+part1fit[1])
            me1fitliney.append(me1fit[0]*me1[i]+me1fit[1])

        plt.plot(part1, part1fitliney, 'r', label = "best fit line, participant 1")
        plt.plot(me1, me1fitliney, 'g', label = "best fit line, me")
        plt.xlabel("participant data")
        plt.ylabel("model")
        plt.legend()
        plt.title("Experiment 1, a = " + str(a) + " b = " + str(b) + ", corr 1: " + str(round(numpy.corrcoef(part1, temp)[0][1],2)) + " and corr 2: " + str(round(numpy.corrcoef(me1, temp)[0][1],2)))
        plt.show()

        ##exp 2
        plt.plot(part2, temp, 'ro', label = "participant 2")
        plt.plot(me2, temp, 'g^', label = "my data")
        part2fit = numpy.polyfit(part2, temp, 1)
        me2fit = numpy.polyfit(me2, temp, 1)
        part2fitliney = []
        me2fitliney = []

        for i in range(len(part1)):
            part2fitliney.append(part2fit[0]*part2[i]+part2fit[1])
            me2fitliney.append(me2fit[0]*me2[i]+me2fit[1])

        plt.plot(part2, part2fitliney, 'r', label = "best fit line, participant 2")
        plt.plot(me2, me2fitliney, 'g', label = "best fit line, me")
        plt.xlabel("participant data")
        plt.ylabel("model")
        plt.legend()
        plt.title("Experiment 2, a = " + str(a) + " b = " + str(b) + ", corr 1: " + str(round(numpy.corrcoef(part2, temp)[0][1],2)) + " corr 2: " + str(round(numpy.corrcoef(me2, temp)[0][1],2)))
        plt.show()
