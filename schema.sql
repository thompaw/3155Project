DROP DATABASE IF EXISTS Project;
CREATE DATABASE Project;
USE Project;

CREATE TABLE user_profile(
    user_id int NOT NULL AUTO_INCREMENT, 
    [name] varchar(30), 
    [password] varchar(30), 
    email varchar(50), 
    PRIMARY KEY (user_id)
);

CREATE TABLE comment(
    comment_id int NOT NULL AUTO_INCREMENT, 
    user_id int NOT NULL, 
    post_id int NOT NULL, 
    content varchar(255) NOT NULL, 
    PRIMARY KEY (comment_id),
    FOREIGN KEY (user_id) REFERENCES user_profile(user_id)
    /* add foreign key for referencing post */
);

CREATE TABLE post(

);