import pyodbc


class AccessDatabase:
    def __init__(self, shp):
        self.shp_number = shp
        self.po_number = 'empty'
        self.company = 'empty'

    def get_data(self):
        server_name = r'####'
        db_name = 'Customer'
        server = "Server=" + str(server_name)
        db = "Database=" + str(db_name)
        key = "Driver={SQL Server};"+server+";"+db+";"+"UID=####;PWD=####"

        cnxn = pyodbc.connect(key)
        cursor = cnxn.cursor()
        cursor.execute(r"SELECT SDHNUM_0,CUSORDREF_0 as PO,BPDNAM_0 from SDELIVERY where SDHNUM_0 = '{}'".format(self.shp_number))
        while 1:
            row = cursor.fetchone()
            if not row:
                break
            print("AccessDatabase: " + row.SDHNUM_0 + ", " + row.PO + ", " + row.BPDNAM_0)
            self.po_number = row.PO
            self.company = row.BPDNAM_0
        cnxn.close()
