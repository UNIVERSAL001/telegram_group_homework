from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    ls = []
    for i in data["messages"]:
        
        if "actor_id" in i and i["actor_id"] not in ls:
            ls.append(i['actor_id'])
        elif "from_id" in i and i["from_id"] not in ls:
            ls.append(i['from_id'])

    return ls

# data = read_data("data/result.json")

# x = find_all_users_id(data)
# print(x)