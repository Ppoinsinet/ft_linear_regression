def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def readValues():
    try:
        file = open("./result", "r")
        str = file.read()
        tab = str.split("|")

        if len(tab) != 2:
            print("Incorrect formatting of result file")
            exit(2)
        return [float(tab[0]), float(tab[1])]

    except:
        print("No results were detected or incorrect formatting.")
        return [0.0, 0.0]
    
[theta0, theta1] = readValues()
print("Theta0 : " + str(theta0))
print("Theta1 : " + str(theta1) + "\n")

val = input("Please specify mileage : ")
if is_float(val) == False:
    print("Incorrect input")
    exit(1)

r = theta0 + (theta1 * float(val))
print("Predicted price : " + str(r))
