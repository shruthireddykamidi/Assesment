# Good Morning App API

This repository contains a Python script for the **Good Morning App API**. The API greets the user every morning and provides the latest weather and news based on their location. It integrates **Dappier's** real-time RAG model to fetch live data and **OpenAI's ChatGPT** to generate a friendly, conversational response.

---

## Overview

The Good Morning App API performs the following steps:

1. ### Receives User Input

   Prompts the user to enter their location.

2. ### Fetches Live Data from Dappier API

   - **Weather Information**: Retrieves the current weather for the specified location.
   - **News Information**: Retrieves the latest news headlines for the same location.
   - **Purpose**: Dappier's API provides real-time data essential for creating personalized content.

3. ### Generates a Response using ChatGPT

   - **Combines** the fetched weather and news data into a prompt.
   - Uses **OpenAI's ChatGPT** to generate a playful, conversational message.
   - **Includes**:
     - A warm greeting.
     - Weather update.
     - News highlight.
     - A joke to brighten the user's day.
     - A follow-up question to encourage engagement.
   - **Purpose**: ChatGPT enhances user interaction by generating natural and engaging text.

4. ### Displays the Response

   Outputs the generated message to the user in a structured format.

---

## Usage

To run the script:

1. ### Ensure API Keys are Set

   - **Obtain** your API keys from **Dappier** and **OpenAI**.
   - **Insert** your API keys into the script where indicated:

     ```python
     openai.api_key = 'your_openai_api_key'
     DAPPIER_API_KEY = 'your_dappier_api_key'
     ```

   - **Note**: Keep your API keys secure and do not share them publicly.

2. ### Run the Script

   ```bash
   python good_morning_app.py
Enter Your Location
When prompted, input your location:

plaintext
Enter your location (e.g., "Austin, TX"):
Example Output
After entering your location, you will receive a response similar to:

Example output

{
  "Response": "Good morning! ☀️ It's a beautiful sunny day in Austin today—perfect for a morning jog! Did you hear about the new art festival starting downtown? 🎨 Here's a joke to kickstart your day: Why don't scientists trust atoms? Because they make up everything! 😂 Any exciting plans for today?"
}
