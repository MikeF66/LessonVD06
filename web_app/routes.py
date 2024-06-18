from flask import render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from web_app import app

# posts = []
# @web_app.route("/blog/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         title = request.form.get('title')
#         image = request.files.get('image')
#         content = request.form.get('content')
#         if image:
#             filename = secure_filename(image.filename)
#             image_path = os.path.join(web_app.config['UPLOAD_FOLDER'], filename)
#             image.save(image_path)
#             image_path = os.path.join('uploads', filename).replace("\\", "/") # относительный путь для отображения
#             print(image_path)
#         else:
#             image_path = None
#         post = {
#             'title': title,
#             'image_path': image_path,
#             'content': content
#         }
#         posts.append(post)
#         return redirect(url_for('index'))
#     return render_template('blog.html', posts=posts)

cards = []
@app.route("/", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        name = request.form.get('name')
        image = request.files.get('image')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        number = int(age)
        if 11 <= number % 100 <= 14:
            suffix = "лет"
        elif number % 10 == 1:
            suffix = "год"
        elif 2 <= number % 10 <= 4:
            suffix = "года"
        else:
            suffix = "лет"
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
            image_path = os.path.join('uploads', filename).replace("\\", "/") # относительный путь для отображения
        else:
            image_path = None
        card = {
            'name': name,
            'image_path': image_path,
            'city': city,
            'hobby': hobby,
            'age': age,
            'suffix': suffix
        }
        cards.append(card)
        return redirect(url_for('profile'))
    return render_template('profile.html', cards=cards)






# @web_app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#         return redirect(request.url)
#     if file:
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(web_app.config['UPLOAD_FOLDER'], filename))
#         # Здесь вы можете добавить пост в базу данных, включая путь к файлу
#         return redirect(url_for('index'))

