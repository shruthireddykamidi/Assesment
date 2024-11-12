import os
from flask import Flask, request, jsonify
import requests
import openai

# === Configuration ===

# Load your API keys from environment variables
DAPPIER_API_KEY = os.getenv('DAPPIER_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Ensure API keys are set
if not DAPPIER_API_KEY or not OPENAI_API_KEY:
    raise Exception("Please set the DAPPIER_API_KEY and OPENAI_API_KEY environment variables.")

# OpenAI API Configuration
openai.api_key = OPENAI_API_KEY

# Dappier API Endpoint
DAPPIER_API_URL = 'https://api.dappier.com/app/datamodel/dm_01hpsxyfm2fwdt2zet9cg6fdxt'

# Headers for Dappier API
dappier_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {DAPPIER_API_KEY}'
}

# Initialize Flask app
app = Flask(__name__)

# === Function Definitions ===

def fetch_dappier_data(query):
    """
    Fetch data from Dappier API based on the provided query.

    :param query: The query string to send to the Dappier API.
    :return: The response from the Dappier API as a string.
    """
    payload = {
        "query": query
    }

    try:
        response = requests.post(DAPPIER_API_URL, headers=dappier_headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("message", "")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurre
