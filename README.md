# Number Classifier API

## Overview
A FastAPI-based microservice that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Features
- Determine if a number is prime
- Identify Armstrong numbers
- Calculate digit sum
- Retrieve fun mathematical facts
- CORS support

# Project Structure

![image](https://github.com/user-attachments/assets/a87e7733-240b-48ad-b2f0-0d784f8fbe4e)


# Create project directory
```bash
mkdir num-classifier
cd num-classifier
mkdir app
```

# Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
###### Windows: venv\Scripts\activate
###### Mac/Linux: source venv/bin/activate

# Install dependencies
```bash
pip install fastapi uvicorn requests python-dotenv
pip freeze > requirements.txt
```

##### Next, create files number_utils.py and main.py in app/ directory

##### Afterwards, create Dockerfile in main directory num-classifier


### Deployment Steps:

1. Create a GitHub repository
2. Push all files to the repository
```bash
git init     # Initialize git repository
git add .    # Add all files
git commit -m "Initial commit: Number Properties API"    # Commit files
git branch -M main    # Create main branch (if not already created)
git remote add origin repo-link     #replace with your actual repository URL
git push -u origin main    # Push to main branch
```

3. Deploy on Render:

##### Connect GitHub repository
##### Set build command: pip install -r requirements.txt
##### Set start command: uvicorn app.main:app --host 0.0.0.0 --port $PORT

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

This project is open-source and available under the MIT License.
