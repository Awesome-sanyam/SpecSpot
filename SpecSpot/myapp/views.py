# myapp/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
import google.generativeai as genai
import json
import logging
from urllib.parse import unquote
from .models import Feedback,Phone,GlossaryTerm
from django.shortcuts import get_object_or_404


# ... (start_view, home_view, logout_view, etc. remain unchanged) ...
def start_view(request):
    return render(request, "start.html")

def home_view(request):
    # Get the 3 most recent feedback items to display on the homepage
    latest_feedback = Feedback.objects.order_by('-timestamp')[:3]

    # Dynamically create initials for the user profile images
    for item in latest_feedback:
        names = item.user.username.split()
        if len(names) > 1:
            item.user_initials = (names[0][0] + names[-1][0]).upper()
        else:
            item.user_initials = names[0][0].upper()

    popular_phones = Phone.objects.filter(is_popular=True)[:4]

    context = {
        'feedback_items': latest_feedback,
        'popular_phones': popular_phones
    }
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('start')

if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)


def about_view(request):
    return render(request, 'about.html')

def terms_view(request):
    return render(request, 'terms.html')

def login_view(request):
    return render(request, "login.html")

def register_view(request):
    return render(request, "register.html")

@login_required
def phone_view(request):
    phones = Phone.objects.all()
    phones_list = []
    for phone in phones:
        phones_list.append({
            'name': phone.name,
            'brand': phone.brand,
            'price': phone.price,
            'ram': phone.ram,
            'camera': phone.camera,
            'battery': phone.battery,
            'processor': phone.processor,
            'displayType': phone.display_type,
            'specs': phone.specs
        })
    

    context = {
        'phones_data_json': phones_list
    }
    return render(request,'Phones.html', context)

@csrf_exempt
def login_api_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                if user.is_superuser:
                    redirect_url = reverse('admin_dashboard')
                else:
                    redirect_url = reverse('home')
                
                return JsonResponse({'success': True, 'redirect_url': redirect_url})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid username or password.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON.'}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
def register_api_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username", "").strip()
            email = data.get("email", "").strip()
            password = data.get("password", "")

            if not all([username, email, password]):
                 return JsonResponse({'success': False, 'error': 'All fields are required.'}, status=400)
            if User.objects.filter(username=username).exists():
                return JsonResponse({'success': False, 'error': 'Username is already taken.'}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'error': 'An account with this email already exists.'}, status=400)

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            return JsonResponse({'success': True, 'message': 'Account created successfully! Please log in.'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON.'}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
def ai_phone_finder(request):
    if request.method == "POST":
        if not settings.GEMINI_API_KEY:
             return JsonResponse({'error': 'GEMINI_API_KEY not configured on the server.'}, status=500)
        try:
            data = json.loads(request.body)
            prompt_text = data.get('prompt')
            if not prompt_text:
                return JsonResponse({'error': 'Prompt is missing.'}, status=400)

            # --- MORE ROBUST PROMPT ---
            # This prompt emphasizes that both keys are mandatory.
            structured_prompt = f"""
            Based on the user's request: "{prompt_text}", perform two tasks:
            1. Recommend up to 10 suitable mobile phones.
            2. Provide a summary explaining which phone is the best overall choice from the list and why.

            Your response MUST be a single, valid JSON object. The root of this object MUST contain exactly two keys: "summary_recommendation" and "recommendations".

            - `summary_recommendation`: A string (2-3 sentences) explaining the top pick from the list and the reasoning. This key is mandatory.
            - `recommendations`: An array of phone objects.

            Each phone object inside the `recommendations` array must have these keys:
            - "name": String
            - "tagline": String
            - "price": String
            - "specs": An array of exactly 4 strings.

            Example format to follow strictly:
            {{
              "summary_recommendation": "For the best balance of camera quality and price, the Example Phone 1 is the top choice. Its 108MP camera is a standout in this range, making it ideal for photography.",
              "recommendations": [
                {{
                  "name": "Example Phone 1",
                  "tagline": "A great all-rounder.",
                  "price": "Approx. ₹29,999",
                  "specs": [
                    "6.5\\" AMOLED Display",
                    "Snapdragon 8 Gen 1",
                    "108MP Main Camera",
                    "5000mAh Battery"
                  ]
                }}
              ]
            }}

            Ensure the final output is only the JSON object, without any markdown formatting like ```json. Both 'summary_recommendation' and 'recommendations' keys must be present at the top level.
            """
            
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content(structured_prompt)
            
            ai_response_text = response.text.strip().replace('```json', '').replace('```', '')
            ai_data = json.loads(ai_response_text)
            
            return JsonResponse(ai_data)

        except json.JSONDecodeError as e:
            logging.error(f"JSON Decode Error in ai_phone_finder: {e}\\nAI Response was: {ai_response_text}")
            return JsonResponse({'error': 'Failed to parse the AI response. It might be in an invalid format.'}, status=500)
        except Exception as e:
            logging.error(f"An error occurred in ai_phone_finder: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
def ai_tech_chat(request):
    if request.method == "POST":
        if not settings.GEMINI_API_KEY:
             return JsonResponse({'error': 'GEMINI_API_KEY not configured on the server.'}, status=500)
        try:
            data = json.loads(request.body)
            prompt_text = data.get('prompt')
            if not prompt_text:
                return JsonResponse({'error': 'Prompt is missing.'}, status=400)

            # --- SYSTEM INSTRUCTION FOR TECH CHAT ---
            system_instruction = """
            You are 'SpecSpot AI', a friendly and knowledgeable assistant specializing in technology. 
            Your expertise includes mobile phones, gadgets, computers, software, and general tech news.
            Your goal is to provide clear, concise, and helpful answers.

            RULES:
            1.  Strictly answer questions related to technology only.
            2.  If a user asks about a non-tech topic (e.g., politics, cooking, history, medical advice), you MUST politely decline.
            3.  When declining, suggest they ask a tech-related question instead. 
                Example responses for declining:
                - "I specialize in technology, so I can't help with that. Feel free to ask me anything about phones, laptops, or other gadgets!"
                - "My knowledge is focused on the tech world. Could you ask me something about technology instead?"
                - "That's a bit outside my area of expertise, which is technology. How about we talk about the latest tech news?"
            """
            
            model = genai.GenerativeModel(
                model_name='gemini-2.5-flash',
                system_instruction=system_instruction
            )
            response = model.generate_content(prompt_text)
            
            return JsonResponse({'response': response.text})

        except Exception as e:
            logging.error(f"An error occurred in ai_tech_chat: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=405)


def get_phone_specs(request, phone_name):
    phone_name_clean = unquote(phone_name)
    context = {
        'phone_name': phone_name_clean.title()
    }
    return render(request, 'specification.html', context)


def api_get_phone_specs_json(request, phone_name):
    phone_name_clean = unquote(phone_name)

    if not settings.GEMINI_API_KEY:
        return JsonResponse({'error': 'GEMINI_API_KEY not configured on the server.'}, status=500)

    try:
        structured_prompt = f"""
        Based on the phone name "{phone_name_clean}", provide a comprehensive and detailed technical specification sheet.
        Provide your response as a single, clean JSON object. The keys must be exactly as follows, with string values. If a value is unknown, use a relevant placeholder like "N/A" or "Not specified".
        Example format to follow strictly:
        {{
            "name": "{phone_name_clean}", "network": {{ "technology": "GSM / HSPA / LTE / 5G" }}, "launch": {{ "announced": "2025, September", "status": "Available. Released 2025, October" }}, "body": {{ "dimensions": "160.8 x 78.1 x 7.7 mm", "weight": "240 g", "build": "Glass front (Gorilla Glass), glass back (Gorilla Glass), stainless steel frame", "sim": "Nano-SIM and eSIM", "durability": "IP68 dust/water resistant" }}, "display": {{ "type": "LTPO Super Retina XDR OLED, 120Hz", "size": "6.7 inches", "resolution": "1284 x 2778 pixels", "protection": "Ceramic Shield glass", "features": "1000 nits (HBM), 1200 nits (peak)" }}, "platform": {{ "os": "iOS 18", "chipset": "Apple A18 Bionic (5 nm)", "cpu": "Hexa-core", "gpu": "Apple GPU (5-core graphics)" }}, "memory": {{ "card_slot": "No", "internal": "128GB 8GB RAM, 256GB 8GB RAM, 512GB 8GB RAM, 1TB 8GB RAM" }}, "main_camera": {{ "modules": "Triple: 48 MP (wide), 12 MP (telephoto), 12 MP (ultrawide)", "features": "Dual-LED flash, HDR", "video": "4K@24/30/60fps, 1080p@30/60/120/240fps" }}, "selfie_camera": {{ "modules": "Single: 12 MP (wide)", "features": "HDR", "video": "4K@24/30/60fps, 1080p@30/60/120fps" }}, "sound": {{ "loudspeaker": "Yes, with stereo speakers", "jack": "No" }}, "comms": {{ "wlan": "Wi-Fi 802.11 a/b/g/n/ac/6, dual-band", "bluetooth": "5.3, A2DP, LE", "positioning": "GPS, GLONASS, GALILEO, QZSS, BDS", "nfc": "Yes", "radio": "No", "usb": "USB Type-C 2.0, DisplayPort" }}, "features": {{ "sensors": "Face ID, accelerometer, gyro, proximity, compass" }}, "battery": {{ "type": "Li-Ion 4352 mAh, non-removable", "charging": "Wired, PD2.0, 50% in 30 min (advertised), 15W wireless" }}, "misc": {{ "colors": "Graphite, Silver, Gold, Sierra Blue", "models": "A2643, A2484, A2641", "price": "About 1100 EUR" }}
        }}
        Only return the JSON object itself, without any markdown formatting like ```json or any other explanatory text.
        """
        
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(structured_prompt)
        ai_response_text = response.text.strip().replace('```json', '').replace('```', '')
        phone_data = json.loads(ai_response_text)
        
        return JsonResponse(phone_data)

    except Exception as e:
        logging.error(f"An error occurred in api_get_phone_specs_json for {phone_name_clean}: {e}")
        return JsonResponse({'error': f'An unexpected error occurred: {e}'}, status=500)

@login_required
def admin_dashboard_view(request):
    if not request.user.is_superuser:
        return redirect('home')

    sort_option = request.GET.get('sort', 'newest') 
    
    if sort_option == 'oldest':
        feedback_items = Feedback.objects.all().order_by('timestamp')
    elif sort_option == 'a-z':
        feedback_items = Feedback.objects.all().order_by('user__username')
    else:
        feedback_items = Feedback.objects.all().order_by('-timestamp')


    all_users_query = User.objects.filter(is_superuser=False)

    if sort_option == 'oldest':
        all_users = all_users_query.order_by('date_joined')
    elif sort_option == 'a-z':
        all_users = all_users_query.order_by('username')
    else:
        all_users = all_users_query.order_by('-date_joined')


    all_phones_query = Phone.objects.all()

    if sort_option == 'oldest':
        all_phones = all_phones_query.order_by('id') 
    elif sort_option == 'a-z':
        all_phones = all_phones_query.order_by('name') 
    else:
        all_phones = all_phones_query.order_by('-id')

    all_glossary_query = GlossaryTerm.objects.all()

    if sort_option == 'oldest':
        all_glossary_terms = all_glossary_query.order_by('id') 
    elif sort_option == 'a-z':
        all_glossary_terms = all_glossary_query.order_by('term') 
    else:
        all_glossary_terms = all_glossary_query.order_by('-id') 
    context = {
        'feedback_items': feedback_items,
        'current_sort': sort_option,
        'all_users': all_users,
        'all_glossary_terms': all_glossary_terms,
        'all_phones': all_phones
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def add_phone_view(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            brand = request.POST.get('brand')
            price = int(request.POST.get('price'))
            ram = int(request.POST.get('ram'))
            camera = int(request.POST.get('camera'))
            battery = int(request.POST.get('battery'))
            processor = request.POST.get('processor')
            display_type = request.POST.get('display_type')
            
            tagline = request.POST.get('tagline', '')
            is_popular = request.POST.get('is_popular') == 'on'
            image = request.FILES.get('image')

            specs_raw = request.POST.get('specs', '')
            specs_list = [spec.strip() for spec in specs_raw.splitlines() if spec.strip()]

            Phone.objects.create(
                name=name,
                brand=brand,
                price=price,
                ram=ram,
                camera=camera,
                battery=battery,
                processor=processor,
                display_type=display_type,
                specs=specs_list,
                tagline=tagline,
                is_popular=is_popular,
                image=image
            )
        except Exception as e:
            print(f"Error adding phone: {e}")
            pass
            
    return redirect('admin_dashboard')


# DELETING PHONES(admin)
@login_required
def delete_phones_view(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    if request.method == 'POST':
        phone_ids_to_delete = request.POST.getlist('phone_ids')
        
        if phone_ids_to_delete:
            Phone.objects.filter(id__in=phone_ids_to_delete).delete()
            
    return redirect('admin_dashboard')

# edit phone data(admin)
@login_required
def edit_phone_view(request, phone_id):
    if not request.user.is_superuser:
        return redirect('home')

    phone_to_edit = get_object_or_404(Phone, id=phone_id)

    if request.method == 'POST':
        try:
            phone_to_edit.name = request.POST.get('name')
            phone_to_edit.brand = request.POST.get('brand')
            try: phone_to_edit.price = int(request.POST.get('price'))
            except: pass
            try: phone_to_edit.ram = int(request.POST.get('ram'))
            except: pass
            try: phone_to_edit.camera = int(request.POST.get('camera'))
            except: pass
            try: phone_to_edit.battery = int(request.POST.get('battery'))
            except: pass
            phone_to_edit.processor = request.POST.get('processor')
            phone_to_edit.display_type = request.POST.get('display_type')
            
            phone_to_edit.tagline = request.POST.get('tagline', '')
            phone_to_edit.is_popular = request.POST.get('is_popular') == 'on'
            
            new_image = request.FILES.get('image')
            if new_image:
                phone_to_edit.image = new_image

            specs_raw = request.POST.get('specs', '')
            phone_to_edit.specs = [spec.strip() for spec in specs_raw.splitlines() if spec.strip()]

            phone_to_edit.save()
        except Exception as e:
            print(f"Error editing phone: {e}")
            pass
            
    return redirect('admin_dashboard')

@login_required
def delete_users_view(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    if request.method == 'POST':
        user_ids_to_delete = request.POST.getlist('user_ids')
        
        if user_ids_to_delete:
            User.objects.filter(id__in=user_ids_to_delete, is_superuser=False).delete()
            
    return redirect('admin_dashboard')

@login_required
def delete_feedback_view(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    if request.method == 'POST':
        feedback_ids_to_delete = request.POST.getlist('feedback_ids')
        
        if feedback_ids_to_delete:
            Feedback.objects.filter(id__in=feedback_ids_to_delete).delete()
            
    return redirect('admin_dashboard')

@login_required
@csrf_exempt
def submit_feedback_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message')

            if not message:
                return JsonResponse({'success': False, 'error': 'Feedback message cannot be empty.'}, status=400)

            Feedback.objects.create(user=request.user, message=message)
            return JsonResponse({'success': True, 'message': 'Thank you for your feedback!'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'An error occurred.'}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@login_required
def add_glossary_view(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        try:
            term = request.POST.get('term')
            icon_name = request.POST.get('icon_name')
            definition = request.POST.get('definition')
            example = request.POST.get('example')

            GlossaryTerm.objects.create(
                term=term,
                icon_name=icon_name,
                definition=definition,
                example=example
            )
        except Exception as e:
            print(f"Error adding glossary term: {e}")
            pass
            
    return redirect('admin_dashboard')

@login_required
def edit_glossary_view(request, term_id):
    if not request.user.is_superuser:
        return redirect('home')

    term_to_edit = get_object_or_404(GlossaryTerm, id=term_id)

    if request.method == 'POST':
        try:
            term_to_edit.term = request.POST.get('term')
            term_to_edit.icon_name = request.POST.get('icon_name')
            term_to_edit.definition = request.POST.get('definition')
            term_to_edit.example = request.POST.get('example')
            
            term_to_edit.save()
        except Exception as e:
            print(f"Error editing glossary term: {e}")
            pass
            
    return redirect('admin_dashboard')

@login_required
def delete_glossary_view(request):
    if not request.user.is_superuser:
        return redirect('home')
    
    if request.method == 'POST':
        glossary_ids_to_delete = request.POST.getlist('glossary_ids')
        
        if glossary_ids_to_delete:
            GlossaryTerm.objects.filter(id__in=glossary_ids_to_delete).delete()
            
    return redirect('admin_dashboard')

@login_required
def brands_view(request):
    return render(request, 'Brands.html')

@csrf_exempt
def api_get_brand_data(request):

    if request.method == "POST":
        if not settings.GEMINI_API_KEY:
             return JsonResponse({'error': 'GEMINI_API_KEY not configured on the server.'}, status=500)
        try:
            data = json.loads(request.body)
            brand_name = data.get('brand')

            if not brand_name:
                return JsonResponse({'error': 'Missing brand parameter. This API endpoint only fetches devices for a specified brand.'}, status=400)

            model = genai.GenerativeModel('gemini-2.5-flash')

            structured_prompt = f"""
            Generate a list of the 10 latest and best **hot deals** for mobile phone models currently available from the brand "{brand_name}".
            Focus on models with current promotions, sales, or excellent value, and provide realistic price and buy link placeholders.

            Your response MUST be a single, valid JSON object with a key "devices".

            - `devices`: An array of exactly 10 phone objects.

            Each phone object inside the `devices` array must have these keys:
            - "name": String (e.g., Galaxy S25 Ultra)
            - "tagline": String (A short description of the deal, e.g., Limited-time sale with free earbuds!)
            - "price": String (The **deal price** with currency, e.g., $799 or Deal Price: ₹65,000)
            - "buy_link": String (A realistic-looking, but placeholder, purchase URL for the deal, e.g., https://example.com/{brand_name}/s25-ultra-deal)
            - "specs": An array of exactly 4 strings (Key specs: Display size/type, Processor/Chip, Camera details, Battery capacity/features).

            Ensure the final output is ONLY the JSON object, without any surrounding markdown fences like ```json or any other text.
            """
            
            response = model.generate_content(structured_prompt)
            ai_response_text = response.text.strip()

            if ai_response_text.startswith("```json"):
                ai_response_text = ai_response_text.replace("```json", "", 1)
            if ai_response_text.endswith("```"):
                ai_response_text = ai_response_text[:-3]

            json_data = json.loads(ai_response_text)
            
            if 'devices' in json_data and isinstance(json_data['devices'], list):
                return JsonResponse(json_data)
            else:
                return JsonResponse({'error': 'Invalid JSON structure returned from AI model.'}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'AI model returned non-JSON data.'}, status=500)
        except Exception as e:
            logging.error(f"An error occurred in api_get_brand_data: {e}")
            return JsonResponse({'error': f'AI Server Error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@login_required
def glossary_view(request):
    all_terms = GlossaryTerm.objects.all()
    
    context = {
        'glossary_terms': all_terms
    }
    return render(request, 'glossary.html', context)

def api_get_tech_news(request):

    if request.method == "GET":
        if not settings.GEMINI_API_KEY:
             return JsonResponse({'error': 'GEMINI_API_KEY not configured on the server.'}, status=500)
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            structured_prompt = """
            Generate a list of 3 recent and significant tech news articles.
            The articles must be related to mobile phones, AI, processors, or major tech companies.

            Your response MUST be a single, valid JSON object with a key "articles".

            - `articles`: An array of exactly 3 news article objects.

            Each article object inside the `articles` array must have these keys:
            - "title": String (The headline of the news)
            - "description": String (A short 1-2 sentence summary)
            - "image_url": String (A valid, direct URL to a relevant image for the article)
            - "article_url": String (A valid, full URL to the original article)

            Example format to follow strictly:
            {
              "articles": [
                {
                  "title": "New 'Snapdragon 9 Gen 1' Details Leaked",
                  "description": "The next-generation chip promises a 30% performance boost and enhanced AI capabilities for upcoming flagship phones.",
                  "image_url": "https://example.com/images/snapdragon.jpg",
                  "article_url": "https://www.techsite.com/news/snapdragon-9-gen-1-leak"
                },
                {
                  "title": "Google Announces 'Gemini 2.0' AI Model",
                  "description": "Google's latest AI model, Gemini 2.0, is set to be integrated into all Pixel devices by the end of the year.",
                  "image_url": "https://example.com/images/gemini-ai.png",
                  "article_url": "https://www.googleblog.com/ai/gemini-2"
                },
                {
                  "title": "Apple's Foldable iPhone Delayed to 2027",
                  "description": "Reports suggest that Apple is facing challenges with display durability, pushing the potential release of a foldable iPhone back.",
                  "image_url": "https://example.com/images/apple-foldable.jpg",
                  "article_url": "https://www.macrumors.com/apple-foldable-delayed"
                }
              ]
            }

            Ensure the final output is ONLY the JSON object, without any surrounding markdown fences like ```json or any other text.
            """
            
            response = model.generate_content(structured_prompt)
            ai_response_text = response.text.strip()

            if ai_response_text.startswith("```json"):
                ai_response_text = ai_response_text.replace("```json", "", 1)
            if ai_response_text.endswith("```"):
                ai_response_text = ai_response_text[:-3]

            json_data = json.loads(ai_response_text)
            
            if 'articles' in json_data and isinstance(json_data['articles'], list) and len(json_data['articles']) == 3:
                return JsonResponse(json_data)
            else:
                logging.error(f"Invalid JSON structure from AI: {ai_response_text}")
                return JsonResponse({'error': 'Invalid JSON structure returned from AI model.'}, status=500)

        except json.JSONDecodeError:
            logging.error(f"JSON Decode Error in api_get_tech_news: {ai_response_text}")
            return JsonResponse({'error': 'AI model returned non-JSON data.'}, status=500)
        except Exception as e:
            logging.error(f"An error occurred in api_get_tech_news: {e}")
            return JsonResponse({'error': f'AI Server Error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
