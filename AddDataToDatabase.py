import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://realtimefacerecog-d270c-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "312416":
        {
            "name": "Pedro Pascal",
            "major": "Film Studies",
            "starting_year": 2016,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-11 01:54:34",
        },
    "473869":
        {
            "name": "Ridwanur Rahman",
            "major": "Computer Science",
            "starting_year": 2019,
            "total_attendance": 8,
            "standing": "G",
            "year": 5,
            "last_attendance_time": "2024-08-19 02:47:10",
        },
    "321654":
        {
            "name": "Giancarlo Esposito",
            "major": "Chemistry",
            "starting_year": 2020,
            "total_attendance": 4,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2024-09-18 08:34:32",
        },
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34",
        },
    "852741":
        {
            "name": "Emily Blunt",
            "major": "Economics",
            "starting_year": 2023,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34",
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34",
        }
}

for key, value in data.items():
    ref.child(key).set(value)