# How to send mailchimp email

1. install hvopen_tools
   - virtualenv -p python3 .venv
   - source .venv/bin/activate
   - pip install -U ./hvopen_tools

2. Get mailchimp API key
   - log into mailchimp
   - get your api key
   - `export MC_KEY=<mailchimp key>`

3. Run mailchimp sync
   - `mailchimp-sync _events/<year>/<eventfile>`

4. Complete campaign
   - log back into mailchimp
   - find the campaign in draft format and edit
   - fill in audience
   - fill in subject line
   - fill in from
   - check design in case there were formatting issues with sync

5. Send test email
   - send a test email to yourself, or a few people

6. Set to post to social
   - add posting to facebook
   - add posting to twitter
   - in both casses you should add a picture if you can, it gets more
     hits

7. Schedule campaign
   - Typically you should send out the first email 10 days before the
     event. Schedule it for 7:30am or 4:30pm.

8. Schedule reminder
   - Copy the campaign
   - Schedule the new campaign for the Monday before the event
   - Again, 7:30am or 4:30pm seem to be ideal send times.
