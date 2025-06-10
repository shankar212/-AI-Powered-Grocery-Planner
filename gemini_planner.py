import google.generativeai as genai
import json
import re

# ✅ Configure Gemini with your API key
genai.configure(api_key="AIzaSyC0-_54ASSpLWDeUoTH-DVr_AfLM09oVqY")

# Use Gemini 1.5 Flash model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_meal_plan(diet, household_size, budget):
    prompt = f"""
    Generate a 7-day meal plan for a household of {household_size} people
    following a {diet} diet, with a weekly grocery budget of ${budget}.

    Output strictly as valid JSON. Each day must include:
    - "day": day name
    - "meals": list of 3 meal names (breakfast, lunch, dinner)
    - "ingredients": list of 3 ingredient lists (one per meal)

    Example:
    [
      {{
        "day": "Monday",
        "meals": ["Meal 1", "Meal 2", "Meal 3"],
        "ingredients": [["item1", "item2"], ["item3"], ["item4", "item5"]]
      }},
      ...
    ]
    """

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        # Remove optional code block like ```json ... ```
        cleaned_text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.DOTALL).strip()

        print("✅ Cleaned Gemini Output:\n", cleaned_text[:300], "...")  # Debug: first 300 chars

        parsed = json.loads(cleaned_text)

        # Handle both array and wrapped object formats
        if isinstance(parsed, list):
            return parsed
        elif isinstance(parsed, dict):
            for value in parsed.values():
                if isinstance(value, list):
                    return value

        print("⚠️ Unexpected JSON format.")
        return []

    except Exception as e:
        print("⚠️ Error generating or parsing meal plan:", e)
        return []
