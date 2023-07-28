import uvicorn
from fastapi import FastAPI
from routers import posts, users, auth, vote
from fastapi.middleware.cors import CORSMiddleware

#If we have existing table, command will not run
#Only create table name if it doesn't exist
#models.Base.metadata.create_all(bind=engine) -> When you use alembic, you dont have to use this command

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(vote.router)
app.include_router(auth.router)



@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}
