import google.generativeai as genai
from PIL import Image
import io

# Replace this with your actual Gemini API key
genai.configure(api_key="AIzaSyBNcuvyE3rT0KyXRYZvx5M6tMSQv4IMBdU")

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')

def generate_responses(name, img_bytes):
    # Open image from bytes
    image = Image.open(io.BytesIO(img_bytes))

    # Create a response from the model: Ugly face rating
    # Pass the name and the image bytes in the prompt
    resp1 = model.generate_content([
        f"As a funny beauty pageant judge, rate {name}'s fabulous face on a scale of 1 (sassy disaster) to 10 (divine beauty). Make it comedic! Only give a number", 
        image
    ])
    ugly_score = resp1.text.strip()

    # Create a response from the model: Funny roast
    resp2 = model.generate_content([
        f"Roast this person like a stand-up comedian. Name: {name}. Keep it hilarious and make it just 3 to 4 lines.", 
        image
    ])
    roast = resp2.text.strip()

    # Create a response from the model: Fortune telling
    resp3 = model.generate_content([
        f"As a fortune teller, tell {name} their funny fate today in just 2 lines."
    ])
    fortune = resp3.text.strip()

    # Create a response from the model: Age guessing
    resp4 = model.generate_content([
        f"Guess the age of {name} based on the image, just give a number.", 
        image
    ])
    age_guess = resp4.text.strip()

    return ugly_score, roast, fortune, age_guess
