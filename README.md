# Number Properties API

## Overview
A FastAPI-based microservice that provides mathematical properties for a given number.

## Features
- Determine if a number is prime
- Identify Armstrong numbers
- Calculate digit sum
- Retrieve fun mathematical facts
- CORS support

## Setup
1. Clone the repository
2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
uvicorn app.main:app --reload
```

## Deployment
Deployed on Render: [Render Deployment URL]

## API Endpoint
`GET /api/classify-number?number=371`

### Response Example
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number..."
}
```

## Technologies
- Python
- FastAPI
- Uvicorn
- Requests

## License
MIT License