from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import openai

# if not config.API_KEY:
#     raise ValueError("API key not found. Make sure to set the 'API_KEY' in config.py.")


def index(request):
    return render(request, 'chatapp/index.html')

def specific(request):
    return HttpResponse("list1")


# def getResponse(request):
#     userMessage = request.GET.get('userMessage')

#     return HttpResponse(userMessage)

# def chatbot(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         response = 'Hi there'
#         return JsonResponse({'message': message, 'response': response})
#     return render(request, 'index.html',)

openai_api_key = 'API-KEY'
openai.api_key = openai_api_key

def ask_openai(userMessage):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        prompt = userMessage,
        max_tokens = 50,
        n=1,
        stop=None,
        temperture=0.7,
    )
    
    answer = response.choices[0].text.strip()
    return answer



# def ask_gemini(userMessage):
#     response = genai.GenerativeModel(
#         model="gemini-1.5-flash",  # Replace with the actual model identifier
#         prompt=userMessage,
#         max_tokens=150,
#         temperature=0.7,
#     )
    
#     answer = response['text'].strip()
#     return answer
    
def getUserResponse(request):
    if request.method == 'POST':
        userMessage = request.POST.get('message')
        response = ask_openai(userMessage)
        return JsonResponse({'message': userMessage, 'response': response})
    return render(request, 'index.html',)



# Define the generation configuration
# generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 64,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }

# # Initialize the model
# model = genai.GenerativeModel(
#     model_name="gemini-1.5-flash",
#     generation_config=generation_config,
# )

# # Define a function to ask the model a question and get the response
# def ask_gemini(userMessage):
#     response = model
#     return response.text

# def getUserResponse(request):
#     if request.method == 'POST':
#         userMessage = request.POST.get('message')
#         response = ask_gemini(userMessage)
#         return JsonResponse({'message': userMessage, 'response': response})
#     return render(request, 'index.html')
