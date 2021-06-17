import json

def db_write(query, table):
    try:
        with open('./data/'+table+'.json') as json_file:
            data = json.load(json_file)
        try:
            previous_user_data = data[query[0]]
            previous_user_data.append(query[1])
            print(previous_user_data)
            if table == "posts":
                new_user = {query[0]:previous_user_data}
            else:
                new_user = {query[0]:query[1:]}
        except:
            new_user = {query[0]:query[1:]}

        data.update(new_user)
        with open('./data/'+table+'.json', 'w') as f:
            json.dump(data, f)
        return True
    except:
        return False

def validate_user(email, password):
    with open('./data/'+ 'auth' +'.json') as json_file:
        data = json.load(json_file)
        try:
            saved_password = data[email][0]
            if password == saved_password:
                return email
        except:
            return False
