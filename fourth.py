import sqlite3


from flask import Flask, render_template


db = sqlite3.connect('Muhib.db')

cr = db.cursor()


cr.execute('select * from user_skills')

save = cr.fetchall()


skills = Flask(__name__)



@skills.route("/")
def now():
    return render_template("mypage.html", pagetitle="Muhib", self_css= 'my.css')
@skills.route('/about')
def now2():
    return render_template('about.html', pagetitle= 'About Muhib', self_css= 'about.css')

@skills.route('/skills')
def now3():
    return render_template('skills.html', 
                           pagetitle= 'Family skills', 
                           self_css= 'skills.css',
                           head= 'Family Skills', 
                           des= 'You can see here our skills',
                           data= save)


if __name__ == "__main__":
    skills.run(debug=True, port=9000)

db.close()