-- Create the database
CREATE DATABASE legal_chatbot;

-- Use the database
USE legal_chatbot;

CREATE TABLE chat_session (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    session_id INT,
    start_time DATETIME,
    questions_answers JSON
);


CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

-- Grant permissions to the database
GRANT ALL PRIVILEGES ON legal_chatbot.* TO 'username'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

ALTER TABLE chat_sessions
ADD COLUMN password VARCHAR(255);


SELECT * FROM chat_session;