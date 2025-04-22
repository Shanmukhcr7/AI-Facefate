import google.generativeai as genai
from PIL import Image
import io

genai.configure(api_key="AIzaSyC0lY3dWDTRsi-lrf4vhS79VcYsAgii3Zw")  # replace with env var in production

model = genai.GenerativeModel('gemini-2.0-flash')

def generate_responses(name, img_bytes):
    image = Image.open(io.BytesIO(img_bytes))

    prompt = f"""
    Here's an image of {name}.
    
    1. As a funny beauty pageant judge, rate {name}'s fabulous face from 1 (sassy disaster) to 10 (divine beauty). Only give a number.

    2. Roast {name} like a stand-up comedian in 3-4 lines.

    3. As a fortune teller, tell {name} their funny fate in 2 lines.

    4. Guess {name}'s age (just give a number).
    """

    response = model.generate_content([prompt, image])
    output = response.text.strip().split("\n")

    ugly_score = output[0].strip()
    roast = "\n".join(output[1:4]).strip()
    fortune = output[4].strip()
    age_guess = output[-1].strip()

    return ugly_score, roast, fortune, age_guess