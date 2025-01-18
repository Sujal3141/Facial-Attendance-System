import os
import traceback
from PIL import Image
from django.shortcuts import render, HttpResponse
from sklearn.metrics.pairwise import cosine_similarity
from deepface import DeepFace
from .forms import UserProfileForm
from .models import UserProfile
import os
from django.shortcuts import render, HttpResponse
from PIL import Image
from deepface import DeepFace
from .models import UserProfile
import os
from django.shortcuts import render, HttpResponse
from deepface import DeepFace
from sklearn.metrics.pairwise import cosine_similarity
from .models import UserProfile
from django.db import models

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# @login_required
# def LoginView(request):
#     user_profiles = UserProfile.objects.all()
#     return render(request, 'view_profiles.html', {'user_profiles': view_profiles})


def increment_attendance(user_id):
    try:
        print(f"Attempting to increment attendance for user_id: {user_id}")
        user = UserProfile.objects.get(user_id=user_id)
        print(f"User found: {user}")
        user.user_Attendance_Count += 1
        user.save()
        print(f"Attendance for user_id {user_id} incremented successfully.")
        return HttpResponse('view_profiles')
    except UserProfile.DoesNotExist:
        print(f"User with user_id {user_id} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
def extract_face_embedding(image_path):
    """
    Extract face embeddings from the given image path.
    """
    try:
        embedding = DeepFace.represent(image_path, model_name="Facenet")[0]['embedding']
        return embedding
    except Exception as e:
        print(f"Error extracting face embedding: {e}")
        return None

def get_all_saved_embeddings():
    """
    Retrieve embeddings of all saved user images along with their names.
    """
    saved_embeddings = []
    try:
        all_profiles = UserProfile.objects.all()
        for profile in all_profiles:
            try:
                # Get the image path
                img_path = profile.user_img.path
                # Extract embedding
                embedding = extract_face_embedding(img_path)
                if embedding:
                    saved_embeddings.append({'id': profile.user_id, 'embedding': embedding})
            except Exception as e:
                print(f"Error processing profile {profile.user_id}: {e}")
                continue
    except Exception as e:
        print(f"Error retrieving saved embeddings: {e}")
    return saved_embeddings



def extract_face_embedding(image_path):
   
    try:
        embedding = DeepFace.represent(image_path, model_name="Facenet")[0]['embedding']
        return embedding
    except Exception as e:
        print(f"Error extracting face embedding: {e}")
        return None

def get_all_saved_embeddings():
    
    saved_embeddings = []
    try:
        all_profiles = UserProfile.objects.all()
        for profile in all_profiles:
            try:
                # Get the image path
                img_path = profile.user_img.path
                # Extract embedding
                embedding = extract_face_embedding(img_path)
                if embedding:
                    saved_embeddings.append({'id': profile.user_id, 'embedding': embedding})
            except Exception as e:
                print(f"Error processing profile {profile.user_id}: {e}")
                continue
    except Exception as e:
        print(f"Error retrieving saved embeddings: {e}")
    return saved_embeddings

def home(request):
   
    if request.method == 'POST' and 'user_image' in request.FILES:
        try:
            user_image = request.FILES['user_image']
            print("Image received!")

            static_dir = os.path.join(os.path.dirname(__file__), 'static', 'images')
            if not os.path.exists(static_dir):
                os.makedirs(static_dir)

            img_path = os.path.join(static_dir, 'uploaded_image.jpg')
            with open(img_path, 'wb') as temp_img:
                for chunk in user_image.chunks():
                    temp_img.write(chunk)

            uploaded_embedding = extract_face_embedding(img_path)
            if not uploaded_embedding:
                return HttpResponse("Could not extract embedding from the uploaded image.")

            saved_embeddings = get_all_saved_embeddings()

            best_match_name = None
            highest_similarity = 0.2 
            for entry in saved_embeddings:
                similarity = cosine_similarity([uploaded_embedding], [entry['embedding']])[0][0]
                if similarity > highest_similarity:
                    highest_similarity = similarity
                    best_match_id = entry['id']

            if best_match_id:
                response = f"Attendance of id : {best_match_id} is marked with an accuracy of {highest_similarity}<br>"
                increment_attendance(best_match_id)


            else:
                response = "No match found , kindly make sure to register first.<br>"

            return HttpResponse(response)
        except Exception as e:
            print(f"Error processing uploaded image: {e}")
            return HttpResponse("Error processing the uploaded image.")

    return render(request, 'home.html')




def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            print(instance)
            return HttpResponse('User successfully registered!')
        else:
            print(form.errors)
            return HttpResponse('Form submission failed. Check errors.')
    else:
        form = UserProfileForm()
    return render(request, 'new_user.html', {'form': form})

def view_profiles(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'view_profiles.html', {'user_profiles': user_profiles})





