# Kaseya Phonon AI
In Quantum mechanics, at low temperature, electron and Phonon interacts with together to form Cooper Pair. Just like the phenomenon, this project is meant to interact with Cooper to form Cooper Pair.

## Installation
```bash
git clone https://github.com/ddqlpajama/KaseyaPhonon.git
cd ./KaseyaPhonon
pip install -r requirements.txt
uvicorn main:app --reload
```

## Features
- [x] Private Model, no need to upload data to external server containing private info.
- [x] Fast, no need to wait for the server to process the data.
- [x] Can arbitrarily add new category to the model.
- [x] Shows you the percentage of the prediction.

## Usage
Request
```
POST {endpoint}/classify_ticket
Accept: application/json
Content-Type: application/json

{
  "title": "I can't log in to my account",
  "description": "Another member bites the dust.",
  "candidates": ["New Member", "Terminated Member", "Problem"]
}
```

Response
```
{
  "title": "I can't log in to my account",
  "description": "Another member bites the dust.",
  "classification": {
    "Terminated Member": 0.8945837616920471,
    "Problem": 0.10309306532144547,
    "New Member": 0.0023231212981045246
  }
}
```     