from flask import Flask
from flask import request
import requests
import json

app = Flask(__name__)


@app.route("/")
def run_app():
    subreddit = request.args.get("subreddit", "")
    if subreddit:
        ret_val = get_subreddit(subreddit)
    else:
        ret_val = ""
    return (
            """<body style="font-family:verdana;">
            <form action="" method="get">
                Enter subreddit name: <input type="text" name="subreddit">
                <input type="submit" value="Submit">
            </form>"""
            + str(ret_val)
            + "</body>"
    )


baseurl = 'https://www.reddit.com'
suffix = '/.json'


def top5_to_string(top5child):
    str_to_return = '<h3 style="font-family:verdana;"> Here are the top 5 posts in this subreddit: </h3>'
    for child in top5child:
        for key, value in child.items():
            if key == 'Link':
                str_to_return += f'{key}: <a href={value}>Click here</a><br>'
            else:
                str_to_return += f'{key}: {value}<br>'
        str_to_return += '-----------------------------------<br>'
    return str_to_return


def get_top5(children_lst, length, index):
    child_to_post = []
    for i in range(index, length):
        if children_lst[index]['data']['stickied']:
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


def get_subreddit(subreddit_name):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_7 rv:5.0; en-US) AppleWebKit/533.31.5 (KHTML, '
                      'like Gecko) Version/4.0 Safari/533.31.5',
    }
    url = f"{baseurl}/r/{subreddit_name}{suffix}"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 404 or (resp.status_code == 200 and len(resp.json()['data']['children']) == 0):
        return f"There is no subreddit named {subreddit_name}"
    if resp.status_code == 403:
        return f"{subreddit_name} is a private subreddit"
    elif resp.status_code != 200:
        return f"Error: {json.loads(resp.text)['message']}"
    else:
        children_lst = resp.json()['data']['children']
        length = len(children_lst)
        index = 0
        top5child, index = get_top5(children_lst, length, index)
        return top5_to_string(top5child)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
