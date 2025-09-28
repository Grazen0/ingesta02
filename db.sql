DROP TABLE IF EXISTS students;

CREATE TABLE students (
  id INT PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  score INT NOT NULL
);

INSERT INTO
  students (id, first_name, last_name, score)
VALUES
  (1, 'Juan', 'Perez', 18),
  (2, 'Martin', 'Gomez', 13),
  (4, 'Felipe', 'Chavez', 12),
  (5, 'Carlos', 'Sanchez', 7),
  (6, 'Diego', 'Acevedo', 20);
