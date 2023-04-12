
CREATE TABLE users2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT,
    balance INTEGER NOT NULL
);


INSERT INTO users2 (first_name, last_name, age, country, phone, balance)
VALUES
('미현', '김', 19, '경기도', '011-211-8482', 300),
('', '최', 33, '제주특별자치도', '', 300),
('미숙', '이', 21, '서울특별시', '010-2122-4958', 480),
('남석', '박', 18, '경기도', '011-484-8667', 260),
('철수', '박', 22, '경상남도', '016-295-8989', 500),
('', '박', 45, '전라북도', '', 320),
('민준', '이', 35, '전라남도', '019-965-8833', 350),
('', '남', 24, '충청남도', '010-5882-5969', 210),
('신', '유', 29, '경상북도', '010-4949-2848', 290),
('', '김', 18, '대전광역시', '', 300);



select * FROM hotels
WHERE grade = "deluxe" OR room_num LIKE "B%";


UPDATE users2
SET balance = "450"
WHERE first_name = "민준";

SELECT id, age, balance FROM users2
WHERE age < 25
ORDER BY age DESC, balance;

SELECT first_name, balance FROM users2
WHERE first_name IS NOT NULL and balance > 400;

UPDATE users2
SET phone = "알 수 없음"
WHERE phone = "";