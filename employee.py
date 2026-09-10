import mysql.connector
class employeemanager():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sinan@2004",
                database="company_db"
            )
        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = "insert into employee(name,place,mobile,email,department,salary,joined_date) values(%s,%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("employee added successfully")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from employee"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            print("___employee details___")
            for i in record:
                print(i)
        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            record = self.get_object(id=id)
            if record == None:
                print("employee is not found")
            else:
                print(record)
        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.cursor = self.connection.cursor()
                query = "delete from employee where id=%s"
                values = (id,)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("employee deleted successfully")
        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                placeholder = ""
                for i in kwargs.keys():
                    placeholder += i + "=%s,"
                placeholder = placeholder.rstrip(", ")
                query = f"update  employee set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("employee updated successfully")
        except Exception as e:
            print(e)

    def get_object(self, id=None):
        self.cursor = self.connection.cursor()
        query = "select * from employee where id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        record = self.cursor.fetchone()
        return record


employee_instance = employeemanager()
#
# employee_instance.post(name="amala",place="kollam",mobile="9876744677",email="amal@gmail.com",department="HR",salary=245555,joined_date=datetime.today())
# employee_instance.get()

# employee_instance.put(id=3,name="amalu",place="kollam")
# employee_instance.get()

# employee_instance.delete(id=1)
# employee_instance.get()
#
# employee_instance.retrieve(id=1)


