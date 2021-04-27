from datetime import datetime
import instaloader

L = instaloader.Instaloader()

posts = instaloader.Hashtag.from_name(L.context, "urbanphotography").get_posts()

k = 0  # initiate k

count = 0
for post in posts:
    count += 1
    #L.download_post(post, "#urbanphotography")
    print(post.url)
    if count == 15:
        break

