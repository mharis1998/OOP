import functools


user={"username": "jose", "access_level": "admin"}

def make_secure(func):
## for parameters function pass *args and **kwargs
    @functools.wraps(func)
    def secure_funciton(*arg,**kwargs):
        if user["access_level"]=="admin":
            return func(*arg,**kwargs)
        else:
            return f"NO admin permission for {user['username']} "
        
    return secure_funciton


@make_secure
def get_admin_password(panel):
    return 123

print(get_admin_password(121))




user={"username": "jose", "access_level": "guest"}

def make_secure_2(access_level):
    def decorator(func):
## for parameters function pass *args and **kwargs
        @functools.wraps(func)
        def secure_funciton(*arg,**kwargs):
            if access_level=="admin":
                return func(*arg,**kwargs)
            else:
                return f"NO admin permission for {user['username']} "
        
        return secure_funciton
    return decorator

@make_secure_2("admin")
def get_admin_password():
    return 123

print(get_admin_password())

