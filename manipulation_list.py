# Operation list

# data starting from index 0
data = [1, 2, 3, 4, 5]
print(f"data [0] : {data[0]}")

# what if we print data[-1]
print(f"data [-1] : {data[-1]}")

# if we want know length of list
print(f"Panjang data list : {len(data)}")

# add new data in list at the end
data.append(6)
print(f"data : {data}")

# list + list
new_data = [7, 8, 9, 10]
data.extend(new_data)
print(data)

# change
data[0] = 2
print(data)
data[0] = 1
print(data)

# remove
data.remove(data[0])
data.remove(3)
print(data)
# remove list from behind
data.pop()
print(data)
