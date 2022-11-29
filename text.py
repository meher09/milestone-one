tasks = [
    {"name": 'mily', "id": 100,
     "title": "Contrary to popular belief",   "gender": 'female'
     },
    {
        "name": 'sourob',  "id": 200, "title": "comes from sections 1.10.32 and 1.10.33 ",
        "gender": 'male'
    },
    {
        "name": 'tasnuba',        "id": 250,
        "title": "Contrary to popular belief",        "gender": '3rd'
    },
    {
        "name": 'duna',        "id": 100,
        "title": "Nullam non magna at augue mattis tincidunt.",        "gender": 'female'
    },
    {
        "name": 'sisir',        "id": 250,
        "title": "Contrary to popular belief",        "gender": '3rd'
    },
    {
        "name": 'Jhon', "id": 200,
        "title": "Aliquam accumsan lectus ac sapien luctus auctor",  "gender": 'male'
    }
]


for task in tasks:
    if task.get('gender') == 'male' and 'id' == 100:
        print(task.get('title'))
    elif task.get('gender') == 'female' and id == 200:
        print(task.get('title'))
    else:
        print(task.get('title'))


