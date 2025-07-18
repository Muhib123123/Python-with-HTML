import sqlite3


from flask import Flask, render_template


db = sqlite3.connect('Muhib.db')

cr = db.cursor()


cr.execute('select * from user_skills')

save = cr.fetchall()

save2=[[2646,	'Muhib',	'Python',	70],
[2367,	'Majd',	'C++'	,50],
[3326,	'Maram',	'JavaScript',	40],
[4546,	'Leena',	'Python',	80],
[4356,	'Muhammed',	'C#',	35],
[467,	'Najwa',	'Java',	20],
[346,	'Hussam',	'Python',	95],
[43546,	'Ayana',	'C++',	33],
[23626,	'Ayala',	'JavaScript',	77],
[4366,	'Tala',	'Python',	55],
[34375,	'Morga',	'C++',	26],
[5488,	'Ghaith',	'JavaScript',	99],
[54858,	'Anwar',	'Python',	35],
[54780,	'Ali',	'C++',	77],
[3445,	'Lana',	'C#',	59]]


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
                           data= save2)


if __name__ == "__main__":
    skills.run(debug=True, port=9000)

db.close()