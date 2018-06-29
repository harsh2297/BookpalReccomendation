import pickle
import numpy as np 

print "Loading prediction model, this may take a few minutes"

with open("predictionModel.pkl") as f:
	pairwiseSimilarity = pickle.load(f)

with open("reverseIndexMap.pkl") as f:
	reverseIndexMap = pickle.load(f)

with open("indexMap.pkl") as f:
	indexMap = pickle.load(f)

print "Loaded all files.."

print reverseIndexMap
print reverseIndexMap[3]

def getTopReccomendation(BookID):
	row = reverseIndexMap[BookID]
	similarBookIDs = [indexMap[i] for i in np.argsort(pairwiseSimilarity[row])[-7:-2][::-1]]
	return similarBookIDs


if __name__ == '__main__':
	getTopReccomendation(1245)
