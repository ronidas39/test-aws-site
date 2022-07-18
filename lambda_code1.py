import json
import boto3
client=boto3.resource("dynamodb")
table=client.Table("july15-api-test")

def create(event):
    response = table.put_item(
      Item={"id":event["id"],"Name":event["name"],"Country":event["country"],"Company":event["company"]}
    )
    return response
    
def read(event):
    response = table.get_item(
      Key={"id":event["id"]})
    return response["Item"]
    
def delete(event):
    response=table.delete_item(Key={"id":event["id"]})
    return response


def lambda_handler(event, context):
    # TODO implement
    key=event["type"]
    if key=="create":
        response=create(event)
        return response
    elif key=="read":
        print("here")
        response=read(event)
        print(response)
        return response
    else:
        response=delete(event)
        return response
    
  