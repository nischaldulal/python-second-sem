#element in set is immutable but set is mutable 
collection=set()
collection.add(1)
collection.add(2)
collection.add("hello")
print(collection)
collection.remove(2)
print(collection)
# collection.add([1,2,3,4,5])TypeError: unhashable type: 'list'
print(collection.pop())
