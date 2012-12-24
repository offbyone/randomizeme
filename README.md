randomizeme
===========

iTunes Playlists, made by others

Accounts
========

Created using Twitter or Facebook; account is linked to an email provided afer auth.

Data
====

Playlists stored in Redis; parsed into artist/album/song indices

User Stories
============

### New user to upload
1. landing page
2. not logged in
3. link to login page with twitter or facebook chooser
4. hand off to oauth
5. return to site with token
6. store token in session
7. redirect to library upload page

### New user to create mix
1. deep link directly to user
2. not logged in
3. playlist chooser
4. playlist is mentioned to the user when next they log in.

### Existing user to create mix for specific user
1. deep link directly to user
2. playlist chooser
3. option to save mix
4. option to notify user of the mix
5. mix is shown to user when next they log in.

### Existing user to create mix for other user
1. search libraries by artist/album/song
2. playlist chooser
3. option to save mix
4. option to notify user of the mix
5. mix is shown to user when next they log in.

### Existing user downloads mix lists
1. see notification
2. download playlist m3u
