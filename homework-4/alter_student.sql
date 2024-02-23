-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student
(
   student_id serial,
   first_name varchar,
   last_name varchar,
   birthday date,
   phone varchar,


   CONSTRAINT pk_student_student_id PRIMARY KEY(student_id)
);


-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student ADD COLUMN middle_name varchar;


-- 3. Удалить колонку middle_name
ALTER TABLE student DROP COLUMN middle_name;


-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student RENAME birthday TO birth_date;


-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student ALTER COLUMN phone SET DATA TYPE varchar(32);


-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (first_name, last_name, birth_date, phone) VALUES
('Alice', 'Jenkins', '2000-05-15', '+143265891245'),
('David', 'Murray', '1998-07-01', '+143215676254'),
('Marry', 'Pitchers', '2001-12-03', '+143212345755');

SELECT * FROM student;


-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE student RESTART IDENTITY;
