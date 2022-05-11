DROP DATABASE IF EXISTS Project;
CREATE DATABASE Project;
USE Project;  /* This is our database name */


CREATE TABLE userprofile( /* Table for the user's profile, contains their id, name, password, and email*/
    user_id int NOT NULL AUTO_INCREMENT, 
    user_name varchar(255) NOT NULL UNIQUE, /* name and pass are blocked due to being sql keywords, they still work fine but need the brackets */
    user_password varchar(255) NOT NULL, 
    user_email varchar(255) NOT NULL UNIQUE, 
    user_biography varchar(255),
    user_location varchar(255),
    PRIMARY KEY (user_id)
);

CREATE TABLE song( /* song table, holds the id as well as title and artist information. */
    song_id int NOT NULL AUTO_INCREMENT, 
    artist varchar(255) NOT NULL,
    song_name varchar(255) NOT NULL,
    PRIMARY KEY (song_id)
);

CREATE TABLE post( /* post table, keeps the id, user id, caption, and song id*/
    post_id int NOT NULL AUTO_INCREMENT, 
    user_id int NOT NULL, 
    title varchar(255) NOT NULL,
    caption varchar(255) NOT NULL,
    song_name varchar(255) NOT NULL,
    song_artists varchar(255) NOT NULL,
    song_link varchar(255) NOT NULL,
    song_image varchar(255) NOT NULL,
    PRIMARY KEY(post_id),
    FOREIGN KEY (user_id) REFERENCES userprofile(user_id)
);

CREATE TABLE comment( /* comment table, keeps comment id, user id, post id, and the conent of the comment */
    comment_id int NOT NULL AUTO_INCREMENT, 
    user_id int NOT NULL, 
    post_id int NOT NULL, 
    content varchar(255) NOT NULL, 
    PRIMARY KEY (comment_id),
    FOREIGN KEY (user_id) REFERENCES userprofile(user_id),
    FOREIGN KEY (post_id) REFERENCES post(post_id)
);

/* JUNCTION TABLE */
CREATE TABLE follower ( /* Table for determining followers, used to track who follows who. */
    follower_id int NOT NULL, 
    following_id int NOT NULL,
    FOREIGN KEY (follower_id) REFERENCES userprofile(user_id),
    PRIMARY KEY (follower_id, following_id), /* composite primary key*/
    FOREIGN KEY (following_id) REFERENCES userprofile(user_id)
);