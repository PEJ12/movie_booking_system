from flask import render_template, request, redirect, url_for, flash
from models import fetch_members_data, distinguish_user, print_all_movie, get_movie_by_title, sort_movie,print_movie, valid_id, print_screening_schedule, get_movie_title, print_theater, print_seat

def login_route(app):
    @app.route("/", methods=["GET", "POST"])
    def login():
        #데스트탑에서 수정함
        if request.method == "POST":
            input_id = request.form['user_id']
            input_password = request.form['password']

            members_data = fetch_members_data()

            for member in members_data:
                if input_id == member[0] and input_password == member[1]:
                    user_type = distinguish_user(input_id)
                    if user_type:
                        return redirect(url_for('dashboard', user_type=user_type, name=member[2], member_id = member[3] ))
                    else:
                        flash("User type could not be determined.")
                        return redirect(url_for('login'))

            flash("Login failed. ID and password do not match.")
            return redirect(url_for('login'))

        return render_template("login.html")

    @app.route("/dashboard")
    def dashboard():
        user_type = request.args.get('user_type')
        name = request.args.get('name')
        member_id = request.args.get('member_id')
        if user_type == "user":
            return render_template("user_function.html", name=name, member_id=member_id)
        elif user_type == "staff":
            return render_template("staff_function.html", name=name, member_id=member_id)
        elif user_type == "analyst":
            return render_template("analyst_function.html", name=name, member_id=member_id)

    @app.route("/movies/book/<name>/<int:member_id>", methods=['GET', 'POST'])
    def book_movie(name, member_id):
        result1 = print_movie()
        message = ""
        if request.method == "POST":
            movie_id = request.form['movie_id']
            if not movie_id:
                flash("Movie ID is required! Please enter a valid ID.")
                return redirect(url_for('book_movie', name=name, member_id=member_id))
            else:
                try:
                    movie_id = int(movie_id)
                    if valid_id(movie_id, result1):
                    # 유효한 경우, 다음 페이지로 이동
                        return redirect(url_for('select_screening_date_id', name=name, member_id=member_id, movie_id=movie_id))
                    else:
                        flash("Invalid movie ID. Please enter a valid movie ID.")
                        return  redirect(url_for('book_movie', name=name, member_id=member_id))
                except ValueError:
                    flash("Invalid input. Please enter a valid integer for movie ID.")
                    return redirect(url_for('book_movie', name=name, member_id=member_id))
        return render_template('user/book_movie_4.html', name=name, member_id=member_id, movies=result1,  message=message)


    @app.route("/movies/book/screening_date_id/<name>/<int:member_id>/<int:movie_id>")
    def select_screening_date_id(name, member_id, movie_id):
        result2 = print_screening_schedule(movie_id)
        movie_title = get_movie_title(movie_id)
        return render_template('user/screening_date_id_4.html', name=name, member_id=member_id, movie_id=movie_id, movie_title=movie_title, result=result2)

    @app.route("/movies/book/valid_screening")
    def select_screening():
        name = request.args.get('name')
        member_id = int(request.args.get('member_id'))
        movie_id = int(request.args.get('movie_id'))
        screening_date_id = int(request.args.get('screening_date_id'))

        theater_id, total_seat = print_theater(movie_id, screening_date_id)
        seat_id = print_seat(screening_date_id)

        return render_template('user/seat_id_4.html', name=name, member_id=member_id, movie_id=movie_id, screening_date_id=screening_date_id, theater_id=theater_id, total_seat=total_seat, seat_id=seat_id)

    @app.route('/movies/sort')
    def sort_movies():
        movies = sort_movie()
        return render_template('user/print_all_movies_1.html', movies = movies)


    @app.route('/movies')
    def view_movies():
        movies = print_all_movie()
        return render_template('user/print_all_movies_1.html', movies=movies)

    @app.route('/movies/search', methods=['GET', 'POST'])
    def print_movie_title():
        if request.method == 'POST':
            movie_title = request.form['movie_title']
            result = get_movie_by_title(movie_title)
            if not result:
                flash(f"'{movie_title}'에 해당하는 영화가 없습니다. 다시 검색해 주세요.")
                return redirect(url_for('print_movie_title'))
            else:
                return render_template('user/movie_title_results_2.html', movies=result, search_title=movie_title)

        return render_template('user/search_movie_2.html')
