# Text Embeddings API

This is a simple FastAPI application that generates text embeddings using the `all-MiniLM-L6-v2` model from the `sentence-transformers` library.

## Features
- **POST /embeddings**: Accepts a text input and returns its embeddings as a list.
- **GET /**: Returns a welcome message with basic API information.

## Prerequisites
- Python 3.8+
- FastAPI
- Pydantic
- Sentence Transformers
- NumPy

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn sentence-transformers numpy
   ```

## Usage
1. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The server will start at `http://127.0.0.1:8000`.

2. Access the API:
   - **GET Welcome Message**:
     ```bash
     curl http://127.0.0.1:8000/
     ```
     Response:
     ```json
     {"message": "Welcome to the Text Embeddings API. Use POST /embeddings to get embeddings."}
     ```

   - **POST Text Embeddings**:
     ```bash
     curl -X POST http://127.0.0.1:8000/embeddings -H "Content-Type: application/json" -d '{"text": "This is a sample text"}'
     ```
     Response:
     ```json
     {"embeddings": [0.12, -0.34, ..., 0.56]}
     ```

3. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Code Structure
- **main.py**: Contains the FastAPI application with two endpoints:
  - `GET /`: Returns a welcome message.
  - `POST /embeddings`: Takes a text input and returns its embeddings.
- **Model**: Uses `all-MiniLM-L6-v2` from `sentence-transformers` to generate embeddings.
- **Input Validation**: Uses Pydantic's `BaseModel` to validate incoming text input.

## Error Handling
- If an error occurs during embedding generation, the API returns a 500 status code with a detailed error message.
