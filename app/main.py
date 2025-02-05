# app/main.py
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .number_utils import (
    is_prime, 
    is_armstrong_number, 
    get_digit_sum, 
    get_fun_fact
)

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., min_length=1)):
    try:
        # Convert and validate input
        n = int(number)
        
        # Determine properties
        properties = []
        if n % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
        
        # Add Armstrong number if applicable
        if is_armstrong_number(n):
            properties.append("armstrong")
        
        # Construct response
        return {
            "number": n,
            "is_prime": is_prime(n),
            "is_perfect": False,  # Not implemented in this version
            "properties": properties,
            "digit_sum": get_digit_sum(n),
            "fun_fact": get_fun_fact(n)
        }
    except ValueError:
        # Handle invalid input
        raise HTTPException(status_code=400, detail={
            "number": number,
            "error": True
        })

# Run with: uvicorn app.main:app --reload
