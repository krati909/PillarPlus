from django.db import connection
from django.shortcuts import render
import MySQLdb
# Create your views here.
import csv
def create(request):
    with open('testdata.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for column in csv_reader:
            field_name = column['field_name']
            type = column['type']
            options = column['options']
            mandatory =column['mandatory']
            #connecting to sql
            cursor = connection.cursor()
            query = "insert into testdata (field_name,type,options,mandatory) values (%s,%s,%s,%s)"
            value = (field_name,type,options,mandatory)
            cursor.execute(query, value)
        query3 ="select * from testdata"
        cursor.execute(query3)
        row = cursor.fetchone()
        return {'field_name': row[0], "type": row[1], "option": row[2], 'mandatory': row[3]}