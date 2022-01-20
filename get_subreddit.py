import json
import requests

baseurl = 'https://www.reddit.com'
suffix = '/.json'


def get_top5(children_lst, length, index):
    child_to_post = []
    for i in range(index, length):
        if children_lst[index]['data']['stickied'] == 'true':
            index += 1
            continue
        child_dict = {'Author': children_lst[index]['data']['author'],
                      'Title': children_lst[index]['data']['title'],
                      'Upvotes': children_lst[index]['data']['score'],
                      'Number of comments': children_lst[index]['data']['num_comments'],
                      'Link': f"{baseurl}{children_lst[index]['data']['permalink']}", }
        child_to_post.append(child_dict)
        index += 1
        if len(child_to_post) == 5:
            break
    if index == length - 1:
        index = -1
    return child_to_post, index


def print_children(top5child):
    for child in top5child:
        for key, value in child.items():
            print(f'{key}: {value}')
        print('-----------------------------------')


def get_subreddit():
    print("Enter subreddit name:")
    subredditName = input()
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_7 rv:5.0; en-US) AppleWebKit/533.31.5 (KHTML, '
                      'like Gecko) Version/4.0 Safari/533.31.5',
    }
    url = f"{baseurl}/r/{subredditName}{suffix}"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 404 or (resp.status_code == 200 and len(resp.json()['data']['children']) == 0):
        print(f"There is no subreddit named {subredditName}")
    elif resp.status_code != 200:
        print(f"Error: {json.loads(resp.text)['message']}")
    else:
        children_lst = resp.json()['data']['children']
        length = len(children_lst)
        index = 0
        top5child, index = get_top5(children_lst, length, index)
        print("Here are the top 5 posts in the subreddit you chose:\n")
        print_children(top5child)
        print("Do you wanna see more? (yes/no)")
        answer = input().lower()
        while answer != "no":
            if answer == "yes":
                if index == -1:
                    print("No more posts available for this subreddit\n")
                    break
                top5child, index = get_top5(children_lst, length, index)
                print_children(top5child)
                print("Do you wanna see more? (yes/no)\n")
                answer = input().lower()
            else:
                print("Please reply with yes or no\n")
                answer = input().lower()


get_subreddit()
