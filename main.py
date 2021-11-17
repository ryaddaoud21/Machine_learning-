from math import sqrt



# calculer la distance euclidienne entre deux vecteurs
def euclidean_distance(x, y):
	distance = 0.0
	for i in range(len(x)-1):
		distance += (x[i] - y[i])**2
	return sqrt(distance)

def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors



def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction


Dataset = list()
i = 0
import random
# Test
R = 20
R1 = 40
while True :
	X = random.randint(1,200)
	Y = random.randint(1,200)
	if (euclidean_distance([X,Y],[0,0]) >R):
		Dataset.append([X,Y,0])
		i += 1

	if (euclidean_distance([X, Y], [0, 0]) <R1):
		Dataset.append([X, Y, 1])
		i += 1

	if (i==200):
		break

X=[25,15]
print(Dataset)
print(predict_classification(Dataset,X,5))