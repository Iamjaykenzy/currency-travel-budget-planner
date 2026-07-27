"""
Gemini AI Service
-----------------
This module connects the application to Google's Gemini API and
generates travel recommendations based on user travel information.

Author: Ekene Nwakonobi
Module: Gemini AI Integration
"""
# Note:
# This project currently uses the google-generativeai package.
# Google has announced a newer SDK (google-genai), but this version
# remains functional for this project.

import google.generativeai as genai


class AIService:
    """
    Handles communication with the Gemini API.
    """

    def __init__(self, api_key):
        """
        Initialize Gemini with an API key.
        """
        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_travel_advice(
        self,
        destination,
        budget,
        duration,
        currency,
        travelers=1,
    ):
        """
        Generate AI travel advice.

        Parameters:
            destination (str)
            budget (float)
            duration (int)
            currency (str)
            travelers (int)

        Returns:
            str
        """

        if not destination:
            raise ValueError("Destination cannot be empty.")

        if budget <= 0:
            raise ValueError("Budget must be greater than zero.")

        if duration <= 0:
            raise ValueError("Duration must be greater than zero.")

        if travelers <= 0:
            raise ValueError("Travelers must be at least 1.")

        prompt = f"""
You are an experienced travel advisor.

Travel Details

Destination: {destination}
Budget: {budget} {currency}
Duration: {duration} days
Number of Travelers: {travelers}

Provide:

1. Budget evaluation.
2. Money-saving tips.
3. Transportation suggestions.
4. Accommodation advice.
5. Safety tips.
6. Best travel period if applicable.
7. Overall recommendation.

Keep the response friendly and concise.
"""

        try:
            response = self.model.generate_content(prompt)

            return response.text

        except Exception as e:
            return f"Gemini API Error: {e}"