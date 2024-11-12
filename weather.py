import requests
import openai

# Set your API keys
openai.api_key = ''
DAPPIER_API_KEY = ''

def call_dappier_api(query):
    url = 'https://api.dappier.com/app/aimodel/am_01j06ytn18ejftedz6dyhz2b15'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {DAPPIER_API_KEY}',
    }
    data = {
        'query': query
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    json_response = response.json()
    
    return json_response

def main():
    # Receive request
    location = input('Enter your location (e.g., "Austin, TX"): ')

    # Call Dappier API for Weather
    weather_query = f'What is the weather in {location} today?'
    weather_response = call_dappier_api(weather_query)
    # Extract weather information from response
    weather = weather_response.get('answer') or weather_response.get('result') or weather_response.get('data') or str(weather_response)

    # Call Dappier API for Latest News
    news_query = f'What is the latest news in {location} today?'
    news_response = call_dappier_api(news_query)
    # Extract news information from response
    news = news_response.get('answer') or news_response.get('result') or news_response.get('data') or str(news_response)

    # Prepare ChatGPT prompt
    system_prompt = '''You are an Assistant who responds to requests first thing in the morning. Your job is to greet the user and provide them with the latest weather and news. Make the response playful, like a text message, and keep it short. Add a joke to brighten their day and ask a follow-up question.'''

    user_message = f'News - {news}\nWeather - {weather}'

    # ChatGPT Integration
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=500,
        n=1,
        temperature=0.7,
    )

    assistant_response = response['choices'][0]['message']['content']

    # Return the response
    result = {
        'Response': assistant_response
    }
    print(result)

if _name_ == '_main_':
    main()
