# FastAPI Template

This is a project template for FastAPI, structured to serve as a basis for developing scalable and secure APIs. It includes an initial setup for JWT authentication, data validation with Pydantic, automatic documentation, and a modularized framework.

## Features

- **JWT Authentication**: Secure authentication for endpoint protection.
- **Data Validation**: Automatic data validation with Pydantic.
- **Automatic Documentation**: Documentation automatically generated with Swagger and Redoc.
- **Modular Structure**: Separation of routes, models, schemes and configuration for easy maintenance.
- **Database Configuration**: Connection to SQL database using SQLAlchemy.

## Project Structure

```plaintext
fast_api/
├── app/
│   ├── main.py               
│   ├── models/               
│   ├── db/                   
│   │   ├── database.py       
│   ├── schemas/             
│   ├── routers/           
│   ├── core/
│   │   ├── config.py         
│   │   └── security.py       
│   └── utils/                
├── venv
├── config/                   
│   ├── .env                  
├── .gitignore                
├── requirements.txt          
└── README.md                 
```

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Python-dotenv
- Other packages listed in `requirements.txt`

## Settings

1. Clone the repository:

   ```bash
   git clone https://github.com/IamLeonardoSouza/fast_api.git
   cd fastapi-template
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate # Linux/macOS
   venv\Scripts\activate # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the `.env` file with the necessary environment variables:

   ```plaintext
   DATABASE_URL=sqlite:///./test.db
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

## Running the Project

Start the development server:

```bash
uvicorn app.main:app --reload
```
