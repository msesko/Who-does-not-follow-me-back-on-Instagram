import re


if __name__ == "__main__":
    with open("following.html", "r", encoding="utf-8") as file:
        a = file.read()

    with open("followers_1.html", "r", encoding="utf-8") as file:
        b = file.read()

    pattern = r"https://www\.instagram\.com/([a-zA-Z0-9._]+)"

    following = re.findall(pattern, a)
    followers = re.findall(pattern, b)

    for acc in following:
        if acc not in followers:
            print(acc)
