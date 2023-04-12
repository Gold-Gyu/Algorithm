-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- 행의 계수 집계
SELECT COUNT(*) FROM users;

-- 평균 집계
SELECT avg(balance) FROM users;

-- 지역별 평균 집계
-- 1. 전체 조회 방법
SELECT DISTINCT country, avg(balance) FROM users
GROUP BY country
ORDER BY avg(balance) DESC;

-- 나이가 30살 이상인 사람들의 평균나이
SELECT avg(age) FROM users
WHERE age >= 30;

-- 각 지역별로 몇명씩 살고 있는가
SELECT country, count(*) FROM users
GROUP BY country;

-- 각각의 성씨가 몇 몇씩 있는지 조회
SELECT last_name, count(last_name) FROM users
GROUP BY last_name;

CREATE TABLE classmates(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
    );

INSERT INTO classmates (name, age, address)
VALUES("홍길동", 23, "서울");

INSERT INTO classmates
VALUES
("김진수", 30, "경기"),
("이영미", 31, "강원"),
("박진성", 26, "전라"),
("최지수", 12, "충청"),
("정요한", 28, "경상");

UPDATE classmates
SET name="김철수한무두루미",
    address="제주도"
-- 두번쨰 줄
WHERE rowid=2;

DELETE FROM classmates
WHERE rowid=5;

-- 이름에 "영"이 포함되어있는 데이터 삭제하기
DELETE FROM classmates
WHERE name LIKE "%영%";

-- 테이블의 모든 데이터 삭제하기
DELETE FROM classmates;



