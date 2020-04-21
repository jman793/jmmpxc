from requests_oauthlib import OAuth2Session

#This function does not work based on its own you would need to register a github web app and then change the your_id and secret variabels
def github():
    your_id = 'This would be given by the github application you register' 
    secret = 'This would be given by the github app'

    #these are used by github and done on githubs backend
    auth_first_url = 'https://github.com/login/oauth/authorize'
    token_url = 'https://github.com/login/oauth/access_token'

    github = OAuth2Session(your_id)


    auth_url, current_state = github.authorization_url(auth_first_url)
    print 'This url needs to be authorized', authorization_url


    redirect_response = raw_input('Copy and paste the URL you were redirected to.')

    # Grab access token from Github
    github.fetch_token(token_url, client_secret=secret, authorization_response=redirect_response)

    # Now you can use the .get method to grab to use the github api to grab data

#This does not work without registering an app on the google cloud platform but could be used as boilerplate for an Oauth sign on
def google():
    your_id="This would be given by the google app"
    secret="This would be given by the app"
    
    redirect_url="This is the regestered callback url"

    auth_base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    #this token would be given by the project
    token_url = "https://www.googleapis.com/oauth2/v4/your_token"
    #This variable is used to let the google api know what you want to access
    scope = ["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"]

    authorization_url, state = google.authorization_url(auth_base_url, access_type="offline", prompt="select_account")
    print 'Please authorize,', authorization_url

    redirect_response = raw_input('Copy and paste the URL you were redirected to.')

    google.fetch_token(token_url, client_secret=secret, authorization_response=redirect_response)

    #Now you can use the .get method to fetch things like user profiles
