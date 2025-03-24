import psycopg2

if __name__ == '__main__':
    con = psycopg2.connect(
        database='movie2023',
        user='db2023',
        password='db!2023',
        host='::1',
        port='5432'
    )


def fetch_members_data():
    cursor = con.cursor()
    cursor.execute("SELECT id, password, member_id FROM Member")
    members_data_from_db = cursor.fetchall()
    return members_data_from_db


def login_attempt():
    members_data = fetch_members_data()

    input_id1 = input("Enter ID: ")
    input_password1 = input("Enter password: ")

    for member in members_data:
        if input_id1 == member[0] and input_password1 == member[1]:
            print("Login successful!")
            user_type = distinguish_user(input_id1)
            return user_type, member[2], input_id1, input_password1

    print("Login failed. ID and password do not match any records.")
    return False, 1, "fail_id", "fail_password"


def login():
    user_type, member_id, input_id1, input_password1 = login_attempt()

    if not user_type:
        while not user_type:
            user_type, member_id, input_id1, input_password1 = login_attempt()
    return user_type, member_id, input_id1, input_password1


def contains_substring(main_string, substring):
    return substring in main_string


def distinguish_user(input_id3):
    if contains_substring(input_id3, "user"):
        return "user"
    elif contains_substring(input_id3, "staff"):
        return "staff"
    elif contains_substring(input_id3, "analyst"):
        return "analyst"


def print_user_function():
    function_num = int(input("1. 모든 상영 예정인 영화 조회 하기.\n"
                             "2. 영화 이름 으로  상영 예정인 영화 조회 하기.\n"
                             "3. 영화 제목 글자 수로 상영 예정인 영화 조회 하기.\n"
                             "4. 영화 제목을 기준 으로 상영 예정인 영화를 오름차순으로 정렬 하기.\n"
                             "5. 영화 상영 날짜를 기준 으로 상영 예정인 영화를 내림차순으로 정렬 하기.\n"
                             "6. 영화 예매 하기.\n"
                             "7. 영화 취소 하기.\n"
                             "8. 프로그램 종료 하기.\n"))
    return function_num


def print_staff_function():
    function_num = int(input("1. 멤버(사용자, 영화관 관계자, 영화 분석가 모두)의 회원id, 아이디, 비밀번호, 이름만 조회하기 (전화번호는 조회할 수 없음).\n"
                             "2. 상영 예정인 영화에 대한 정보인 영화제목, 배우, 감독의 "
                             "조건에 따라 영화를 조회 가능하다.\n"
                             "3. 상영 예정인 영화에 대한 정보인 영화제목, 배우, 감독 같은"
                             "조건에 따라 영화를 갱신 가능하다.\n"
                             "4. 영화 관객이 작성한 평점을 추가 한다.\n"
                             "5. 영화 관객이 작성한 평점을 조회 한다.\n"
                             "6. 모든 배우 별로 각자 출연한 영화의 평균 평점을 조회 하는데 평균"
                             "평점이 2.5점 이상인 그룹만 조회한다.\n"
                             "7. 프로그램 종료 하기.\n"))
    return function_num


def print_analyst_function():
    function_num = int(input("1. 영화 제목이 'The Matrix' 와 'John Wick' 인 영화를 모두 관람한 관객 이름을 조회한다.\n"
                             "2. 영화 제목이 'The Matrix' 와 'John Wick' 인 영화 두 작품 중 한 작품 이상 관람한 관객 이름을 조회한다.\n"
                             "3. 영화 제목이 'The Matrix' 와 'John Wick' 인 영화 중 'The Matrix'는 관람하고 'John Wick'는 "
                             "관람하지 않은 관객 이름을 조회한다.\n"
                             "4. 영화를 보고 관객이 부여한 평점이 평점이 달린 모든 영화의 평균 평점보다 높았던 경험이 있는"
                             "회원 id를 조회한다.\n"
                             "5. 가장 높은 평점을 받은 모든 영화를 조회한다.\n"
                             "6. 프로그램 종료 하기.\n"))
    return function_num


def print_all_movie():
    cursor = con.cursor()

    cursor.execute("select distinct m.movie_id, movie_title , theater_id, screening_date "
                   "from movie m ,screeningschedule s "
                   "where m.movie_id = s.movie_id and screening_date >= current_date")
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)


def print_movie_title():
    while True:
        movie_title = input("원하는 영화 제목을 입력 하세요\n")
        cursor = con.cursor()
        # Check if the index already exists
        cursor.execute("SELECT EXISTS(SELECT 1 FROM pg_indexes WHERE indexname = 'idx_movie_title')")
        index_exists = cursor.fetchone()[0]

        if not index_exists:
            cursor.execute("CREATE INDEX idx_movie_title ON movie(movie_title)")
            con.commit()

        # Perform the query using the index
        cursor.execute("SELECT DISTINCT m.movie_id, movie_title, theater_id, screening_date "
                       "FROM movie m, \"screeningschedule\" s "
                       "WHERE m.movie_id = s.movie_id AND screening_date >= current_date "
                       "AND m.movie_title = %s", (movie_title,))
        result = cursor.fetchall()

        if not result:
            print(f"입력한 '{movie_title}'가 제목인 영화는 존재하지 않습니다. 다시 입력하세요.")
        else:
            for r in result:
                print(r)
            break


def print_movie_num():
    while True:
        movie_title_num = int(input("원하는 영화 제목의 글자 수를 입력 하세요\n"))
        cursor = con.cursor()
        movie_title_struct = ""
        for i in range(movie_title_num):
            movie_title_struct += "_"
        cursor.execute("select distinct m.movie_id, movie_title , theater_id, screening_date "
                       "from movie m ,screeningschedule s "
                       "where m.movie_id = s.movie_id and screening_date >= current_date "
                       "and m.movie_title like %s", (movie_title_struct,))
        con.commit()
        result = cursor.fetchall()

        if not result:
            print(f"입력한 영화 제목의 글자수가 '{movie_title_num}'인 영화는 존재하지 않습니다. 다시 입력하세요.")
        else:
            for r in result:
                print(r)
            break


def sort_movie_title():
    cursor = con.cursor()
    cursor.execute("select distinct m.movie_id, movie_title , theater_id, screening_date "
                   "from movie m ,screeningschedule s "
                   "where m.movie_id = s.movie_id and screening_date >= current_date "
                   "order by movie_title asc")
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)


def sort_movie_screening_date():
    cursor = con.cursor()
    cursor.execute("select distinct m.movie_id, movie_title , theater_id, screening_date "
                   "from movie m ,screeningschedule s "
                   "where m.movie_id = s.movie_id and screening_date >= current_date "
                   "order by screening_date desc")
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)


def print_movie_actor():
    while True:
        movie_actor = input("원하는 배우 이름을 입력 하세요\n")
        cursor = con.cursor()
        # Check if the index already exists
        cursor.execute("SELECT EXISTS(SELECT 1 FROM pg_indexes WHERE indexname = 'idx_actor_name')")
        index_exists = cursor.fetchone()[0]

        if not index_exists:
            # Create the index if it doesn't exist
            cursor.execute("CREATE INDEX idx_actor_name ON movie(actor)")
            con.commit()

        # Perform the query using the index
        cursor.execute("SELECT DISTINCT m.movie_id, movie_title, theater_id, screening_date "
                       "FROM movie m, \"screeningschedule\" s "
                       "WHERE m.movie_id = s.movie_id AND screening_date >= current_date "
                       "AND m.actor = %s", (movie_actor,))
        result = cursor.fetchall()

        if not result:
            print(f"입력한 '{movie_actor}'의 이름을 가진 배우는 존재하지 않습니다. 다시 입력하세요.")
        else:
            for r in result:
                print(r)
            break


def print_movie_director():
    while True:
        movie_director = input("원하는 감독 이름을 입력 하세요\n")
        cursor = con.cursor()
        # Check if the index already exists
        cursor.execute("SELECT EXISTS(SELECT 1 FROM pg_indexes WHERE indexname = 'idx_director_name')")
        index_exists = cursor.fetchone()[0]

        if not index_exists:
            # Create the index if it doesn't exist
            cursor.execute("CREATE INDEX idx_director_name ON movie(director)")
            con.commit()

        # Perform the query using the index
        cursor.execute("SELECT DISTINCT m.movie_id, movie_title, theater_id, screening_date "
                       "FROM movie m, \"screeningschedule\" s "
                       "WHERE m.movie_id = s.movie_id AND screening_date >= current_date "
                       "AND m.director = %s", (movie_director,))
        result = cursor.fetchall()

        if not result:
            print(f"입력한 '{movie_director}'의 이름을 가진 감독은 존재하지 않습니다. 다시 입력하세요.")
        else:
            for r in result:
                print(r)
            break


def update_movie_title():
    cursor = con.cursor()
    while True:
        old_movie_title = input("갱신 시킬 영화 제목을 입력 하세요.\n")
        cursor.execute("SELECT DISTINCT movie_title FROM movie m,\"screeningschedule\" s "
                       "WHERE movie_title = %s and m.movie_id = s.movie_id AND screening_date >= current_date",
                       (old_movie_title,))
        existing_movie_title = cursor.fetchone()

        if existing_movie_title:
            break  # Exit the loop if the entered actor name exists
        else:
            print(f"The movie_title '{old_movie_title}' does not exist. Please enter a valid actor name.")

    new_movie_title = input("새로운 영화 제목을 입력 하세요.\n")

    cursor.execute("update movie set movie_title = %s where movie_title = %s", (new_movie_title, old_movie_title))

    cursor.execute("select distinct movie_title, summary , actor, director "
                   "from movie "
                   "where movie_title = %s", (new_movie_title,))
    con.commit()
    result = cursor.fetchall()
    print("갱신된 정보를 출력 하겠습니다.")
    for r in result:
        print(r)


def update_movie_actor():
    cursor = con.cursor()
    while True:
        old_actor_name = input("갱신 시킬 영화 배우 이름을 입력 하세요.\n")
        cursor.execute("SELECT DISTINCT actor FROM movie m,\"screeningschedule\" s "
                       "WHERE actor = %s and m.movie_id = s.movie_id AND screening_date >= current_date",
                       (old_actor_name,))
        existing_actor = cursor.fetchone()

        if existing_actor:
            break
        else:
            print(f"The actor '{old_actor_name}' does not exist. Please enter a valid actor name.")

    new_actor_name = input("새로운 영화 배우 이름을 입력 하세요.\n")

    cursor.execute("update movie set actor = %s where actor = %s", (new_actor_name, old_actor_name))

    cursor.execute("select distinct movie_title, summary , actor, director "
                   "from movie "
                   "where actor = %s", (new_actor_name,))
    con.commit()
    result = cursor.fetchall()
    print("갱신된 정보를 출력 하겠습니다.\n")
    for r in result:
        print(r)


def update_movie_director():
    cursor = con.cursor()
    while True:
        old_director_name = input("갱신 시킬 감독 이름을 입력 하세요.\n")
        cursor.execute("SELECT DISTINCT director FROM movie m,\"screeningschedule\" s "
                       "WHERE director = %s and m.movie_id = s.movie_id AND screening_date >= current_date",
                       (old_director_name,))
        existing_director = cursor.fetchone()

        if existing_director:
            break  # Exit the loop if the entered actor name exists
        else:
            print(f"The director '{old_director_name}' does not exist. Please enter a valid director name.")

    new_director_name = input("새로운 영화 감독 이름을 입력 하세요.\n")

    cursor.execute("update movie set director = %s where director = %s", (new_director_name, old_director_name))

    cursor.execute("select distinct movie_title, summary , actor, director "
                   "from movie "
                   "where director = %s", (new_director_name,))
    con.commit()
    result = cursor.fetchall()
    print("갱신된 정보를 출력 하겠습니다.\n")
    for r in result:
        print(r)


def valid_movie_id(result):
    while True:
        try:
            movie_id = int(input("Enter the movie ID: "))

            if any(movie_id == r[0] for r in result):
                print(f"You selected movie_id {movie_id}.")
                return movie_id

            else:
                print("Invalid movie ID. Please enter a valid movie ID.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for movie ID.")


def print_movie():
    cursor = con.cursor()

    print("상영 예정 영화의 movie_id와 movie_title을 출력 합니다. ")
    cursor.execute("select distinct m.movie_id, m.movie_title "
                   "from movie m ,screeningschedule s "
                   "where m.movie_id = s.movie_id and screening_date >= current_date")
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)

    return result


def valid_screening_date_id(result):
    while True:
        try:
            screening_date_id = int(input("Enter the screening date ID : "))

            if any(screening_date_id == r[0] for r in result):
                print(f"You selected screening_date_id {screening_date_id}.")
                return screening_date_id
            else:
                print("Invalid screening_date_id. Please enter a valid screening_date_id.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for screening_date_id.")


def print_screening_schedule(movie_id):
    cursor = con.cursor()

    print("해당 movie_id인 영화의 screening_date_id, screening_date를 출력 합니다.")
    cursor.execute("select distinct screening_date_id, screening_date  from screeningschedule s where s.movie_id = %s",
                   (movie_id,))
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)
    return result


def print_theater(movie_id, screening_date_id):
    cursor = con.cursor()
    print("해당 movie_id, screening_date_id에 맞는 theater_id와 total_seat를 출력 합니다.")
    cursor.execute("select distinct s.theater_id, t.total_seat  from screeningschedule s, theater t "
                   "where s.movie_id = %s and screening_date_id = %s and s.theater_id = t.theater_id",
                   (movie_id, screening_date_id))
    con.commit()
    result = cursor.fetchall()
    for r in result:
        theater_id, total_seat = r
        print(r)
        return theater_id


def valid_seat_id(result):
    while True:
        try:
            seat_id = (int(input("Enter the seat ID: ")))

            if any(seat_id == r[0] for r in result):
                print(f"You selected seat_id {seat_id}.")
                return seat_id

            else:
                print("Invalid seat_id. Please enter a valid seat_id.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for seat_id.")


def print_seat(screening_date_id):
    cursor = con.cursor()
    print("해당 screening_date_id에 맞는 theater의 seat_id를 seat_assignment가 true일 때만 출력 합니다.")
    cursor.execute("select distinct seat_id from seat s where screening_date_id "
                   "= %s and seat_assignment = true", (screening_date_id,))
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)
    return result


def valid_pay_method():
    while True:
        pay_method = input("Select payment method (Credit Card / Debit Card / Cash): ")

        if pay_method.lower() in ['credit card', 'debit card', 'cash']:
            return pay_method
        else:
            print("Invalid payment method. Please enter Credit Card, Debit Card, or Cash.")


def print_reservation_id(price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id):
    print("Reservation successful! Reservation ID를 출력 하겠습니다. ")
    cursor = con.cursor()
    cursor.execute("select distinct reservation_id from reservation r where price = %s "
                   "and pay_method = %s and screening_date_id = %s and "
                   "theater_id = %s and seat_id = %s and movie_id = %s and member_id = %s",
                   (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id))
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)


def reservation_movie(member_id):
    try:
        cursor = con.cursor()

        print("로그인 하신 member_id는 " + str(member_id) + " 입니다.")
        # Step 1: Select Information for Reservation
        print("이제 예약 하실 정보를 입력 받겠습니다.")

        result1 = print_movie()
        movie_id = valid_movie_id(result1)

        result2 = print_screening_schedule(movie_id)
        screening_date_id = valid_screening_date_id(result2)

        theater_id = print_theater(movie_id, screening_date_id)
        # 상영스케쥴이 정해지면 영화는 한 상영관에서만 상영되므로 정해진 상영관을 받아온다.

        result4 = print_seat(screening_date_id)
        seat_id = valid_seat_id(result4)

        pay_method = valid_pay_method()

        price = 8000
        cursor.execute("BEGIN")

        cursor.execute(
            "INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id))

        cursor.execute("update seat set seat_assignment = false where seat_id = %s", (seat_id,))
        con.commit()

        print_reservation_id(price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id)

    except Exception as e:
        print(f"Error : {e}")
        con.rollback()


def valid_reservation_id(result):
    while True:
        try:
            reservation_id = int(input("예매를 취소할 reservation ID를 입력하세요 : "))

            if any(reservation_id == r[0] for r in result):
                print(f"You selected reservation_id {reservation_id}.")
                return reservation_id
            else:
                print("Invalid reservation_id. Please enter a valid reservation_id.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for reservation_id.")


def print_reservation(member_id):
    cursor = con.cursor()
    cursor.execute("select * from reservation r where member_id = %s", (member_id,))
    con.commit()
    result = cursor.fetchall()
    print("member_id가 " + str(member_id) + "인 회원 님의 reservation 정보를 "
                                           " reservation_id, price, pay_method, screening_date_id, theater_id,"
                                           " seat_id, movie_id, member_id 순으로 출력합니다.")
    for r in result:
        print(r)
    return result


def find_seat_id(reservation_id):
    cursor = con.cursor()
    cursor.execute("select distinct s.seat_id from seat s , reservation r "
                   "where r.seat_id = s.seat_id and reservation_id = %s", (reservation_id,))
    con.commit()
    result = cursor.fetchone()
    return result


def delete_reservation(member_id):
    try:
        result = print_reservation(member_id)
        reservation_id = valid_reservation_id(result)
        seat_id = find_seat_id(reservation_id)

        cursor = con.cursor()
        # 이거 grant?
        cursor.execute("BEGIN")

        cursor.execute("delete from reservation where reservation_id = %s", (reservation_id,))
        cursor.execute("update seat set seat_assignment = true where seat_id = %s", (seat_id,))

        con.commit()

    except Exception as e:
        print(f"Error : {e}")
        con.rollback()


def start_user_function(function_num, member_id):
    if function_num == 1:
        print("모든 상영 예정인 영화 조회")
        print_all_movie()
    elif function_num == 2:
        print("영화 이름 으로  상영 예정인 영화 조회")
        print_movie_title()

    elif function_num == 3:
        print("영화 제목 글자 수로 상영 예정인 영화 조회")
        print_movie_num()

    elif function_num == 4:
        print("영화 제목을 기준 으로 상영 예정인 영화를 오름차순으로 정렬")
        sort_movie_title()

    elif function_num == 5:
        print("영화 상영 날짜를 기준 으로 상영 예정인 영화를 내림차순으로 정렬")
        sort_movie_screening_date()

    elif function_num == 6:
        print("영화 예매")
        reservation_movie(member_id)

    elif function_num == 7:
        print("예매 취소")
        delete_reservation(member_id)


def print_user_info():
    cursor = con.cursor()

    cursor.execute("SELECT EXISTS(SELECT 1 FROM information_schema.views WHERE table_name = 'user_info')")
    view_exists = cursor.fetchone()[0]

    if not view_exists:
        cursor.execute("CREATE VIEW user_info AS "
                       "SELECT member_id, id, password, name FROM member m")
        con.commit()

    cursor.execute("SELECT * FROM user_info")
    result = cursor.fetchall()

    for r in result:
        print(r)


def search_movie():
    function_num = int(input("상영 예정인 영화 정보를 조회할 조건을 선택 하세요.\n"
                             "1. 영화 제목\n"
                             "2. 배우\n"
                             "3. 감독\n"))
    if function_num == 1:
        print_movie_title()
    elif function_num == 2:
        print_movie_actor()
    elif function_num == 3:
        print_movie_director()


def update_movie():
    function_num = int(input("상영 예정인 영화 정보를 갱신할 조건을 선택 하세요.\n"
                             "1. 영화 제목\n"
                             "2. 배우\n"
                             "3. 감독\n"))
    if function_num == 1:
        update_movie_title()
    elif function_num == 2:
        update_movie_actor()
    elif function_num == 3:
        update_movie_director()


def print_old_movie():
    cursor = con.cursor()

    print("상영 했던 영화의 movie_id와 movie_title을 출력 합니다. ")
    cursor.execute("select distinct m.movie_id, m.movie_title "
                   "from movie m ,screeningschedule s "
                   "where m.movie_id = s.movie_id and screening_date <= current_date")
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)

    return result


def print_member_id():
    cursor = con.cursor()

    print("멤버 아이디, 이름을 출력하겠습니다.")
    cursor.execute("select distinct m.member_id , m.name "
                   "from member m ")
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)

    return result


def add_review():
    cursor = con.cursor()

    while True:
        rating = input("평점으로 0~5사이의 정수를 입력하세요.\n")
        try:
            rating = int(rating)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        if 0 <= rating <= 5:
            break
        else:
            print("Invalid rating. Please enter a value between 0 and 5.")

    print_old_movie()
    movie_id = input("Enter the movie_id for the entered rating.\n")

    print_member_id()
    member_id = input("Enter the member_id who wrote the review.\n")

    cursor.execute(
        "INSERT INTO review (rating, movie_id, member_id) VALUES (%s, %s, %s) "
        "RETURNING review_id, rating, movie_id, member_id",
        (rating, movie_id, member_id))
    con.commit()

    result = cursor.fetchone()

    if result:
        print("추가된 review 정보를 review_id, rating, movie_id, member_id 순으로 출력하겠습니다.\n")
        print(result)
    else:
        print("No results returned after the INSERT.")

    cursor.close()


def print_review():
    cursor = con.cursor()
    cursor.execute("select * from review r")
    con.commit()
    result = cursor.fetchall()
    print("review_id, 평점, movie_id, member_id 순으로 출력 합니다.\n ")
    for r in result:
        print(r)


def print_good_actor():
    cursor = con.cursor()
    cursor.execute("select distinct movie.actor, avg(review.rating) as avg_rating "
                   "from movie join review on movie.movie_id = review.movie_id "
                   "group by movie.actor having avg(review.rating)>=2.5;")
    con.commit()
    result = cursor.fetchall()
    print("영화 배우와 평균 평점을 출력 합니다.")
    for r in result:
        print(r)


def start_staff_function(function_num):
    if function_num == 1:
        print("멤버(사용자, 영화관 관계자, 영화 분석가 모두)의 회원id, 아이디,"
              " 비밀번호, 이름만 조회 (전화번호는 조회할 수 없음)")
        print_user_info()
    elif function_num == 2:
        print("상영 예정인 영화에 대한 정보인 영화제목, 배우, 감독의 조건에 따라 영화를 조회 가능")
        search_movie()
    elif function_num == 3:
        print("상영 예정인 영화에 대한 정보인 영화제목, 배우, 감독 같은"
              "조건에 따라 영화를 갱신 가능")
        update_movie()
    elif function_num == 4:
        print("영화 관객이 작성한 평점을 추가")
        add_review()
    elif function_num == 5:
        print("영화 관객이 작성한 평점을 조회")
        print_review()
    elif function_num == 6:
        print("모든 배우 별로 각자 출연한 영화의 평균 평점을 조회 하는데 평균"
              "평점이 2.5점 이상인 그룹만 조회")
        print_good_actor()


def print_both_movie_watch():
    cursor = con.cursor()
    cursor.execute("select distinct name from member m, reservation r , movie mv "
                   "where m.member_id = r.member_id and mv.movie_title = 'The Matrix' and r.movie_id = mv.movie_id "
                   "intersect select name from member m, reservation r , movie mv "
                   "where m.member_id = r.member_id and mv.movie_title  = 'John Wick' and r.movie_id = mv.movie_id")
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)


def print_one_more_movie_watch():
    cursor = con.cursor()
    cursor.execute("select distinct name from member m, reservation r , movie mv "
                   "where m.member_id = r.member_id and mv.movie_title = 'The Matrix' and r.movie_id = mv.movie_id "
                   "union select name from member m, reservation r , movie mv "
                   "where m.member_id = r.member_id and mv.movie_title  = 'John Wick' and r.movie_id = mv.movie_id")
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)


def print_one_movie_watch():
    cursor = con.cursor()
    cursor.execute("select distinct name from member m, reservation r , movie mv "
                   "where m.member_id = r.member_id and mv.movie_title = 'The Matrix' and r.movie_id = mv.movie_id "
                   "except select name from member m, reservation r , movie mv "
                   "where m.member_id = r.member_id and mv.movie_title  = 'John Wick' and r.movie_id = mv.movie_id")
    con.commit()
    result = cursor.fetchall()
    for r in result:
        print(r)


def print_member_high_rate():
    cursor = con.cursor()
    cursor.execute("SELECT AVG(r2.rating) FROM review r2")
    avg_rating = cursor.fetchone()
    print("평균 평점:", avg_rating[0])

    cursor.execute("SELECT member_id, id FROM member")
    member_ids = cursor.fetchall()

    for member_id in member_ids:
        member_id, member_type = member_id
        if distinguish_user(member_type) == "user":
            cursor.execute(f"SELECT MAX(rating) FROM review WHERE member_id = {member_id}")
            max_rating = cursor.fetchone()
            print(f"멤버 {member_id}의 최대 평점:", max_rating[0])

    cursor.execute("SELECT DISTINCT r1.member_id FROM review r1 "
                   "WHERE r1.rating > (SELECT AVG(r2.rating) FROM review r2)")
    above_avg_members = cursor.fetchall()
    print("평균 평점보다 높은 평점을 준 멤버: ", above_avg_members)

    con.commit()


def print_best_movie():
    cursor = con.cursor()
    cursor.execute("with max_rating (value) as (select max(rating) from review) "
                   "select distinct m.movie_title , value from movie m, review r, max_rating "
                   "where m.movie_id = r.movie_id and r.rating = max_rating.value")
    con.commit()
    result = cursor.fetchall()
    print("가장 높은 평점을 받은 모든 영화 제목과 최고 평점을 출력 합니다.")
    for r in result:
        print(r)


def start_analyst_function(function_num):
    if function_num == 1:
        print("영화 제목이 'The Matrix' 와 'John Wick' 인 영화를 모두 관람한 관객 이름을 조회")
        print_both_movie_watch()
    elif function_num == 2:
        print("영화 제목이 'The Matrix' 와 'John Wick' 인 영화 두 작품 중"
              " 한 작품 이상 관람한 관객 이름을 조회")
        print_one_more_movie_watch()
    elif function_num == 3:
        print("영화 제목이 'The Matrix' 와 'John Wick' 인 영화 중 "
              "'The Matrix'는 관람하고 'John Wick'는 "
              "관람하지 않은 관객 이름을 조회")
        print_one_movie_watch()
    elif function_num == 4:
        print("영화를 보고 관객이 부여한 평점이 평점이 달린 모든 영화의 "
              "평균 평점보다 높았던 경험이 있는 회원 id를 조회")
        print_member_high_rate()
    elif function_num == 5:
        print("가장 높은 평점을 받은 모든 영화를 조회")
        print_best_movie()


def user_function(member_id):
    flag = True
    function_num = print_user_function()
    while flag:
        if function_num == 8:
            print("프로그램을 종료 합니다.")
            flag = False
        else:
            start_user_function(function_num, member_id)
            function_num = int(input((userType + "님 원하는 기능을 선택 하세요.\n")))


def staff_function():
    flag = True
    function_num = print_staff_function()
    while flag:
        if function_num == 7:
            print("프로그램을 종료 합니다.")
            flag = False
        else:
            start_staff_function(function_num)
            function_num = int(input((userType + "님 원하는 기능을 선택 하세요.\n")))


def analyst_function():
    flag = True
    function_num = print_analyst_function()
    while flag:
        if function_num == 6:
            print("프로그램을 종료 합니다.")
            flag = False
        else:
            start_analyst_function(function_num)
            function_num = int(input((userType + "님 원하는 기능을 선택 하세요.\n")))


userType, memberId, input_id, input_password = login()

print("안녕 하세요! " + userType + "님 원하는 기능을 선택 하세요.\n")

if userType == "user":
    user_function(memberId)
elif userType == "staff":
    staff_function()
elif userType == "analyst":
    analyst_function()
