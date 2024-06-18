from flask import render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from web_app import app

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
        if 11 <= number % 100 <= 14:  # год-года-лет  
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
            image_path = os.path.join('uploads', filename).replace("\\", "/") # относительный путь для отображения, замена обратного слэша
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

