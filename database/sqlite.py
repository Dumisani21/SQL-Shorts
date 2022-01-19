import sqlite3

class DATABASE:

	def __init__(self,db_name):

		self.db_name = db_name


	def sql_create_table(self,tb_name,tb_attributes: list):

		conn = sqlite3.connect(self.db_name)

		c = conn.cursor()

		c.execute(f"CREATE TABLE {tb_name} {tb_attributes}")

		conn.commit()
		conn.close()

		print("table created")


	def sql_insert_data(self,tb_name,insert_data):

		conn = sqlite3.connect(self.db_name)

		c = conn.cursor()

		placeholder = '?'
		placeholders = ''

		if len(insert_data) == 1:

			placeholders = '(?)'

		else:


			for index in range(len(insert_data)):

				if index == len(insert_data) -1:

					placeholders += placeholder + ""

				else:

					placeholders += placeholder + ","

		data = f'({placeholders})'

		c.execute(f"INSERT INTO {tb_name} VALUES {data}",insert_data)

		conn.commit()
		conn.close()

		print("data inserted")


	def sql_udate_data(self,tb_name,updated_data,index_of_row):

		conn = sqlite3.connect(self.db_name)

		c = conn.cursor()

		c.execute(f"UPDATE {tb_name} SET {updated_data} WHERE rowid = {index_of_row}")

		conn.commit()
		conn.close()

		print("Data updated")


	def sql_delete_data(self,tb_name,index_of_row):
		
		conn = sqlite3.connect(self.db_name)

		c = conn.cursor()

		c.execute(f"DELETE FROM {tb_name} WHERE rowid = {index_of_row}")

		conn.commit()
		conn.close()

		print("data deleted")


	def sql_drop_table(self,tb_name):

		conn = sqlite3.connect(self.db_name)

		c = conn.cursor()

		c.execute(f"DROP TABLE {tb_name}")

		conn.commit()
		conn.close()

		print("table deleted")


	def sql_view_all(self,tb_name):

		conn = sqlite3.connect(self.db_name)

		c = conn.cursor()

		c.execute(f"SELECT rowid, * FROM {tb_name}")

		read_data = c.fetchall()

		list_data = []

		for data in read_data:

			list_data.append(data)

		print("view data is returned")

		return list_data

	def sql_view_specific(self,tb_name,data_view):

		conn = sqlite3.connect(self.db_name)

		c = conn.cursor()

		c.execute(f"SELECT rowid, {data_view} FROM {tb_name}")

		read_data = c.fetchall()

		list_data = []

		for data in read_data:

			list_data.append(data)

		print("view data is returned")

		return list_data


	def sql_search_table(self,tb_name,search_query):

		conn = sqlite3.connect(self.db_name)

		c = conn.cursor()

		c.execute(f"SELECT rowid, * FROM {tb_name} WHERE {search_query}")

		read_data = c.fetchall()

		list_data = []

		for data in read_data:

			list_data.append(data)

		print("view data is returned")
			
		return list_data