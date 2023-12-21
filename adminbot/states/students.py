from aiogram.dispatcher.filters.state import StatesGroup, State


class StudentsStates(StatesGroup):
    initial = State()
    enter_student_username = State()
    enter_teacher_name = State()
    enter_course_name = State()
    enter_date = State()
    enter_time = State()
    enter_task = State()