import boto3
ddb = boto3.client("dynamodb")

def handler(event, context):
    try:
        data = ddb.put_item(
            TableName="Users",
            Item={
                'email': {
                    'S': event.email
                },
                'device': {
                    'S': event.device
                }
            }
        )
        print(data)
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully Added"}
