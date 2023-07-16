with open(r"D:\New folder\files\New folder\Python\Day 13\iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()
    print(iris_data)

irises = []

for row in iris_data[1:]:
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")

    irises.append({
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    })


#alternative way
with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

headers = iris_data[0].strip().split(",")
irises = []

for row in iris_data[1:]:
    iris = row.strip().split(",")
    iris_dict = dict(zip(headers, iris))

    irises.append(iris_dict)





