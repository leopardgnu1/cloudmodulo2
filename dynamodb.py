import boto3
print ("SI")

#create funcion to create for list dynamo table 
def list_table():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)
     
     list_table()
