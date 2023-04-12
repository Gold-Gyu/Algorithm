CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTERGER NOT NULL
);

SELECT * FROM users;

-- 이름과 나이 컬럼만 조회하기
SELECT first_name, age from users;


SELECT rowid, first_name FROM users;

-- 이름과 나이를 나이가 어린 순서대로 조회
SELECT first_name, age FROM users ORDER BY age DESC;

--이름, 나이, 잔고를 나이가 작은 순서로, 
SELECT first_name, age, balance FROM users
ORDER BY age, balance DESC;

-- 모든 지역을 조회해본다.
-- 결과에서 중복을 제거하는 방법 : DISTINCT
SELECT DISTINCT country FROM users ORDER BY country;

-- 조회 칼럼이 2개 이상인 경우 : 두 컬럼을 하나의 집합으로 보고 중복을 제거함
SELECT DISTINCT first_name, country From users;

SELECT DISTINCT first_name, country
From users
ORDER BY country;

SELECT first_name, age, balance
FROM users
WHERE age >= 30 AND balance > 500000;


-- 몇개만 짤라서 보고 싶다면 limit
SELECT first_name, age, balance
FROM users
ORDER BY age
LIMIT 10
OFFSET 10;

