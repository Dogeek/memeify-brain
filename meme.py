import praw
from PIL import Image, ImageFont, ImageDraw
import textwrap

reddit = praw.Reddit(client_id="9y8m9AYCA3LM6g",
                     client_secret="ZGLTYphrcn4vrv6go8zCAd0ILoA",
                     user_agent='testscript by /u/dogeek')
subreddit = reddit.subreddit('showerthoughts')

font = ImageFont.truetype("arial.ttf", 15)
wrap_at = 55

for i, submission in enumerate(subreddit.top(limit=100)):
    coordsx, coordsy = (18, 377)
    template = Image.open("template.jpg")
    draw = ImageDraw.Draw(template)
    wrapped = textwrap.wrap(submission.title, width=wrap_at)
    for i, wrap in enumerate(wrapped):
        coords = (coordsx, coordsy + i * 18)
        draw.text(coords, wrap, font=font, fill="#000000")
    template.save(f"result-{i}.jpg", "JPEG")
