# Class to interact with grumba bot

import tweepy
from Person import Person

class Grumba:
    # {string} username 
    def __init__(this, username) -> None:
        # Use these keys for read only api calls (my own account)
        this.auth = tweepy.OAuthHandler("Z6DJoiHjExjTiBh7eBSu976xd", "WWooaalC3TY1E06o52waBrQI8QQVtDyhp9bW0wNEysMJ8H4ePh")
        this.getAuth()
        # After auth is set make the API 
        this.api = tweepy.API(this.auth)

        # List of {person} to keep track of all people to reply to
        this.people = this.getPeople()
        # List of names of files
        this.media = this.getMedia()
        # List copy pastas
        this.pastas = this.getPastas()

    # TODO Store access tokens in a file and check if they're in there instead of getting new ones every run
    def getAuth(this):
        try:
            redirect_url = this.auth.get_authorization_url()
            print(redirect_url)
        except tweepy.TweepError:
            print('Error! Failed to get request token.')
        
        verifier = input("Verifier: ")

        try:
            this.auth.get_access_token(verifier)
        except tweepy.TweepError:
            print("Error! Failed to get access token.")

    # Add all users to the list of users
    def getPeople(this):
        users = []

        infile = open("../data/users.txt")
        for aline in infile:
            line_stripped = aline.strip()
            a_user = Person(this.api, line_stripped)
            users.append(a_user)

        infile.close()
        return users
    
    # Get the filenames of the pictures
    def getMedia(this):
        media = []
        infile = open( "../data/media.txt" )
        for aline in infile:
            file_name = aline.strip()
            media.append( file_name )

        infile.close()
        return media

    # Get the strings of all the copypastas
    def getPastas():
        pastas = []
        infile = open("../data/copy_pastas.txt")
        for aline in infile:
            pasta = aline.strip()
            pastas.append( pasta )

        infile.close()
        return pastas
        