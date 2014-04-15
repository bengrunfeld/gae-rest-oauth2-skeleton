# Google Flow Skeleton on GAE

This is a full example of the use of Google's Flow object to take a user
through the OAuth 2.0 process. 

A great API to test it with is [Github's](https://developer.github.com/v3/).

## Google Flow Docs

Enough with the read'ie read'ie. Show me the docs and I'll figure it out by
myself. [docs](https://developers.google.com/api-client-library/python/guide/aaa_oauth#flows)

## Setup

1. Enter secret information into `client_secrets.json`
2. Add `client_secrets.json` to your `.gitignore` file
3. Make sure you add the needed 3rd party libraries to your GAE app somehow
4. Go into `auth.py` and update the `scope` and `redirect_url` on line `33`
5. Build out the rest of your program

## What are Google Flows?

According to Google: 

> The purpose of a Flow class is to acquire credentials that authorize your 
application access to user data.

A simpler explanation would be that Google Flows are a set of functions that
take a user through the steps of the OAuth 2.0 process.

Abstracting the workflow like this means that the programmer doesn't have to
worry about the nuts and bolts of the process, e.g. swapping the temporary code
for an access token.

## So why create a skeleton of the workflow?

Oh boy, there are a couple of answers to this one...

* Putting the pieces together is sometimes difficult and time consuming
* Now you can learn from an example that works
* Don't set it up from scratch every time you create a new app that uses OAuth
* So Google can see how *bling mah shit is*

## Upcoming changes

I'll set this up on appspot so you can see that it actually works. 

## I want to leave a comment

Write something on Github or hit me up on Twitter: [@bengrunfeld](https://twitter.com/bengrunfeld) 
