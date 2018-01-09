import re
import zipfile

pattern = re.compile("Next nothing is (\d+)")

num = "90052"
comments = []

file = zipfile.ZipFile("channel.zip")

while True:
    content = file.read(num + ".txt").decode("utf-8")
    comments.append(file.getinfo(num + ".txt").comment.decode("utf-8"))
    print(content)
    match = re.search(pattern, content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))
