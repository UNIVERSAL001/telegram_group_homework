from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """

    d={}
    for i in users_id:
        d[i]=0
    # print(d)
    for i in data["messages"]:
        if "actor_id" in i:
            d[i['actor_id']]+=1
        elif "from_id" in i:
            d[i['from_id']]+=1

    return d

data = read_data("data/result.json")

x = find_all_users_id(data)

y = find_user_message_count(data,x)
print(y)

