def lambda_handler(event, context):
    # This function simply takes the First and last name as input and returns Hello f_name l_name
    return f"Hello {event['1st_name']} {event['2nd_name']}"