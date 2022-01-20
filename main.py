from flask import Flask
from flask import request

from RedditFeed.get_subreddit import get_subreddit

app = Flask(__name__)


@app.route("/")
def index():
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

if __name__ == "__main__":
    app.run()
