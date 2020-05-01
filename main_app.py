from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('main.html', title='Главная')


@app.route("/about")
def about():
    return render_template('about.html', title='О сайте')


@app.route("/types_of_expertises")
def about():
    return render_template('experts.html', title='Виды экспертиз')


@app.route("/types_of_expertises/identificial")
def about():
    return render_template('identif.html', title='Идентификационная экспертиза')


@app.route("/types_of_expertises/threat")
def about():
    return render_template('threat.html', title='Дела об угрозе')


@app.route("/types_of_expertises/protect_honor")
def about():
    return render_template('threat.html', title='Защита чести и достоинства')


@app.route("/types_of_expertises/author")
def about():
    return render_template('author.html', title='Автороведческая экспертиза')


@app.route("/news")
def about():
    return render_template('news.html', title='Новости')


@app.route("/types_of_expertises/abuse")
def about():
    return render_template('abuse.html', title='Оскробление')


@app.route("/library")
def about():
    return render_template('biblio.html', title='Библиотека')


@app.route("/contacts")
def about():
    return render_template('cont.html', title='Контакты')


@app.route("/types_of_expertises/corruption")
def about():
    return render_template('corrupt.html', title='Антикоррупционные дела')


@app.route("/types_of_expertises/dignostical")
def about():
    return render_template('.html', title='Жиагностическая экспертиза')


@app.route("/extremism")
def about():
    return render_template('extremism.html', title='Экстремизм')


if __name__ == '__main__':
    app.run(debug=True)