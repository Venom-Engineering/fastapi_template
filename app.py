from fastapi import FastAPI
from routers import subapp_1, subapp_2

description = """
A templaste api for anyone who just want the minimal requirement for deploying data 🚀

## Items

**subapp_1**: exemple of router 1 \n
**subapp_2**: exemple of router 2

## Users

* **anyone who need it**
"""

app = FastAPI(
    debug=True,
    title="API template",
    description=description,
    version="0.0.1",
    contact={
        "name": "Jonathan Ndamba",
        "email": "jonathan.ndamba.pro@gmail.com",
    },
    license_info={
        "name": "venom",
    },
)

app.include_router(subapp_1.router)
app.include_router(subapp_2.router)
