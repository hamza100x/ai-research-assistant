# Use Python 3.13
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose the port
EXPOSE 7860

# Run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "7860"]