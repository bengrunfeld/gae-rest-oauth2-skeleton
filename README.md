# Google AppEngine REST OAuth2 Skeleton

This is a skeleton app designed for **Google AppEngine** that illustrates how to go through the **OAuth 2.0** process and connect to a **RESTful API** like GitHub's.

## Background

Personally, I found it extremely challenging to put together the pieces of **GAE** and **OAuth 2.0**, and then connect to a **RESTful API**. Documentation was either non-existant or sparse at best. Fighting through it did teach me a lot, but it almost cost me my job due to the time taken. A tutorial for this subject would have taught me the same amount without endangering my steak budget.

## Installation

We're going to set up the app on the [Python Development Server](https://developers.google.com/appengine/docs/python/tools/devserver), and as such will be using `http://localhost:8080` as a redirect URI. NOTE: this isn't best practice and should **never** be used in production. I am doing it here because it's the easiest way to educate new programmers how all the parts work together.

If you are already using `http://localhost:8080` for something, swap this out for another `port` value.

**1.** Download and install the [Python Development Server](https://developers.google.com/appengine/docs/python/tools/devserver) so that you can set this up on a locally.

**2.** Run `git clone git@github.com:bengrunfeld/gae-rest-oauth2-skeleton.git` wherever you want this to live

**3.** Go to Github and register a new application: *Github -> Settings -> Applications -> Register new application*.

**4.** Copy the `Client ID` and `Client Secret`, and set the `Authorization callback URL` to `http://localhost:8080`

**5.** Create a file in the project directory called `client_secrets.json`

It needs to have the following format:

    {
      "web": {
        "client_id": "",
        "client_secret": "",
        "redirect_uris": [""],
        "auth_uri": "https://github.com/login/oauth/authorize",
        "token_uri": "https://github.com/login/oauth/access_token"
      }
    }

**6.** Paste the `Client ID` and `Client Secret` into their respective places, and paste `http://localhost:8080` into `redirect_urls`. The square brackets are necessary.

This next step requires **Virtualenv**, or preferably **VirtualenvWrapper**, as it sets up 3rd party Python libraries not supported by Google AppEngine. 

**7.** Activate your respective Virtualenv or VirtualenvWrapper and `pip install httplib2` and `pip install oauth2client`. Then `pip show` both those packages and copy their locations.

**8.** Create a `lib` directory inside the project directory and create symlinks to the packages with `ln -s path-to-location/httplib2` and `ln -s path-to-location/oauth2client`.

In addition to `sys.path.append("lib")`, these 2 steps allow you to `import` 3rd party libraries not supported by Google. 

**9.** Go to Google AppEngine Launcher and add the project using `File -> Add Existing Application`. Navigate to the project directory, and make sure that the value for `port` is `8080` (unless you're using it for something else). Hit `Run`. Open up the Logs to see what's going on.

## Usage

1. Navigate to `http://localhost:8080`.
2. The app will take you to a dummy Google Accounts login screen. Just hit `Login`.
3. You will be redirected to the Github login page. Enter your credentials and hit `Sign in`.
4. You will be redirected to an **Authorize Application** page. Don't worry, the only person you're giving permissions to is yourself, since you created the Github app in the steps above. Go ahead and authorize the application.
5. You'll be taken to the UI of the app. If your username shows up correctly, it worked. Go pour one out.
6. **IMPORTANT:** If you want to test the app with another user, hit the `Logout` button at the top right of the page. This deletes the access token for the existing user stored in Storage.

## Links to relevant Google Documentation

**Google: OAuth 2.0** – [https://developers.google.com/api-client-library/python/guide/aaa_oauth](https://developers.google.com/api-client-library/python/guide/aaa_oauth)

**client_secrets.json** – [https://developers.google.com/api-client-library/python/guide/aaa_client_secrets](https://developers.google.com/api-client-library/python/guide/aaa_client_secrets)

**StorageByKeyName** – At bottom of doc. [https://developers.google.com/api-client-library/python/guide/google_app_engine](https://developers.google.com/api-client-library/python/guide/google_app_engine)

**URL Fetch** – [https://developers.google.com/appengine/docs/python/urlfetch/](https://developers.google.com/appengine/docs/python/urlfetch/)

**Google Users Service** – [https://developers.google.com/appengine/docs/python/gettingstartedpython27/usingusers](https://developers.google.com/appengine/docs/python/gettingstartedpython27/usingusers)

**Webapp2 Sessions** – [https://webapp-improved.appspot.com/api/webapp2_extras/sessions.html](https://webapp-improved.appspot.com/api/webapp2_extras/sessions.html)

**Github API** – [https://developer.github.com/v3/](https://developer.github.com/v3/)

## I want to leave a comment

Write something on Github or hit me up on Twitter: [@bengrunfeld](https://twitter.com/bengrunfeld). Please **&#9734;Star&#9734;** this project if you like it.