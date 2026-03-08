def findNumberOfFeatures(fileName: str) -> int:
    with open(fileName, 'r') as file:
        firstLine = file.readline()
        features = firstLine.split()
        return len(features) - 1

def findNumberOfInstances(fileName: str) -> int:
    with open(fileName, 'r') as file:
        lines = file.readlines()
        return len(lines)

def main():
    print("Welcome to Stanley's Search Algorithm!")
    print("Type in the name of the file to test : ")
    fileName = input()
    print("Type in the number of the algorithm you want to run.\n")
    print("\t1. Forward Selection")
    print("\t2. Backward Elimination")
    algorithm = input()
    numFeatures = findNumberOfFeatures(fileName)
    numInstances = findNumberOfInstances(fileName)
    print("This dataset has " + str(numFeatures) + " features (not including the class attribute), with " + str(numInstances) + " instances.")

if __name__ == "__main__":
    main()