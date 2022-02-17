# Basic ORM using Python and SQLite3

```python
DATA_TYPES_MAPPER = {
    int: "INTEGER",
    float: 'REAL',
    str: "TEXT",
    bytes: "BLOB",
    bool: "INTEGER" # 1 for True and 0 for False
}
```

# Testing the ORM

- Unit tests are included in test.py
- To run the test execute the command below

```
    python3 test.py
```

# How to use the ORM

```python
import myorm
import models

#Create data base
users = myorm.create_db('users')

class User(myorm.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    isAdmin = models.BooleanField(default=False)

#Creating table using
User.create_table('users')

user = User(username='mjthecoder', email='mjthecoder@gmail.com', password='HAwK;2$]BH,ZTJx', isAdmin=True)
user.save()

# Finding user
del user

user = User.filter(email="mjthecoder@gmail.com")
print(user[0]) # { username: 'mjthecoder', email: 'mjthecoder@gmail.com', password: 'HAwK;2$]BH,ZTJx', isAdmin: 1}
```
