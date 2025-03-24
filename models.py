import sqlite3

def get_db_connection():
    """SQLite 데이터베이스 연결 함수"""
    conn = sqlite3.connect('movies.db') #movies.db는 프로젝트 디렉터리에 저장된 파일
    #conn.row_factory = sqlite3.Row #딕셔너리 형태로 결과를 반환하도록 설정
    return conn

#3
def print_seat(screening_date_id):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("select distinct seat_id from seat s where screening_date_id "
                   "= ? and seat_assignment = 1", (screening_date_id,))
    result = cursor.fetchall()
    con.close()
    return [seat[0] for seat in result]

def print_theater(movie_id, screening_date_id):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("select distinct s.theater_id, t.total_seat  from screeningschedule s, theater t "
                   "where s.movie_id = ? and screening_date_id = ? and s.theater_id = t.theater_id",
                   (movie_id, screening_date_id))
    result = cursor.fetchone()
    con.close()
    return result

#2
def get_movie_title(movie_id):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("select movie_title from movie where movie_id = ?", (movie_id,))
    result = cursor.fetchone()
    con.close()
    return result

def print_screening_schedule(movie_id):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("select distinct screening_date_id, screening_date  from screeningschedule s where s.movie_id = ?",
                   (movie_id,))
    result = cursor.fetchall()
    con.close()
    return result

def valid_id(movie_id, result):
    # 영화 ID가 유효한지 체크하는 함수
    if any(movie_id == r[0] for r in result):
        return True
    return False

def print_movie():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("select distinct m.movie_id, m.movie_title, poster_url "
                   "from movie m ,screeningschedule s "
                   "where m.movie_id = s.movie_id and screening_date >= current_date")
    result = cursor.fetchall()
    con.close()
    return result

def sort_movie():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("select distinct m.movie_id, movie_title , theater_id, screening_date, poster_url "
                   "from movie m ,screeningschedule s "
                   "where m.movie_id = s.movie_id and screening_date >= current_date "
                   "order by DATE(screening_date) desc")
    con.commit()
    result = cursor.fetchall()
    con.close()
    return result

def print_all_movie():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("""SELECT DISTINCT m.movie_id, m.movie_title, s.theater_id, s.screening_date, m.poster_url
            FROM movie m JOIN screeningschedule s ON m.movie_id = s.movie_id
            WHERE s.screening_date >= CURRENT_DATE""")
    result = cursor.fetchall()
    con.close()
    return result

def get_movie_by_title(movie_title):
    con = get_db_connection()
    cursor = con.cursor()

    # Check if the index already exists
    cursor.execute("PRAGMA index_list('movie')")
    indexes = cursor.fetchall()

    index_exists = any(index[1] == 'idx_movie_title' for index in indexes)

    if not index_exists:
         cursor.execute("CREATE INDEX idx_movie_title ON movie(movie_title)")
         con.commit()

    # Perform the query using the index
    cursor.execute("SELECT DISTINCT m.movie_id, movie_title, theater_id, screening_date, poster_url "
                       "FROM movie m, \"screeningschedule\" s "
                       "WHERE m.movie_id = s.movie_id AND screening_date >= current_date "
                       "AND LOWER(m.movie_title) = LOWER(?)", (movie_title,))

    result = cursor.fetchall()

    return result

def fetch_members_data():
    """회원 데이터 가져오기"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, password, name, member_id FROM Member")
    members_data_from_db = cursor.fetchall()
    return members_data_from_db

def distinguish_user(input_id):
    """사용자 유형 구분하기"""
    if "user" in input_id:
        return "user"
    elif "staff" in input_id:
        return "staff"
    elif "analyst" in input_id:
        return "analyst"


