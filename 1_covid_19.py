import numpy as np

sum_patient = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

def get_minimum(data):
   return np.min(data) 

def get_maximum(data):
   return np.max(data)
   
def get_range(data):
   return np.ptp(data)

def get_mean(data):
   return np.mean(data)

def get_median(data):
   return np.median(data)

def get_variance(data):
   return np.var(data, ddof=1)

def get_standard_deviation(data):
   return np.std(data, ddof=1)

print('Patient Covid-19: ', sum_patient)
print("Minimum:", get_minimum(sum_patient))
print("Maximum:", get_maximum(sum_patient))
print("Range:", get_range(sum_patient))
print("Mean:", get_mean(sum_patient))
print("Median:", get_median(sum_patient))
print("Variance:", get_variance(sum_patient))
print("Standard Deviation:", get_standard_deviation(sum_patient))
