# PillarPlus
I have Design an API that creates a form template in form directory. It takes dictionary which have all the data, obtained after either inserting the data, deleting the data or updating the data from sql.
Designed APIs to allow users to create, update, delete entries for an existing form template. 

create function, reads data from csv file, store it in database and returnes the data in form of dictionary, which is further used by form template.
update function, takes data as input from the user, update the data in databse and returned the data in form of dictionary,used further.
delete function. takes the data to be deleted, delete it from database and returnes dictionary to be used further in form template.
I have used models to create schemas, Sql query to insert, delete and update database and used serializers
