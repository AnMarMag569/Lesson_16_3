from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = [{
        'id': 1, 'Имя': "Example", 'возраст': 18
        }]

@app.get("/user")
async def read_users():
    return (users)
@app.post('/user/{username}/{age}')
async def post_user(
        username: Annotated[str, Path(..., min_length=5, max_length=20)],
        age: Annotated[int, Path(..., gt=18, lt=100)]):
    user_id = max(user['id'] for user in users) + 1 if users else 1
    new_user = {'id': user_id, 'Имя': username, 'возраст': age}
    users.append(new_user)
    return (f'User {user_id} is registered')

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user['id'] == user_id:
            user['Имя'] = (username)
            user['возраст'] = (age)

    return (f'User {user_id} has been updated')


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user['id'] == user_id:
            del users[i]
    return (f"User {user_id} has been deleted")



# uvicorn module_16_3:app --reload