from sklearn import datasets

iris_dataset =  datasets.load_iris()

print(iris_dataset.data)

print(iris_dataset.target_names)

print(iris_dataset['target'])

print(iris_dataset['DESCR'])