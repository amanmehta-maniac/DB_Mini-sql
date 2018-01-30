import sys
import csv
class Table():
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.data = []

    def update_data(self, new_data):
        self.data = new_data

    def readData(self):
        data_file = self.name + ".csv"

        with open(data_file, "rb") as fl:
            tbl = csv.reader(fl)
            for rows in tbl:
                row = []
                for column in rows:
                    row.append(column)
                self.data.append(row)

class Database():
    def __init__(self, name, file_name):
        self.file_name = file_name
        self.name = name
        self.tables = {}
        self.metadata = {}

    def readMetaData(self):
        with open(self.file_name,"rb") as mtd:
            read_table_name = False
            try:
                for line in mtd:
                    line = line.strip()
                    if line == "<begin_table>":
                        read_table_name = True
                        continue
                    if read_table_name == True:
                        table_name = line
                        self.metadata[table_name] = []
                        read_table_name = False
                        continue
                    if not line == "<end_table>":
                        self.metadata[table_name].append(line)
                	# print "aww", self.metadata[table_name]
                for key in self.metadata:
                    self.metadata[key] = filter(None, self.metadata[key])
            except:
                print "Error while reading Metadata File"
            else:
                pass

    def populateDB(self):
        for tbl in self.metadata:
            objTable = Table(tbl, self.metadata[tbl])
            objTable.readData()
            self.tables[tbl] = objTable
            objTable = None
