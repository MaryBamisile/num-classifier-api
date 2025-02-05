# app/main.py
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .number_utils import (
    is_prime, 
    is_armstrong_number, 
    get_digit_sum, 
    get_fun_fact
)
import math

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/classify-number", response_class=JSONResponse)
async def classify_number(number: str = Query(..., min_length=1)):
    try:
        # Convert input, handling floats and negative numbers
        n = float(number)
        
        # Convert to integer if whole number
        n = int(n) if n.is_integer() else n
        
        # Determine properties
        properties = []
        if isinstance(n, int):
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
            "is_prime": is_prime(abs(int(n))) if isinstance(n, int) else False,
            "is_perfect": False,
            "properties": properties,
            "digit_sum": get_digit_sum(abs(int(n))) if isinstance(n, int) else sum(int(d) for d in str(abs(n)) if d.isdigit()),
            "fun_fact": get_fun_fact(abs(int(n))) if isinstance(n, int) else "No specific fun fact for non-integer numbers"
        }
    except ValueError:
        # Handle invalid input
        return JSONResponse(
            status_code=200,
            content={
                "number": number,
                "error": True,
                "message": "Invalid number format"
            }
        )
