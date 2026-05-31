class Planner:

    def create(self, prompt: str):

        return {
            "scenes": [
                {
                    "id": 1,
                    "text": prompt,
                    "visual": "cinematic futuristic battlefield",
                    "voice": "The war begins beyond the stars.",
                    "music": "dark orchestral sci-fi",
                    "duration": 6
                }
            ]
        }
