from datetime import datetime


class Email:
    """
    Represents an email message with metadata and content.

    Emails are comparable based on their `date` attribute.

    Attributes:
        sender (str): Email address of the sender.
        recipient (str): Email address of the recipient.
        subject (str): Subject line of the email.
        body (str): Body text of the email.
        date (datetime): Date and time the email was sent.

    Methods:
        __lt__(other): Compare emails by date (older than).
        __le__(other): Compare emails by date (older or equal).
        __gt__(other): Compare emails by date (newer than).
        __ge__(other): Compare emails by date (newer or equal).
        __eq__(other): Check equality based on date.
        __str__(): Return a formatted string representation.
        __len__(): Return length of email body.
        __bool__(): Return True if email body contains non-whitespace text.
    """
    def __init__(
            self,
            sender,
            recipient,
            subject,
            body,
            date
    ):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __lt__(self, other):
        return self.date < other.date

    def __le__(self, other):
        return self.date <= other.date

    def __gt__(self, other):
        return self.date > other.date

    def __ge__(self, other):
        return self.date >= other.date

    def __eq__(self, other):
        return self.date == other.date

    def __str__(self):
        return (
            f"From: {self.sender}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"- {self.body} -"
        )

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        return bool(self.body and self.body.strip())


e1 = Email(
    "alice@example.com",
    "bob@example.com",
    "Meeting",
    "Let's meet at 10am",
    datetime(2024, 6, 10)
)
e2 = Email(
    "bob@example.com",
    "alice@example.com",
    "Report",
    "",
    datetime(2024, 6, 11)
)

print(e1)
print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)


class Money:
    """
    Represents a simple monetary value.

    This class supports basic arithmetic operations between Money objects.

    Attributes:
        amount (int | float): The stored monetary value.

    Methods:
        __add__(other): Add two Money objects.
        __sub__(other): Subtract one Money object from another (clamped at 0).
        __str__(): Return a user-friendly currency string.
        __repr__(): Return a developer-friendly representation.
    """
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        result = self.amount - other.amount
        if result < 0:
            result = 0
        return Money(result)

    def __str__(self):
        return f"${self.amount}"

    def __repr__(self):
        return f"Money({self.amount})"


money1 = Money(100)
money2 = Money(50)
print(money1 + money2)
print(money1 + money2)
print(money1 - money2)
print(money2 - money1)

