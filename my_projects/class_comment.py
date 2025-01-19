class Comment:
    total_comments = 0
    def __init__(self, text, initial_votes_qty=0):
        self.text = text
        self.votes_qty = initial_votes_qty
        Comment.total_comments += 1

    def upvote(self, qty):
        self.votes_qty += qty

    def reset_votes_qty(self):
        self.votes_qty = 0


first_comment = Comment("First comment")
print(first_comment.text)
print(first_comment.votes_qty)  # 0
print(first_comment.total_comments)  # 1
print(Comment.total_comments)
first_comment.upvote(10)
first_comment.upvote(20)

print(first_comment.votes_qty)  # 30

first_comment.reset_votes_qty()
print(first_comment.votes_qty)  # 0

first_comment.upvote(7)
print(first_comment.votes_qty)
first_comment.upvote_1 = 10
first_comment.upvote(3)
print(first_comment.votes_qty)
print(type(first_comment.upvote_1))

second_comment = Comment("Second comment")
second_comment.upvote(2)
print(second_comment.text)
print(first_comment.total_comments)  # 2
print(Comment.total_comments)  # 2


