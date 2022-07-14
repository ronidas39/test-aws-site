
#dynamo db bulk upload

import boto3
import io
client=boto3.resource("dynamodb")
table=client.Table("emp")


with io.open("emp.csv","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
lines=data.split("\n")[1:]


for line in lines:
    name=line.split(",")[0]
    ph_no=line.split(",")[1]
    email=line.split(",")[2]
    country=line.split(",")[3]
    
    table.put_item(
      Item={"email":email,"Name":name,"Country":country,"Ph":ph_no}
)