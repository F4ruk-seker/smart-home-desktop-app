import jwt

token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NzM0NDUyOCwiaWF0IjoxNjg3MjU4MTI4LCJqdGkiOiIxZmZhMTVjZmI3NzQ0ZGVkYTJmYzU2NjdjMTJmYmRkMyIsInVzZXJfaWQiOjF9.munnY_gkZGpLXjfgD2FXrl3HDacid4fuojCDxSMgwkg"

rem = jwt.decode(token, algorithms='HS256')

print(rem)