import openai
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

class Generator:
    def __init__(self, openai_key=None, fallback_model_name="EleutherAI/gpt-neo-125M"):
        self.openai_key = openai_key
        self.use_openai = openai_key is not None
        self.fallback_tokenizer = None
        self.fallback_model = None
        # Set cache directory in the project folder
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        self.cache_dir = os.path.join(self.project_dir, "models")
        os.makedirs(self.cache_dir, exist_ok=True)
        self.setup_fallback(fallback_model_name)

    def setup_fallback(self, model_name):
        """Load fallback Hugging Face model and tokenizer."""
        try:
            self.fallback_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=self.cache_dir)
            self.fallback_model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=self.cache_dir)
        except Exception as e:
            print(f"Failed to load fallback model: {e}")

    def generate_openai_response(self, query, context):
        """Generate response using OpenAI API."""
        try:
            openai.api_key = self.openai_key
            prompt = f"Answer the query based on the following context: {context}\nQuery: {query}"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return None

    def generate_fallback_response(self, query, context):
        """Generate response using the fallback model."""
        prompt = f"Answer the query based on the following context: {context}\nQuery: {query}"
        inputs = self.fallback_tokenizer(prompt, return_tensors="pt")
        outputs = self.fallback_model.generate(inputs["input_ids"], max_length=150)
        return self.fallback_tokenizer.decode(outputs[0], skip_special_tokens=True)

    def generate_response(self, query, context):
        """Main generator function with OpenAI and fallback support."""
        if self.use_openai:
            response = self.generate_openai_response(query, context)
            if response:
                return response
        return self.generate_fallback_response(query, context)
