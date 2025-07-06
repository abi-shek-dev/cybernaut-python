import re

text = "Please contact us at abishekinterspace@gmail.com, wukongabish@gmail.com, or abishek2006me@gmail.com."

emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails)
