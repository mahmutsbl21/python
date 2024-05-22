import requests
import time
import sys

def clear_screen():
    if sys.platform == "win32":
        _ = system("cls")
    else:
        _ = system("clear")

url = input("Enter the URL of the course: ")
course_id = url.split("-")[-1]

clear_screen()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Origin": "https://www.btkakademi.gov.tr",
    "Dnt": "1",
    "Referer": url,
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
    "Connection": "close"
}

json = {"demandForm": {}}

response = requests.post(
    f"https://www.btkakademi.gov.tr:443/api/service/v1/course/registration/register/{course_id}?language=tr",
    headers=headers, json=json
)

print(response.json()["status"])
time.sleep(1)
clear_screen()

headers["Authorization"] = "Bearer YOUR_AUTHORIZATION_TOKEN"

url = f"https://www.btkakademi.gov.tr:443/api/service/v1/public/51/course/details/program/syllabus/{course_id}?language=tr"

response = requests.get(url, headers=headers)

data = response.json()

for i, course in enumerate(data, start=1):
    print(f"{i}. {course['title']}")

selection = int(input("\nEnter your selection: "))

clear_screen()

for i, lesson in enumerate(data[selection-1]["courses"], start=1):
    print(f"{i}. {lesson['title']}")

selection = int(input("\nEnter your selection: "))

lesson_id = data[selection-1]["courses"][selection-1]["id"]

url = f"https://www.btkakademi.gov.tr:443/api/service/v1/course/deliver/start/{lesson_id}"

headers["Content-Type"] = "application/json"

json = {"programId": int(course_id)}

response = requests.post(url, headers=headers, json=json)

print(response.json()["remoteCourseReference"])
