from flask import render_template, redirect
from forms import RegisterForm
from os import path
from ext import app, db
from forms import SportForm
from model import Sport
from flask import redirect, url_for

profiles = []


# sports = [
#     {"id": 1, "name": "Basketball", "img": "Basketball.jpg", "description": "Basketball is a team sport in which two teams of five players each, opposing one another on a rectangular court, compete with the primary objective of shooting a basketball through a hoop at each end of the court.", "des_long": "Basketball is a team sport in which two teams of five players each (excluding substitutes), opposing one another on a rectangular court, compete with the primary objective of shooting a basketball through a hoop (a basket mounted to a backboard) at each end of the court. Teams alternate between offense, when they attempt to score, and defense, when they try to prevent the opposing side from scoring. A field goal is worth two points, unless made from behind the three-point line, when it is worth three. After a foul, timed play stops and the fouled team either takes one to three free throws worth one point each, or restarts play with an inbound pass. The team with the most points at the end of the game wins. If regulation play expires with the score tied, most basketball leagues mandate additional periods of play (overtime) until the score is no longer tied.Players advance the ball by bouncing it while walking or running (dribbling) or by passing it to a teammate, both of which require considerable skill. On offense, players may use a variety of shots – the layup, the jump shot, or a dunk; on defense, they may steal the ball from a dribbler, intercept passes, or block shots; either offense or defense may collect a rebound, that is, a missed shot that bounces from rim or backboard. It is a violation to lift or drag one's pivot foot without dribbling the ball, to carry it, or to hold the ball with both hands then resume dribbling." },
#     {"id": 2, "name": "Volleyball", "img": "Volleyball.jpg", "description": "Volleyball is a fast-paced team sport played by two teams of six on a court divided by a net, aiming to land the ball in the opponent's court. Teams use up to three hits to return the ball, focusing on a pass-set-spike sequence to score.", "des_long": "Volleyball was invented in 1895 by the American educator William G. Morgan, a YMCA physical education director in Holyoke, Massachusetts. Morgan intended the game, which he originally called “mintonette”, to be an alternative to basketball that was less physically demanding. It spread rapidly through YMCA networks in the United States and abroad. An international governing body, the Fédération Internationale de Volleyball (FIVB), was established in 1947, and the sport grew into a global phenomenon. Its social history has included diverse communities such as nudists and, more recently, debates over inclusion and fairness regarding transgender athletes."},
#     {"id": 3, "name": "Golf", "img": "Golf.jpg", "description": "Golf is a precision club-and-ball sport where players use various clubs to hit a ball into a series of holes (usually 9 or 18) on a large outdoor course in the fewest strokes possible", "des_long": "Golf is a club-and-ball sport in which players use various clubs to hit a ball into a series of holes on a course in as few strokes as possible.Golf, unlike most ball games, cannot and does not use a standardized playing area, and coping with the varied terrains encountered on different courses is a key part of the game. Courses typically have either 9 or 18 holes, regions of terrain that each contain a cup, the hole that receives the ball. Each hole on a course has a teeing ground for the hole's first stroke, and a putting green containing the cup. There are several standard forms of terrain between the tee and the green, such as the fairway, rough (tall grass), and various hazards that may be water, rocks, or sand-filled bunkers. Each hole on a course is unique in its specific layout. Many golf courses are designed to resemble their native landscape, such as along a sea coast (where the course is called a links), within a forest, among rolling hills, or part of a desert."},
#     {"id": 4, "name": "Rugby", "img": "Rugby.jpg", "description": "Rugby is a full-contact team sport developed in 19th-century England, characterized by running with an oval ball to score points by touching it down in the opponent's end zone or kicking it through goalposts.", "des_long": "Rugby union football, commonly known simply as rugby union or often just rugby, is a close-contact team sport that originated at Rugby School in England in the first half of the 19th century. Rugby involves running with the ball in hand. In its most common form, the game is played between two teams of 15 players each, using an oval-shaped ball on a rectangular field called a pitch. The field has H-shaped goalposts at both ends. The objective of the game is to score more points than the opposing team by scoring tries, conversion kicks, penalties, and drop goals.Rugby union is a popular sport around the world, played by people regardless of gender, age or size.[3] In 2023, there were more than 10 million players worldwide, of whom 8.4 million were registered. World Rugby, previously called the International Rugby Football Board (IRFB) and the International Rugby Board (IRB), has been the governing body for rugby union since 1886, and currently has 116 countries as full members and 18 associate members."},
#     {"id": 5, "name": "Tennis", "img": "Tennis.jpg", "description": "Tennis is a racket sport played individually (singles) or in pairs (doubles) on a rectangular court divided by a net, aiming to hit a felt-covered ball into the opponent's court so they cannot return it. Players use stringed rackets to score points.", "des_long": "Tennis is a racket sport that is played either individually against a single opponent (singles) or between two teams of two players each (doubles). Each player uses a tennis racket strung with a cord to strike a hollow rubber ball covered with felt over or around a net and into the opponent's court. The object is to manoeuvre the ball in such a way that the opponent is not able to play a valid return. If a player is unable to return the ball successfully, the opponent scores a point. Tennis can be played by anyone who can hold a racket, including wheelchair users, and is played by people at every level of society and across all ages. The original forms of tennis developed in France during the late Middle Ages.[3] The modern form of tennis originated in Birmingham, England, in the late 19th century as lawn tennis.[4] It had close connections to various field (lawn) games such as croquet and bowls as well as to the older racket sport today called real tennis.[5]"},
#     {"id": 6, "name": "Football", "img": "Football.jpg", "description": "Football is the world's most popular sport, featuring two teams of 11 players aiming to score by moving a ball into the opponent's net. Played mainly with the feet, it focuses on skill and tactics, with 90-minute matches overseen by a referee.", "des_long": "Football is a family of team sports in which the object is to get the ball over a goal line, into a goal, or between goalposts using merely the body (by carrying, throwing, or kicking. vUnqualified, the word football generally means the form of football that is the most popular where the word is used. Sports commonly called football include association football (known as soccer in Australia, Canada, South Africa, the United States, and sometimes in Ireland and New Zealand); Australian rules football; Gaelic football; gridiron football (specifically American football, arena football, or Canadian football); International rules football; rugby league football; and rugby union football.[4] These various forms of football share, to varying degrees, common origins and are known as 'football codes'."},
#     {"id": 7, "name": "Water Polo", "img": "Polo.jpg", "description": "Water polo is a fast-paced, highly physical team sport played in deep water, combining elements of rugby, soccer, and basketball. Two teams of seven players (six field players, one goalie) attempt to score.", "des_long": "Water polo is a competitive team sport played in water between two teams of seven players each. The game consists of four quarters in which the teams attempt to score goals by throwing the ball into the opposing team's goal. The team with more goals at the end of the game wins the match. Each team is made up of six field players and one goalkeeper. Excluding the goalkeeper, players participate in both offensive and defensive roles. It is typically played in an all-deep pool where players cannot touch the bottom. A game consists mainly of the players swimming to move about the pool, treading water (mainly using the eggbeater kick), passing the ball, and shooting at the goal. Teamwork, tactical thinking and awareness are also highly important aspects. Water polo is a highly physical and demanding sport and has frequently been cited as one of the most difficult to play.[1][2][3]"},
#     {"id": 8, "name": "Dancing", "img": "Dancing.jpg", "description": "Dance is the artistic, rhythmic movement of the body in time and space, often accompanied by music to express emotions, stories, or social interaction. It involves structured steps or improvised gestures, ranging from high-energy.", "des_long": "Dance is an art form, consisting of sequences of body movements with aesthetic and often symbolic value, either improvised or purposefully selected. Dance can be categorized and described by its choreography, by its repertoire of movements or by its historical period or place of origin. Dance is typically performed with musical accompaniment, and sometimes with the dancer simultaneously using a musical instrument themselves. Two common types of group dance are theatrical and participatory dance. Both types of dance may have special functions, whether social, ceremonial, competitive, erotic, martial, sacred or liturgical. Dance is not solely restricted to performance, as dance is used as a form of exercise and occasionally training for other sports and activities. Dance performances and dancing competitions are found across the world exhibiting various different styles and standards."},
# ]


@app.route("/")
def home():
    sports = Sport.query.all()
    return render_template("index.html", sports=sports)  # HTML-ისთვის ცვლადის გადაცემა


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = {
            "username": form.username.data,
            "mobile": form.mobile.data,
            "date": form.birthdate.data,
        }
        img = form.image.data  # None
        if img:  # None-ის გარდა ნებისმიერი რაღაც იქნება True
            directory = path.join(app.root_path, "static", "images", img.filename)
            new_user["img"] = img.filename
            img.save(directory)
        profiles.append(new_user)
        return redirect("/")
    return render_template("register.html", form=form)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/profile/<int:profile_id>")  # profile_id დინამიური ცვლადია, რომელიც int ტიპია (int:) ამ შემთხვევაში. default-ად სტრინგია
def profile(profile_id):
    profile = profiles[profile_id]
    return render_template("profile.html", profile=profile)


@app.route("/sport/<int:sport_id>")
def view_sport_details(sport_id):
    sport = Sport.query.get(sport_id)
    return render_template("sport_details.html", sport=sport)


# routes.py
@app.route("/add_sport", methods=["GET", "POST"])
def add_sport():
    form = SportForm()
    if form.validate_on_submit():
        new_sport = Sport(
            name=form.name.data,
            description=form.description.data,
            desc_long=form.desc_long.data,
            img=""
        )
        img = form.img.data
        if img:
            directory = path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)
            new_sport.img = img.filename

        try:
            db.session.add(new_sport)
            db.session.commit()
            print("Sport saved!")
            return redirect(url_for("add_sport"))
        except Exception as e:
            db.session.rollback()
            print("DB Error:", e)

    print("Form errors:", form.errors)
    return render_template("add_sport.html", form=form)
