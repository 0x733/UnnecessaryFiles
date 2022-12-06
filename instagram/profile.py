import instaloader

ig = instaloader.Instaloader()
dp = input("Kullanıcı Adını Gir Amcık : ")

ig.download_profile(dp  ,   profile_pic_only=True)
