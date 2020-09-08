#!/bin/zsh

# app = FastAPI()
# --reload: make the server restart after code changes. Only use for development.
poetry run uvicorn main:app --reload