[1mdiff --git a/.env.sample b/.env.sample[m
[1mindex 0bfb8ff..baa44b3 100644[m
[1m--- a/.env.sample[m
[1m+++ b/.env.sample[m
[36m@@ -1,2 +1,3 @@[m
 PASS=<make copy of file without the .sample in the name, and replace this text with your sql passowrd>[m
[31m-SECRET_KEY=mysecretekey[m
\ No newline at end of file[m
[32m+[m[32mSECRET_KEY=mysecretekey[m
[32m+[m[32mCLEARDB_DATABASE_URL=mysql://username:password@localhost:3306/Project[m
\ No newline at end of file[m
[1mdiff --git a/app.py b/app.py[m
[1mindex db6e1a3..af37e45 100644[m
[1m--- a/app.py[m
[1m+++ b/app.py[m
[36m@@ -26,7 +26,7 @@[m [mengine = sqlalchemy.engine.URL.create(   #This is just the URI but separated. It[m
     port = "3306",[m
     database="Project"[m
 )[m
[31m-app.config['SQLALCHEMY_DATABASE_URI'] = engine[m
[32m+[m[32mapp.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CLEARDB_DATABASE_URL')[m
 app.config['SQLALCHEMY_TRACK_MODRIFICATIONS'] = False[m
 app.secret_key = os.getenv('SECRET_KEY')[m
 [m
