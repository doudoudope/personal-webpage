from flask import Flask, render_template
from flask import abort  # among other things

def create_app():
    app = Flask(__name__)
    projects = [
        {
            "name": "Habit tracking app with Python and MongoDB",
            "thumb": "img/habit.png",
            "hero": "img/habit-tracking-hero.png",
            "categories": ["python", "web"],
            "slug": "habit-tracking",
            "prod": "https://daily-tracker-sarah.herokuapp.com/",
        },
        {
            "name": "Microblog app with Python and MongoDB",
            "thumb": "img/microblog.png",
            "hero": "img/microblog-hero.png",
            "categories": ["javascript", "web"],
            "slug": "microblog",
            "prod": "https://sarah-microblog-app.herokuapp.com/"
        },
        {
            "name": "Movie watchlist app with Javascript",
            "thumb": "img/movie.png",
            "hero": "img/rest-api-docs.png",
            "categories": ["javascript"],
            "slug": "movie-watchlist",
        },
    ]

    slug_to_project = {project["slug"]: project for project in projects}

    @app.route("/")
    def home():
        return render_template("home.html", projects = projects)


    @app.route("/about")
    def about():
        return render_template("about.html")


    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template(f"project_{slug}.html", project=slug_to_project[slug])

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404
    
    return app