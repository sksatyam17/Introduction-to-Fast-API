from fastapi import FastAPI, status, HTTPException
import uuid
from models import User

app = FastAPI()

users = {
    "1": {
        "name": "John",
        "age": 20
    },
    "2": {
        "name": "Jane",
        "age": 21
    }
}

@app.get("/users")
def users_list():
    return users

@app.get("/users/{user_id}")
def user_details(user_id: str):
    if user_id in users:
        return users[user_id]
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.post("/users", status_code=status.HTTP_201_CREATED)
def user_add(user: User):
    user_id = str(uuid.uuid4())
    users[user_id] = user.dict()  # Convert User model to dictionary
    return {user_id: users[user_id]}  # Return the new user details

@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def user_update(user_id: str, user: User):
    if user_id in users:
        users[user_id] = user.dict()  # Convert User model to dictionary
        return "User updated"
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def user_delete(user_id: str):
    if user_id in users:
        del users[user_id]
        return "User deleted"
    else:
        raise HTTPException(status_code=404, detail="User not found")
