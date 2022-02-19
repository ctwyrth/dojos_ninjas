from dojo_ninjas_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in dojos_from_db:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location) VALUES (%(name)s, %(location)s);"
        print(query)
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def show(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        dojo = cls(results[0])
        return dojo

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s, location=%(location)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)
    
    @classmethod
    def get_students(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)