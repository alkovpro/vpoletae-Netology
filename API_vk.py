import requests

# Creating class 'user'
class User:
    def __init__(self, token):
        self.id_ = token

    def show_friends(self, id_):
        params = {
        'access_token': self.token,
        'user_id' = id_
        'v': '5.92'}

        friends_set = set()
        response = requests.get('https://api.vk.com/method/friends.get', params).json()
        for friend in response['response']['items']:
            friends_set.add(friend['id'])

        return friends_set
                                                
# Creating objects
def create_users():
      users_list = []
      token = input('Please enter token: ')
      count = input('Please enter number of objects: ')
      assert count.isdigit() == True, print('Please enter a number!')
      
      for number in range(int(count)):
            user = User(token)
            users_list.append(user)
            
      return users_list

# Check intersection
def get_id():
    id_ = ''
    while not id_.isdigit() == True:
        id_ = input("Please enter user's ID: ")
        
    return int(id_)

def check_intersection(users_list):
    id_ = get_id()
    intersected_set = users_list[0].show_friends(id_)
    
    for user in user_list:
        id_ = get_id()
        friends_set = user.show_friends(id_)
        intersected_set = intersected_set & friends_set
        
    return intersected_set    

# Printing results
def print_results(intersected_set):
    intersected_list = list(intersected_set)
    if len(intersected_list) == 0:
        print('There are no same friends found')
    else:
        for id_ in intersected_list:
            print('https://vk.com/id'.format(id_))

# Main function
def main():
      users_list = create_users()
      intersected_set = check_intersection(users_list)
      print_results(intersected_set)
                      
if __name__ == '__main__':
    main()
