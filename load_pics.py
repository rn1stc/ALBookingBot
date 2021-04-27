from datetime import datetime
import instaloader

L = instaloader.Instaloader()

posts = instaloader.Hashtag.from_name(L.context, "urbanphotography").get_posts()

k = 0  # initiate k
#k_list = []  # uncomment this to tune k
count = 0
for post in posts:
    count += 1
    #L.download_post(post, "#urbanphotography")
    print(post.url)
    if count == 15:
        break


#     postdate = post.date
#
#     if postdate > UNTIL:
#         continue
#     elif postdate <= SINCE:
#         k += 1
#         if k == 10:
#             break
#         else:
#             continue
#     else:
#         L.download_post(post, "#urbanphotography")
#         # if you want to tune k, uncomment below to get your k max
#         #k_list.append(k)
#         k = 0  # set k to 0
#
# #max(k_list)