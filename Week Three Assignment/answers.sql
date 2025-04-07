
-- Question 1: Create the 'student' table with three columns
CREATE TABLE student (
    id INT PRIMARY KEY,           -- The 'id' column is an integer and the primary key
    fullName TEXT(100),           -- The 'fullName' column is a text field with a maximum of 100 characters
    age INT                       -- The 'age' column is an integer
);

-- Question 2: Insert 3 records into the 'student' table
INSERT INTO student (id, fullName, age)
VALUES
    (1, 'Alice Johnson', 22),    -- Record 1: Alice Johnson, Age 22
    (2, 'Bob Smith', 19),        -- Record 2: Bob Smith, Age 19
    (3, 'Charlie Brown', 21);    -- Record 3: Charlie Brown, Age 21

-- Question 3: Update the age of the student with ID 2 to 20
UPDATE student
SET age = 20                    -- Setting the age to 20
WHERE id = 2;                   -- Targeting the student with ID 2
