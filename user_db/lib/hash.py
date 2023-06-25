import bcrypt


# function for validation password

def generate_password_hash(password: str, ) -> str:
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(bytes(password), salt).decode()


def check_password_hash(pwd_hash, password):
    return bcrypt.hashpw(bytes(password), pwd_hash)
