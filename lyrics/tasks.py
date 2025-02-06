from celery import shared_task
from .models import lyric
import random

# Registers this function as a celery task
# Everytime the task runs, it picks a random lyric from the list and saves it to the database
@shared_task
def generate_new_lyric():
    # A list of sample lyrics to choose from
    possible_lyrics = [
        "They told us that our gods would outlive us, they lied",
        "The art of dying, a gauntlet of rhythmic violence",
        "A sprint though broken glass, Vordhobsn",
        "Ain't in funny, this carnival of self-destruction",
        "This is my moon song, love as a quiet apocalypse",
    ]

    new_lyric = random.choice(possible_lyrics)

    # Save the lyric to the database
    lyric.objects.create(text=new_lyric)

    print("New Lyric Generated:", new_lyric)
