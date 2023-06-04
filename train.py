import matplotlib.pyplot as plt

learningRate = 0.001

def openFile():
    try:
        file = open("./data.csv")
        content = file.read()
    except FileNotFoundError:
        print("Could not find data file 'data.csv'")
        exit(1)

    lines = content.split("\n")
    lines.pop(0)
    return lines    

def getData(file):
    x = []
    y = []
    data = []

    for line in file:
        tab = line.split(",")
        if (len(tab) == 2):
            x.append(float(tab[0]))
            y.append(float(tab[1]))
            data.append([float(tab[0]), float(tab[1])])
    
    max_value = max(x)
    length = len(x)
    normalized_data = []

    for i in range(length):
        normalized_data.append([x[i]/max_value, y[i]/max_value])

    return [data, normalized_data]

def predict(theta0, theta1, x):
    return theta0 + (theta1 * x)

def get_sum(data, theta0, theta1, param = 0):
    result = 0
    for iteration in data:
        result += (predict(theta0, theta1, iteration[0]) - iteration[1]) * (iteration[0] if param == 1 else 1)
    return result

def compute_coefs(data, theta0, theta1):
    length = len(data)
    diff0 = learningRate * (1/length) * get_sum(data, theta0, theta1)
    diff1 = learningRate * (1/length) * get_sum(data, theta0, theta1, 1)
    return [theta0 - diff0, theta1 - diff1]

def compute_error(data, theta0, theta1):
    result = 0

    for it in data:
        p = predict(theta0, theta1, it[0])
        result += abs(p - it[1]) / it[1]

    return 1 - (result/len(data))

file = openFile()
data = []
normalized_data = []
[data, normalized_data] = getData(file)

x = []
y = []

for it in data:
    x.append(it[0])
    y.append(it[1])

theta0 = 0
theta1 = 0
iterations = 0

while 1:
    [theta0, theta1] = compute_coefs(normalized_data, theta0, theta1)
    if iterations % 10000 == 0 and iterations > 0:
        print(str(iterations) + " iterations")
        print("Accuracy : " + str(compute_error(normalized_data, theta0, theta1)))
        stop = input("stop ? (y/n) ")
        if stop == "y":
            break
    iterations += 1

theta0 *= max(x)
print("theta0 : " + str(theta0))
print("theta1 : " + str(theta1))

predicted = []
for it in x:
    predicted.append(predict(theta0, theta1, it))

output = open("result", "w")
output.write(str(theta0) + "|" + str(theta1))
output.close()

plt.plot(x, predicted)
plt.plot(x, y, "bo")

plt.show()