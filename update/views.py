from django.db import connection
from django.shortcuts import render
import pandas as pd
import MySQLdb
# Create your views here.
import csv
def update(request):
    with open('testdata.csv', 'w') as csv_file:
        old_data= request.GET.get("old_data")
        data= request.GET.get("data")
        column=request.GET.get("column")
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for col in csv_reader:
            field_name = column['field_name']
            type = column['type']
            option = column['options']
            mandatory =column['mandatory']
            cursor = connection.cursor()
            if data in field_name or type or option or mandatory:
                query2 = "update testdata set " + column + "=" + data + " where " + column + " = '" + old_data + "'"
                cursor.execute(query2)
        query3 ="select * from testdata"
        cursor.execute(query3)
        row = cursor.fetchall()

        return {'field_name': row[0], "type": row[1], "option": row[2], 'mandatory': row[3]}