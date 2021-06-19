# Architecting Flask Project

Boilerplate code for organizing flask application using Flask Blueprint

Approach 1

```
|   main.py
|   util.py
|
+---app
|   +---auth
|   |   |   __init__.py
|   |   |
|   |   +---static
|   |   |       auth.css
|   |   |
|   |   \---template
|   |           login.html
|   |           register.html
|   |
|   \---user_post
|       |   __init__.py
|       |
|       +---static
|       |       post.css
|       |
|       \---template
|               upload_post.html
|               view_post.html
|
\---data
        auth.json
        posts.json
```

Approach 2

```
\---app
    |   main.py
    |   util.py
    |
    +---controllers
    |   |   auth.py
    |   |   user_post.py
    |   |   __init__.py
    |   
    |
    +---data
    |       auth.json
    |       posts.json
    |
    +---static
    |   +---auth
    |   |       auth.css
    |   |
    |   \---post
    |           post.css
    |
    +---templates
    |   +---auth
    |   |       login.html
    |   |       register.html
    |   |
    |   \---post
    |           upload_post.html
    |           view_post.html
  

```
