from class_Forum import Forum
from class_User import User


forum = Forum()
bogdan: User = forum.register_user('bogdan123', 'b@gmail.com')
alice: User = forum.register_user('alice643', 'a@outlook.com')

# print(forum.users)

forum.create_post('My first post', 'Post content', bogdan)

# now you should NOT search for posts like that.
# Use find_posts_by_author!
# print(forum.posts)
# print(forum.posts[0].title)
# print(forum.posts[0].content)
# print(forum.posts[0].author.username)
# print(forum.posts[0].author.email)

print(forum.find_user_by_username('admin123'))  # None
# print(forum.find_user_by_username('bogdan123'))  # Return object
print(forum.find_user_by_username('bogdan123').email)  # b@gmail.com

forum.create_post('Second great post', 'Post content', bogdan)

# find posts of the user
found_posts = forum.find_post_by_author(bogdan)
print(found_posts[0].content)
found_posts_titles = [post.title for post in found_posts]
print(found_posts_titles)

# find user by email and find all posts by that user
user_email = 'b@gmail.com'
found_user = forum.find_user_by_email(user_email)
if found_user:
    print(forum.find_post_by_author(found_user))
else:
    print(f"User with email {user_email} doesn't exist!")

