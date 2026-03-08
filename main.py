import math

def organizeData(fileName: str) -> tuple[list[list[float]], list[int]]:
    data: list[list[float]] = []
    classes: list[int] = []
    with open(fileName, "r") as f:
        for line in f:
            values: list[str] = line.split()
            if not values: continue
            classes.append(int(float(values[0])))
            data.append([float(x) for x in values[1:]])
    return data, classes

def euclideanDistance(x: list[float], y: list[float], featureIndices: set[int]) -> float:
    return math.sqrt(sum([(x[i] - y[i]) ** 2 for i in featureIndices]))

def nearestNeighbor(data: list[list[float]], classes: list[int], featureIndices: set[int]) -> float:
    n: int = len(data) # of instances
    correct: int = 0
    for i in range(n):
        nearestNeighborDistance: float = float('inf')
        nearestNeighborClass: int = -1
        for j in range(n):
            if i == j: continue
            distance: float = euclideanDistance(data[i], data[j], featureIndices)
            if distance < nearestNeighborDistance:
                nearestNeighborDistance = distance
                nearestNeighborClass = classes[j]
        if nearestNeighborClass == classes[i]: correct += 1
    return correct / n

def forwardSelection(data: list[list[float]], classes: list[int], numFeatures: int) -> None:
    print("Hello World!")

def backwardsElimination(data: list[list[float]], classes: list[int], numFeatures: int) -> None:
    print("Hello World!")


def main():
    print("Welcome to Stanley's Search Algorithm!\n")
    fileName = input("Type in the name of the file to test: ").strip()
    print("Type in the number of the algorithm you want to run.\n\t1. Forward Selection\n\t2. Backward Elimination")
    algorithm = input().strip()

    data: list[list[float]]
    classes: list[int]
    data, classes = organizeData(fileName)

    numFeatures: int = len(data[0])
    numInstances: int = len(data)

    nearestNeighborAccuracy: float = nearestNeighbor(data, classes, set(range(numFeatures)))

    print(f"This dataset has {numFeatures} features (not including the class attribute), with {numInstances} instances.\n")
    print(f"Running nearest neighbor with all {numFeatures} features, using \"leave-one-out\" evaluation, I get an accuracy of {nearestNeighborAccuracy * 100:.2f}%")

    match algorithm:
        case "1": forwardSelection(data, classes, numFeatures)
        case "2": backwardsElimination(data, classes, numFeatures)
        case _: print("Invalid algorithm choice. Please choose either 1 or 2.")
    
if __name__ == "__main__":
    main()