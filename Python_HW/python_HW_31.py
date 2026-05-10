import re


# task 1

text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022"

pattern = r"\b\d{2}[\/\-.]\d{2}[\/\-.]\d{4}\b"
dates = re.findall(pattern, text)

print(dates)


# task 2

tag_input = "python, data-science / machine-learning; AI neural-networks"

tags = re.split(r"[,\s;/]+", tag_input)
print(tags)

