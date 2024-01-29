import requests
from plyer import notification
import datetime

def get_horoscope(sign):
    base_url = "https://aztro.sameerkumar.website/?"
    params = {
        "sign": sign,
        "day": "today"
    }

    response = requests.post(base_url, params=params)
    horoscope_data = response.json()

    return horoscope_data.get('description', 'Unable to fetch horoscope.')

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # e.g., 'path/to/icon.png'
        timeout=10,
    )

def main():
    # Replace 'YOUR_SIGN' with the zodiac sign for which you want to receive daily horoscope
    zodiac_sign = 'YOUR_SIGN'

    # Get today's date
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Fetch horoscope for the specified sign
    horoscope = get_horoscope(zodiac_sign)

    # Display and notify the user
    notification_title = f"Daily Horoscope - {zodiac_sign.capitalize()} ({today_date})"
    send_notification(notification_title, horoscope)
    print(f"{notification_title}\n{horoscope}")

if __name__ == "__main__":
    main()
