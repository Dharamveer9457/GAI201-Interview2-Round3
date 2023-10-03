from flask import flask, request, jsonify

app = flask(__name__)

posts = []

class Post:
    def __init__(self, username, caption):
        self.id = len(posts)+1
        self.username = username
        self.caption = caption

@app.route("/createpost", methods = ['POST'])
def createPost():
    data = request.get_json()
    if 'username' in data and 'caption' in data:
        username = data['username']
        caption = data['caption']
        new_post = Post(username,caption)

        posts.append(new_post)
        return jsonify({'msg':"New Post created"}), 200
    else:
        return jsonify({'msg':"Invalid Data"}), 400

@app.route("/viewposts", methods = ["GET"])
def get_post():
    posts_list = [{'id':post.id, 'username':post.username, 'caption':post.caption}]
    return jsonify(posts_list), 200

@app.route("/deletepost/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    for post in posts:
        if post.id == post_id:
            posts.remove(post)
            return jsonify({'msg':'Post deleted successfully'}), 200
        else:
            return jsonify({'msg':'Post not found'}), 404
        

if __name__ == '__main__':
    app.run(debug=True)