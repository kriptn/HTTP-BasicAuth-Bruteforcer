# HTTP BasicAuth Broteforcer

## Description: 

Written in python to bruteforce password of admin user in my test environment.

You can change the username, URL, HTTP Method, Password file to your hearts content.

If you have the password then you can change the variable names around after modifying the positions in the `auth(user, password=pword)` to bruteforce just usernames

If you have ssl or want to ignore ssl then add the `verify` argument when sending the request. To ignore SSL/TLS add `verify= False`

I may or may not modify this script in the future to brute force usernames in a culsterbomb manner

------

## Usage :
Edit the contents of `run.py` as mentioned in the description

```
python3 run.py
```
