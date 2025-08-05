student = {'id1': {"name": "Hanniel", 'age': 20, 'grade': 'A'},
           'id2': {'name': "John", 'age': 22, 'grade': 'B'},
           'id3': {'name': 'Alice', 'age': 21, 'grade': 'A'}}
result = {}
for i, j in student.items():
    if j not in result.values():
        result[i] = j
print(result)