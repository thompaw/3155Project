DROP DATABASE IF EXISTS Project;
CREATE DATABASE Project;
USE Project;  /* This is our database name */


CREATE TABLE user_profile(
    user_id int NOT NULL AUTO_INCREMENT, 
    [name] varchar(30), 
    [password] varchar(30), 
    email varchar(50), 
    PRIMARY KEY (user_id)
);

CREATE TABLE follower (
    follower_id int NOT NULL, 
    following_id int NOT NULL,
    PRIMARY KEY (follower_id),
    FOREIGN KEY (follower_id) REFERENCES user_profile(user_id),
    PRIMARY KEY (following_id), 
    FOREIGN KEY (following_id) REFERENCES user_profile(user_id)
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
    post_id int NOT NULL AUTO_INCREMENT, 
    user_id int NOT NULL, 
    caption varchar(255) NOT NULL,
    song_id int NOT NULL,
    PRIMARY KEY(post_id),
    FOREIGN KEY (user_id) REFERENCES user_profile(user_id),
    FOREIGN KEY (song_id) REFERENCES song(song_id)
);

CREATE TABLE post_user(
    user_id int NOT NULL, 
    post_id int NOT NULL, 
    PRIMARY KEY (user_id), 
    PRIMARY KEY (post_id), 
    FOREIGN KEY (user_id) REFERENCES user_profile(user_id), 
    FOREIGN KEY (post_id) REFERENCES post(post_id)
);

CREATE TABLE song(
    song_id int NOT NULL AUTO_INCREMENT, 
    artist varchar(255) NOT NULL,
    song_name varchar(40) NOT NULL,
    PRIMARY KEY (song_id)
);