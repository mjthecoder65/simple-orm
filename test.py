import unittest 
import myorm
import models

class TestingMappingClasses(unittest.TestCase):
    def test_charfield_type(self):
        name = models.CharField(max_length=20)
        self.assertEqual(name.type, 'TEXT')
    def test_integerfield_type(self):
        age = models.IntegerField()
        self.assertEqual(age.type, 'INTEGER')
    def test_floatfield_type(self):
        temperature = models.FloatField()
        self.assertEqual(temperature.type, 'REAL')
    def test_booleanfield_type(self):
        is_authorized = models.BooleanField()
        self.assertEqual(is_authorized.type, 'INTEGER')

class TestingDataBase(unittest.TestCase):
    def test_create_database(self):
        mydb = myorm.create_db('mydb')
        self.assertEqual(mydb, 'mydb')

class TestingORM(unittest.TestCase):
    class Author(myorm.Model):
        name = models.CharField(max_length=20)
        email = models.CharField(max_length=20)
    def test_create_table(self):
        result = self.Author.create_table('mydb')
        self.assertEqual(result, True)
    def test_save(self):
        author = self.Author(name="Michael", email="michael@gmail.com")
        result = author.save()
        self.assertEqual(result, True)
        author = self.Author(name="Jerry", email="jerrylst@gmail.com")
        result = author.save()
        self.assertEqual(result, True)
    def test_filter(self):
        authors = self.Author.filter(email='michael@gmail.com')
        self.assertEqual(isinstance(authors, list), True)
        print(authors)
        if len(authors) > 0:
            self.assertEqual(authors[0]['name'], 'Michael')
            print(authors)

if __name__ == '__main__':
    unittest.main()