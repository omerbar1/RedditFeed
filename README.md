Shared steps fot both running the file locally and running the script:
1.1. Choose the folder you want to run the file locally from.
2. Clone the git rep (https://github.com/omerbar1/RedditFeed)
3. Open the terminal/cmd.
4. Navigate to the folder where all the files are at.
5. install the requirements file using this line: "python -m pip install -r requirements.txt
"

How to run the file locally:
1. write this line: "python main.py".
2. You should see this line: "* Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)", navigate to the adress.
3. Use the website according to the instructions. input a subreddit, and get the output back.

How to run the script manually:
1. Write this line: "python subreddit_finder.py".
2. You should get in return the correct values. If your input was wrong (no subreddit found, or no posts), you will get a matching message.

Notes:
1. if writing "python ....." doesn't work, you should try using "py ..." or "python3 ...", depends on your machine.
2. I decided to return the hottest 5 posts on the subreddit, not the top 5 because the top is date dependant, and the hot section is decided by reddit's algorithm.
3. I have decided to use Google Cloud as the server to host the website, the link is: https://redditfeed1.uc.r.appspot.com/
4. Overview of how the app works: the app takes the subreddit from the input, running some tests on the input to make sure its right, and if so creates the needed json file. From there, it creates the top 5 posts (looping the dictionary), and printing it nicely.
5. The top posts that you get back are all the posts **without** the pinned posts, as most of the time (if not always), they are only messages from moderators, and are not the top posts in the subreddit. 
6. I decided to integrate both approaches. While the UI isn't very appealing, both of them work together well in the website.
7. I wrote many tests to check the code, but removed them, so the code won't be so loaded.
8. I have written the whole script in Python.
9. My best friend during this project was the internet. I learnt a lot.