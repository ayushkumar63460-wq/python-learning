text = input("Enter your comment:").lower()

if ("make a lot of money" in text) or ("buy now" in text) or ("subscribe this" in text) or ("click this" in text):
    print("SPAM Detected!")
else:
    print("No spam Detected.")