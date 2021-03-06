# Program description
# Return in json unique groups' set among all friends in vk

#Import libs, define constants, variables
import requests
import json
import time
from pprint import pprint

TOKEN = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'
EVG_ID = 171691064

#Create User-class
class User:
      def __init__(self, token, id_):
            self.token = token
            self.id_ = id_
            self.friends_list = list()
            self.groups_set = set()

      def get_friends(self):
            """get list of friends"""
            params = {
                  'access_token': self.token,
                  'user_id' : self.id_,
                  'v': '5.92'
                  }

            response = requests.get('https://api.vk.com/method/friends.get', params).json()
            self.friends_list = response['response']['items']

            return self.friends_list

      def get_groups(self):
            """get set of groups"""
            params = {
                  'access_token': self.token,
                  'user_id' : self.id_,
                  'v': '5.92'
                  }

            response = requests.get('https://api.vk.com/method/groups.get', params).json()
            self.groups_set = set(response['response']['items'])

            return self.groups_set


def get_unique_groups(evgen_friends_list, evgen_groups_set, TOKEN):
      """Get unique groups IDs"""
      for evgen_friend in evgen_friends_list:
            while True:
                  print('...')
                  friend = User(TOKEN, evgen_friend)
                  try:
                        friends_set = friend.get_groups()
                        evgen_groups_set -= friends_set
                        time.sleep(1)
                  except KeyError:
                        pass
                  else:
                        break
            
      return list(evgen_groups_set)


def get_group_description(groups_description, TOKEN, group_id):
      """Get group description by ID"""
      group_dict = dict()
      params = {
                  'access_token': TOKEN,
                  'group_id' : group_id,
                  'v': '5.92'
                  }
      print('...')
      get_by_id = requests.get('https://api.vk.com/method/groups.getById', params).json()
      
      for group in get_by_id['response']: # to operate with list
            print('...')
            get_members = requests.get('https://api.vk.com/method/groups.getMembers', params).json()
            count_members = get_members['response']['count']
            group_dict['name'] = group['name']
            group_dict['gid'] = group['id']
            group_dict['members_count'] = count_members
            groups_description.append(group_dict)

      return groups_description


def create_json(groups_description):
      """Create json file"""
      data_to_write = json.dumps(groups_description)
      with open('groups.json', 'w') as f:
            f.write(data_to_write)
      

def main(TOKEN = TOKEN, EVG_ID = EVG_ID):
      """Key loop"""
      evgen = User(TOKEN, EVG_ID)
      evgen_friends_list = evgen.get_friends()
      evgen_groups_set = evgen.get_groups()
      unique_groups_list = get_unique_groups(evgen_friends_list, evgen_groups_set, TOKEN)

      groups_description = []
      for group_id in unique_groups_list:
            get_group_description(groups_description, TOKEN, group_id)
      create_json(groups_description)

      # testing
      with open('groups.json', 'r', encoding = 'UTF8') as f:
            data = json.load(f)
            print(data)
            
if __name__ == '__main__':
      main()
      











      
