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
    currentFeatures: set[int] = set()
    bestFeatures: set[int] = set()
    bestAccuracy: float = 0.0

    print("Beginning search.")

    for _ in range(numFeatures):
        currentBestAccuracy: float = 0.0
        currentBestFeature: int = -1
        for feature in range(numFeatures):
            if feature in currentFeatures: continue # skip the features we already have
            mergedset = currentFeatures.union({feature}) # create a new set of features by adding the current feature with our current set
            accuracy: float = nearestNeighbor(data, classes, mergedset) # find the accuracy with the new set of features
            feature_str: str = "{" + ",".join(str(x + 1) for x in sorted(mergedset)) + "}"
            print(f"Using feature(s) {feature_str} accuracy is {accuracy * 100:.2f}%")
            if accuracy > currentBestAccuracy: # if the accuracy is better than what we have so far update our current best accuracy and feature for the current level
                currentBestAccuracy = accuracy
                currentBestFeature = feature
        currentFeatures.add(currentBestFeature) # add the best feature for this level to our current set of features
        level_text: str = "{" + ",".join(str(x + 1) for x in sorted(currentFeatures)) + "}"
        print(f"Feature set {level_text} was best, with an accuracy of {currentBestAccuracy * 100:.2f}%\n")
        if currentBestAccuracy > bestAccuracy:
            bestAccuracy = currentBestAccuracy
            bestFeatures = set(currentFeatures)
    print(f"Finished search!! The best feature subset is {bestFeatures}, which has an accuracy of {bestAccuracy * 100:.2f}%")

def backwardsElimination(data: list[list[float]], classes: list[int], numFeatures: int) -> None:
    currentFeatures: set[int] = set(range(numFeatures))
    bestFeatures: set[int] = set(currentFeatures)
    bestAccuracy: float = nearestNeighbor(data, classes, currentFeatures)
    print("Beginning search.")
    for _ in range(numFeatures - 1):
        currentBestAccuracy: float = 0.0
        featureToRemove: int = -1
        for feature in currentFeatures:
            mergedset = currentFeatures.difference({feature}) # create a new set of features by removing the current feature from our current set
            accuracy: float = nearestNeighbor(data, classes, mergedset) # find the accuracy with the new set of features
            feature_str: str = "{" + ",".join(str(x + 1) for x in sorted(mergedset)) + "}"
            print(f"Using feature(s) {feature_str} accuracy is {accuracy * 100:.2f}%")
            if accuracy > currentBestAccuracy: # if the accuracy is better than what we have so far update our current best accuracy and feature to remove for the current level
                currentBestAccuracy = accuracy
                featureToRemove = feature
        currentFeatures.remove(featureToRemove) # remove the feature for this level from our current set of features
        level_text: str = "{" + ",".join(str(x + 1) for x in sorted(currentFeatures)) + "}"
        print(f"Feature set {level_text} was best, with an accuracy of {currentBestAccuracy * 100:.2f}%\n")
        if currentBestAccuracy > bestAccuracy:
            bestAccuracy = currentBestAccuracy
            bestFeatures = set(currentFeatures)
    bestText: str = "{" + ",".join(str(x + 1) for x in sorted(bestFeatures)) + "}"
    print(f"Finished search!! The best feature subset is {bestText}, which has an accuracy of {bestAccuracy * 100:.2f}%")

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
        case _: print("Invalid algorithm choice. Goodbye!")
    
if __name__ == "__main__":
    main()