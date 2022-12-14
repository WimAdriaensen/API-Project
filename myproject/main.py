from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Union  # Dit moet ik gebruiken omdat ik anders de "None | None" niet kan gebruiken
                                # Deze wordt vervangen door "Union[str, None] = None"
import requests
from fastapi.middleware.cors import CORSMiddleware


class Course(BaseModel):
    id: int
    name_course: str
    lecturer: str
    it_class: str


app = FastAPI()

origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/",
    "https://wimadriaensen.github.io",
    "http://localhost:63343"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

course_api = {
    "id": 1,
    "name_course": "API Development",
    "lecturer": "Michiel Verboven",
    "it_class": "CCS"
}

course_iot = {
    "id": 2,
    "name_course": "IoT Advanced",
    "lecturer": "Stef Van Wolputte",
    "it_class": "CCS"
}

course_mysql = {
    "id": 3,
    "name_course": "MySQL",
    "lecturer": "Brent Pulmans",
    "it_class": "APP"
}

course_webdesign = {
    "id": 4,
    "name_course": "Webdesign Advanced",
    "lecturer": "Maartje Eyskens",
    "it_class": "APP"
}

course_bigdata = {
    "id": 5,
    "name_course": "Big Data",
    "lecturer": "Bart Portier",
    "it_class": "AI"
}

course_datasience = {
    "id": 6,
    "name_course": "Data Sience",
    "lecturer": "Bart Portier",
    "it_class": "AI"
}

courses_dict = {}
courses_list = []

courses_list.append(course_api)
courses_list.append(course_iot)
courses_list.append(course_mysql)
courses_list.append(course_webdesign)
courses_list.append(course_bigdata)
courses_list.append(course_datasience)
courses_dict = courses_list


@app.get("/courses")
async def show_courses():
    return courses_dict


@app.get("/courses/{it_class}")
async def get_courses(it_class: str):
    hulp_list = []
    for course in courses_dict:
        if course["it_class"] == it_class.upper():
            hulp_list.append(course)
    get_dict = hulp_list
    return get_dict


# Optie voor een extra GET? --> https://api.github.com/repos/wimadriaensen/wimadriaensen.github.io
# bv. url van mijn github ophalen
@app.get("/maker")
async def show_maker():
    response = requests.get("https://api.github.com/repos/wimadriaensen/API-Project")
    response_dict = {}
    response_dict["owner"] = response.json()["owner"]["login"]
    response_dict["github"] = response.json()["owner"]["html_url"]
    response_dict["repository"] = response.json()["html_url"]
    return response_dict


@app.post("/courses", response_model=Course)
async def create_course(course: Course):
    new_course = course.dict()
    courses_list.append(new_course)
    # print(courses_list)
    courses_dict = courses_list
    return course
