from django.db import models
from accounts.models import User
import os
from django.core.exceptions import ValidationError


# Function to generate a unique file name based on user's first name
def user_upload_path(instance, filename):
    # Get the user's first name and last name
    user_first_name = instance.user.first_name
    user_last_name = instance.user.last_name

    # Replace spaces with underscores and make the filename lowercase
    filename = filename.replace(' ', '_').lower()

    # Construct the path
    return f"storage_for_users/{user_last_name}_{user_first_name}/{filename}"



def validate_file_extension(value):
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.jpeg', '.png']
    _, file_extension = os.path.splitext(value.name)
    if file_extension.lower() not in valid_extensions:
        raise ValidationError("Unsupported file extension.")
    

def validate_music_file_extension(value):
    valid_extensions = ['.mp3', '.wav', '.flac', '.ogg', '.aac', '.aiff', '.wma', '.m4a' ]  
    _, file_extension = os.path.splitext(value.name)
    if file_extension.lower() not in valid_extensions:
        raise ValidationError("Unsupported music file extension.")
    

def validate_video_extension(value):
    valid_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.WebM', '.3gp', '.3g2', '.h.265']
    _, file_extension = os.path.splitext(value.name)
    if file_extension.lower() not in valid_extensions:
        raise ValidationError("Unsupported video file extension.")
   
    

class DigitalStorage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to=user_upload_path, null=True, blank= True)
    video_file = models.FileField(upload_to=user_upload_path,null=True, blank= True,
                                  validators=[validate_video_extension]
                                  )
    music_file= models.FileField(upload_to=user_upload_path,null=True, blank= True,
                                 validators=[validate_music_file_extension]
                                 )
    
    document_file = models.FileField(upload_to=user_upload_path, null=True, blank= True,
                                     validators=[validate_file_extension]
                                     )
    

    def __str__(self):
        user = self.user
        return f"{user.first_name} {user.last_name} ({user.email})"

    
