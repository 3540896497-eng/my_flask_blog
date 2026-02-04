from flask import Flask, render_template, abort

app = Flask(__name__)

# 模拟文章数据
POSTS = [
    {"id": 1, "category": "novel", "title": "我的第一部小说", "content": "这是小说内容..."},
    {"id": 2, "category": "tech", "title": "Flask 入门指南", "content": "Python 开发非常有趣..."},
    {"id": 3, "category": "daily", "title": "今天的心情", "content": "今天天气不错..."},
    {"id": 4, "category": "finance", "title": "投资心得", "content": "保持理性，长期主义..."},
]

# 模块配置
MODULES = {
    "novel": "小说写作",
    "tech": "技术分享",
    "daily": "个人日常",
    "finance": "金融投资"
}

@app.route('/')
def index():
    # 落地页：头像 + 欢迎语
    return render_template('index.html')

@app.route('/main')
def main():
    # 第二个页面：模块展示
    return render_template('main.html', modules=MODULES)

@app.route('/category/<cat_id>')
def category(cat_id):
    # 分类文章列表页
    if cat_id not in MODULES:
        abort(404)
    cat_posts = [p for p in POSTS if p['category'] == cat_id]
    return render_template('category.html', cat_name=MODULES[cat_id], posts=cat_posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    # 文章内容页
    post = next((p for p in POSTS if p['id'] == post_id), None)
    if not post:
        abort(404)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)