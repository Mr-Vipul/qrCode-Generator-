import qrcode 

img = qrcode.make('https://www.link')  #Paste your link here
type(img) 
img.save("LinkedInProfile.png")