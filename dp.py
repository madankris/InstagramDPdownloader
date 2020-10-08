from instaloader import instaloader
downld = instaloader.Instaloader()
username = input('enter the username:')
downld.download_profile(username,profile_pic_only=True)
