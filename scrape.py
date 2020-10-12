

def website_grab(website):
    website = str(website)
    n = website.count('businessWebsite":null')
    if n == 0:
        website = website.split('businessWebsite')
        website = website[1].split('website_link')
        website = website[0][39:]
        website = website.split('&')
        website = website[0]
        if website.count("www") == 1:
            website = website
        else:
            website = "www." + website
        if website.count("2F") == 1:
            website = website.split("2F")
            website = website[0][:-1]
        else:
            pass
    else:
        website = "No business website detected"
    return website


def smoking_grab (smoking):
    smoking = str(smoking)
    outside = smoking.count("Smoking Outside Only")
    inside = smoking.count("Smoking Allowed")
    return outside, inside
