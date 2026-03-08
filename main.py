def organizeData(fileName: str) -> tuple[list[list[float]], list[int]]:
    data: list[list[float]] = []
    labels: list[int] = []
    with open(fileName, "r") as f:
        for line in f:
            values: list[str] = line.split()
            if not values: continue
            labels.append(int(float(values[0])))
            data.append([float(x) for x in values[1:]])
    return data, labels


def main():
    print("Welcome to Stanley's Search Algorithm!\n")
    fileName = input("Type in the name of the file to test: ").strip()
    print("Type in the number of the algorithm you want to run.\n\t1. Forward Selection\n\t2. Backward Elimination")
    algorithm = input().strip()

    data: list[list[float]]
    labels: list[int]
    data, labels = organizeData(fileName)

    numFeatures: int = len(data[0])
    numInstances: int = len(data)

    print(f"This dataset has {numFeatures} features (not including the class attribute), with {numInstances} instances.\n")
    print(f"Running nearest neighbor with all {numFeatures} features, using \"leave-one-out\" evaluation, I get an accuracy of ")


if __name__ == "__main__":
    main()