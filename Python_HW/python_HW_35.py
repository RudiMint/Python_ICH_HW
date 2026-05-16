class User:
    """
    Represents a system user with login credentials.

    Attributes:
        total_users (int): Class-level counter tracking how many users
            have been created.
        login (str): User login name.
        password (str): User password.
    """
    total_users = 0

    def __init__(self, login, password):
        """
        Initialize a new User instance.

        Args:
            login (str): The user's login name.
            password (str): The user's password.

        Raises:
            ValueError: If login or password validation fails.
        """
        self.validate_login(login)
        self.validate_password(password)

        self.login = login
        self.password = password

        User.total_users += 1

    @staticmethod
    def validate_login(login):
        """
        Validate the login value.
        Args:
            login (str): Login string to validate.
        Raises:
            ValueError: If login is not a non-empty string.
        """
        if not isinstance(login, str) or not login.strip():
            raise ValueError("login must be a string. not empty")

    @staticmethod
    def validate_password(password):
        """
        Validate the password value.
        Args:
            password (str): Password string to validate.
        Raises:
            ValueError: If password is not a string
                or contains fewer than 5 characters.
        """
        if not isinstance(password, str) or len(password) < 5:
            raise ValueError("password must be a string of 5 or more symbols")

    def __str__(self):
        """
        Return a readable string representation of the user.
        Returns:
            str: Formatted user description.
        """
        return f"User(login='{self.login}')"

    @classmethod
    def get_total(cls):
        """
        Get the total number of created users.
        Returns:
            int: Number of User instances created.
        """
        return cls.total_users


print(f"total users: {User.get_total()}")

user1 = User("login1", "pass1")
user2 = User("login2", "pass2")

print(f"total users: {User.get_total()}")

print(user2)

# tests with incorrect data
tests = [
    ("", "pass123"),
    ("   ", "pass123"),
    ("user", "123"),
    (123, "password"),
]

for log, passw in tests:
    try:
        user = User(log, passw)
    except ValueError as e:
        print(f"Error: {e}")

