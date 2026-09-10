import mysql.connector
class mysll():
    def news(self):
      try:
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sinan@2004",
            database="company_db"
        )
        return self.connection
      except Exception as e:
          return None
employees_instance=mysll()
employees_instance.news()

