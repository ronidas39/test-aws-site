import json
import boto3
client=boto3.resource("dynamodb")
table=client.Table("api-gateway")


def create():
    response=table.put_item(
      Item={"id":3,"Name":"John","Country":"USA","Company":"Netflix"}
      
)   
    return response
    
def read():
    response = table.get_item(
      Key={"id":3}
  )
    return response["Item"]

def update():
    response = table.update_item(
      Key={"id":3},
      ReturnValues='UPDATED_NEW',
      UpdateExpression="SET Department = :dep",
      ExpressionAttributeValues={
          ":dep":"IT-DEPARTMENT"
          }
  )
  
def delete():
    response = table.delete_item(
      Key={"id":3}
  )

    

def lambda_handler(event, context):
    # TODO implement
    #
    #update()
    #delete()
    if event["type"]=="create":
      response=create()
      return response
    elif event["type"]=="read":
      response=read()
      return response
    elif event["type"]=="update":
       response=update()
       return response
    else:
        response=delete()
        return response
      
      

    return {
        'statusCode': 200,
        'body': event,
        'test':'successfull'
    }
