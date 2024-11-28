import openai

class Completion():
    """A wrapper class for OpenAI's chat completion API"""
    
    def __init__(self, oai_client=None, oai_api_key=""):
        """Initialize with either an existing client or an API key"""
        self.oai_client = oai_client if oai_client else openai.OpenAI(api_key=oai_api_key)

    def run(self, content, model, system="", max_tokens=1024, temperature=1, logprobs=False, top_logprobs=None, n=1):
        """
        Generate chat completions using OpenAI's API
        
        Args:
            content (str): The user message content
            model (str): The model to use (e.g. "gpt-3.5-turbo")
            system (str): Optional system message to set context
            max_tokens (int): Maximum tokens in the response
            temperature (float): Controls randomness (0-2)
            logprobs (bool): Whether to return log probabilities
            top_logprobs (int): Number of most likely tokens to return
            n (int): Number of completions to generate
            
        Returns:
            list: The generated completion choices
        """
        response = self.oai_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": content},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            logprobs=logprobs,
            top_logprobs=top_logprobs,
            n=n,
        )
        return response
