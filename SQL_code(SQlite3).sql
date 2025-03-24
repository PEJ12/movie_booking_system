
CREATE TABLE Theater (
    theater_id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_seat INTEGER CHECK (total_seat > 0)
);

CREATE TABLE Seat (
    seat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    theater_id INTEGER,
    seat_assignment BOOLEAN NOT NULL,
    screening_date_id INTEGER,
    FOREIGN KEY (theater_id) REFERENCES Theater(theater_id),
    FOREIGN KEY (screening_date_id) REFERENCES ScreeningSchedule(screening_date_id)
);

CREATE TABLE Movie (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_title VARCHAR(50) NOT NULL,
    summary TEXT,
    actor VARCHAR(30),
    director VARCHAR(30),
    CONSTRAINT unique_movie_title UNIQUE (movie_title)
);

CREATE TABLE ScreeningSchedule (
    screening_date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    screening_date DATE,
    movie_id INTEGER,
    theater_id INTEGER,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (theater_id) REFERENCES Theater(theater_id)
);

CREATE TABLE Member (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    id VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(30) UNIQUE NOT NULL,
    name VARCHAR(30) NOT NULL,
    phone_number CHAR(11)
);

CREATE TABLE Review (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rating INTEGER CHECK (((rating >= 0) AND (rating <= 5))), 
    movie_id INTEGER,
    member_id INTEGER,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Reservation (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    price INTEGER,
    pay_method VARCHAR(30) NOT NULL,
    screening_date_id INTEGER,
    theater_id INTEGER,
    seat_id INTEGER,
    movie_id INTEGER,
    member_id INTEGER,
    FOREIGN KEY (screening_date_id) REFERENCES ScreeningSchedule(screening_date_id),
    FOREIGN KEY (theater_id) REFERENCES Theater(theater_id),
    FOREIGN KEY (seat_id, theater_id) REFERENCES Seat(seat_id, theater_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

INSERT INTO Theater (total_seat) VALUES (10);
INSERT INTO Theater (total_seat) VALUES (15);

INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (1, 1, true, 27);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (2, 1, true, 27);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (3, 1, true, 27);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (4, 1, true, 27);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (5, 1, true, 27);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (6, 1, true, 27);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (7, 1, true, 27);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (8, 1, true, 27);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (9, 1, true, 27);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (10, 1, true, 27);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (11, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (12, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (13, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (14, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (15, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (16, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (17, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (18, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (19, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (20, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (21, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (22, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (23, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (24, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (25, 2, true, 28);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (26, 1, true, 29);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (27, 1, true, 29);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (28, 1, true, 29);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (29, 1, true, 29);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (30, 1, true, 29);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (31, 1, true, 29);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (32, 1, true, 29);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (33, 1, true, 29);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (34, 1, true, 29);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (35, 1, true, 29);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (36, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (37, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (38, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (39, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (40, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (41, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (42, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (43, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (44, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (45, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (46, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (47, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (48, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (49, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (50, 2, true, 30);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (51, 1, true, 31);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (52, 1, true, 31);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (53, 1, true, 31);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (54, 1, true, 31);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (55, 1, true, 31);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (56, 1, true, 31);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (57, 1, true, 31);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (58, 1, true, 31);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (59, 1, true, 31);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (60, 1, true, 31);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (61, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (62, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (63, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (64, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (65, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (66, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (67, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (68, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (69, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (70, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (71, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (72, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (73, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (74, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (75, 2, true, 32);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (76, 1, false, 33);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (77, 1, false, 33);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (78, 1, false, 33);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (79, 1, false, 33);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (80, 1, false, 33);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (81, 2, false, 34);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (82, 2, false, 34);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (83, 2, false, 34);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (84, 2, false, 34);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (85, 2, false, 34);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (86, 1, false, 35);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (87, 1, false, 35);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (88, 1, false, 35);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (89, 1, false, 35);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (90, 1, false, 35);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (91, 1, false, 36);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (92, 1, false, 36);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (93, 1, false, 36);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (94, 2, false, 37);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (95, 2, false, 37);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (96, 2, false, 37);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (97, 1, false, 38);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (98, 1, false, 38);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (99, 1, false, 38);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (100, 1, false, 39);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (101, 1, false, 39);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (102, 1, false, 40);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (103, 1, false, 40);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (104, 2, false, 41);
INSERT INTO Seat (seat_id, theater_id, seat_assignment, screening_date_id) VALUES (105, 2, false, 41);

INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('Inception', 'A mind-bending thriller', 'Leonardo DiCaprio', 'Christopher Nolan');
INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('The Shawshank Redemption', 'A tale of hope and perseverance', 'Tim Robbins', 'Frank Darabont');
INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('Pulp Fiction', 'A Quentin Tarantino classic', 'John Travolta', 'Quentin Tarantino');
INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('The Matrix', 'Welcome to the real world', 'Keanu Reeves', 'Lana Wachowski');
INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('Forrest Gump', 'Life is like a box of chocolates', 'Tom Hanks', 'Robert Zemeckis');
INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('Eternal Sunshine of the Spotless Mind', 'Love, memories, and second chances', 'Jim Carrey', 'Michel Gondry');
INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('John Wick', 'Retired assassin seeks vengeance', 'Keanu Reeves', 'Chad Stahelski');
INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('Speed', 'A bomb on a bus with no brakes', 'Keanu Reeves', 'Jan de Bont');
INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('Cast Away', 'Survival on a deserted island', 'Tom Hanks', 'Robert Zemeckis');
INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('Saving Private Ryan', 'A mission to save a soldier', 'Tom Hanks', 'Steven Spielberg');
INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('The Truman Show', 'Living a scripted life', 'Jim Carrey', 'Peter Weir');
INSERT INTO Movie (movie_title, summary, actor, director) VALUES ('The Mask', 'Mild mannered banker with a magical mask', 'Jim Carrey', 'Charles Russell');

INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-12-23', 1, 1);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-12-24', 1, 2);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-12-25', 2, 1);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-12-26', 2, 2);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-12-27', 3, 1);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-12-28', 3, 2);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-9-20', 4, 1);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-9-24', 5, 2);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-10-25', 6, 1);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-10-27', 7, 2);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-11-11', 8, 2);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-11-15', 9, 1);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-11-16', 10, 1);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-11-18', 11, 1);
INSERT INTO ScreeningSchedule (screening_date, movie_id, theater_id) VALUES ('2025-11-20', 12, 2);

INSERT INTO Member (id, password, name, phone_number) VALUES ('user1', 'pass1', 'John', '01045678902');
INSERT INTO Member (id, password, name, phone_number) VALUES ('user2', 'pass2', 'Jane', '01065423210');
INSERT INTO Member (id, password, name, phone_number) VALUES ('user3', 'pass3', 'Smith', '01011116666');
INSERT INTO Member (id, password, name, phone_number) VALUES ('user4', 'pass4', 'Danny', '01099991111');
INSERT INTO Member (id, password, name, phone_number) VALUES ('user5', 'pass5', 'Jenny', '01088884444');
INSERT INTO Member (id, password, name, phone_number) VALUES ('staff1', 'pass6', 'Tom', '01023455555');
INSERT INTO Member (id, password, name, phone_number) VALUES ('staff2', 'pass7', 'Jerry', '01022223333');
INSERT INTO Member (id, password, name, phone_number) VALUES ('analyst1', 'pass8', 'Eun Jae', '01012344567');

INSERT INTO Review (rating, movie_id, member_id) VALUES (4, 4, 1);
INSERT INTO Review (rating, movie_id, member_id) VALUES (5, 4, 2);
INSERT INTO Review (rating, movie_id, member_id) VALUES (5, 4, 3);
INSERT INTO Review (rating, movie_id, member_id) VALUES (2, 5, 1);
INSERT INTO Review (rating, movie_id, member_id) VALUES (3, 5, 2); 
INSERT INTO Review (rating, movie_id, member_id) VALUES (1, 5, 3);
INSERT INTO Review (rating, movie_id, member_id) VALUES (2, 5, 4);
INSERT INTO Review (rating, movie_id, member_id) VALUES (3, 5, 5);
INSERT INTO Review (rating, movie_id, member_id) VALUES (3, 6, 1);
INSERT INTO Review (rating, movie_id, member_id) VALUES (3, 6, 2);
INSERT INTO Review (rating, movie_id, member_id) VALUES (2, 6, 3);
INSERT INTO Review (rating, movie_id, member_id) VALUES (4, 6, 4); 
INSERT INTO Review (rating, movie_id, member_id) VALUES (3, 6, 5); 
INSERT INTO Review (rating, movie_id, member_id) VALUES (3, 7, 1);
INSERT INTO Review (rating, movie_id, member_id) VALUES (2, 7, 2);
INSERT INTO Review (rating, movie_id, member_id) VALUES (3, 7, 3);
INSERT INTO Review (rating, movie_id, member_id) VALUES (1, 8, 4);
INSERT INTO Review (rating, movie_id, member_id) VALUES (2, 8, 5);
INSERT INTO Review (rating, movie_id, member_id) VALUES (1, 8, 1);
INSERT INTO Review (rating, movie_id, member_id) VALUES (3, 9, 2);
INSERT INTO Review (rating, movie_id, member_id) VALUES (5, 9, 3);
INSERT INTO Review (rating, movie_id, member_id) VALUES (2, 9, 4);
INSERT INTO Review (rating, movie_id, member_id) VALUES (1, 10, 5);
INSERT INTO Review (rating, movie_id, member_id) VALUES (5, 10, 1);
INSERT INTO Review (rating, movie_id, member_id) VALUES (3, 11, 2);
INSERT INTO Review (rating, movie_id, member_id) VALUES (2,11, 3); 
INSERT INTO Review (rating, movie_id, member_id) VALUES (4,12, 4); 
INSERT INTO Review (rating, movie_id, member_id) VALUES (3, 12, 5);

INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Credit Card', 33, 1, 76, 4, 1);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Debit Card', 33, 1, 77, 4, 2);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 33, 1, 78, 4, 3);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Credit Card', 33, 1, 79, 4, 4);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Credit Card', 33, 1, 80, 4, 5);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Credit Card', 34, 2, 81, 5, 1);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Debit Card', 34, 2, 82, 5, 2);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 34, 2, 83, 5, 3);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 34, 2, 84, 5, 4);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Debit Card', 34, 2, 85, 5, 5);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Debit Card', 35, 1, 86, 6, 1);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Credit Card', 35, 1, 87, 6, 2);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 35, 1, 88, 6, 3);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 35, 1, 89, 6, 4); 
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Credit Card', 35, 1, 90, 6, 5);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Debit Card', 36, 1, 91, 7, 1);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Credit Card', 36, 1, 92, 7, 2);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 36, 1, 93, 7, 3);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 37, 2, 94, 8, 4); 
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Credit Card', 37, 2, 95, 8, 5);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 37, 2, 96, 8, 1);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Debit Card', 38, 1, 97, 9, 2);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Credit Card', 38, 1, 98, 9, 3);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 38, 1, 99, 9, 4); 
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Credit Card', 39, 1, 100, 10, 5);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 39, 1, 101, 10, 1); 
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Debit Card', 40, 1, 102, 11, 2); 
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 40, 1, 103, 11, 3);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 41, 2, 104, 12, 4);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Credit Card', 41, 2, 105, 12, 5); 
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 32, 2, 75, 3, 1);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Debit Card', 31, 1, 60, 3, 1);
INSERT INTO Reservation (price, pay_method, screening_date_id, theater_id, seat_id, movie_id, member_id) VALUES (8000, 'Cash', 27, 1, 1, 1, 1);
