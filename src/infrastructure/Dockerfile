# DESIGN EXERCISE - Not for production
FROM python:3.9-slim as design-stage

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Intentional break (per brief, no full implementation)
# CMD ["uvicorn", "app.main:app"] 