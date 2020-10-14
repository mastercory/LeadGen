

def website_grab(website):
    try:
        website = str(website)
        n = website.count('businessWebsite":null')
        if n == 0:
            if website.count('businessWebsite":{"href":"/biz_redir?url=https') == 1:
                website = website.split('businessWebsite":{"href":"/biz_redir?url=https')
                website = website[1]
            else:
                website = website.split('businessWebsite":{"href":"/biz_redir?url=http')
                website = website[1]
            website = website.split('&amp;website_link')
            website = website[0]
            if website.count('%3A%2F%2F') == 1:
                website = website.split('%3A%2F%2F')
                website = website[1]
            else:
                pass
            if website.count('%2F') > 0:
                website = website.split('%2F', 1)
                website = website[0]
            else:
                pass
            if website.count('www') == 0:
                website = "www." + website
            else:
                pass
        else:
            website = "No business website detected"
    except:
        website = "No business website detected"
    return website


def smoking_grab(smoking):
    smoking = str(smoking)
    outside = smoking.count("Smoking Outside Only")
    inside = smoking.count("Smoking Allowed")
    return outside, inside


def social_grab(social):
    facebook = str(social)

    # FIND FB?

    if facebook.count('facebook.com/') > 0:
        facebook = facebook.split('facebook.com/')
        facebook = facebook[1]
        facebook = "http://www.facebook.com/" + facebook
    else:
        facebook = "N/A"

    # TAIL DELIMITERS

    if facebook.count('">') > 0:
        facebook = facebook.split('">', 1)
        facebook = facebook[0]
    if facebook.count('?') > 0:
        facebook = facebook.split('?', 1)
        facebook = facebook[0]
    if facebook.count('"') > 0:
        facebook = facebook.split('"', 1)
        facebook = facebook[0]
    else:
        pass

    # FIND INSTA?

    insta = str(social)
    if insta.count('instagram.com/') > 0:
        insta = insta.split('instagram.com/')
        insta = insta[1]
        insta = "http://www.instagram.com/" + insta
    else:
        insta = "N/A"

    # TAIL DELIMITERS

    if insta.count('">') > 0:
        insta = insta.split('">', 1)
        insta = insta[0]
    if insta.count('?') > 0:
        insta = insta.split('?', 1)
        insta = insta[0]
    if insta.count('"') > 0:
        insta = insta.split('"', 1)
        insta = insta[0]
    else:
        pass

    return facebook, insta
