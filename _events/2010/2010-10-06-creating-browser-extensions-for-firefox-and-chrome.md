---
dtend: 2010-10-06 20:00:00 -0400
dtstart: 2010-10-06 18:00:00 -0400
location: Mid Hudson Library System Auditorium
mhvlug_url: /meetings/2010/creating-browser-extensions-for-firefox-and-chrome
presenter: Kris Walker
title: Creating Browser Extensions for Firefox and Chrome
type: meeting
---


<img align="right" width="400" hspace="5" height="321" alt="Firefox Addons (courtesy of sockrotation on flickr)" src="/sites/default/files/2722706523_99a3686dba.jpg" />Browser extensions offer a way for linux users to build and distribute useful applications to a wide (cross platform) audience using open source tools. Two browsers in particular lend themselves well to extension development -- Mozilla's Firefox and Google's Chromium.

Because of Mozilla's XPCOM system (Cross Platform Component Object Modeling -- similar to Microsoft's COM system), Firefox essentially gives you access to the full capabilities of the host OS. Firefox itself it based on XPCOM and exposes the entire Mozilla platform to extension developers. This is a powerful platform for building user facing applications, even those that are not "webby".

On the other hand, the extension API for Chromium is much less powerful, but much easier to grok. It walls off developers from the OS, so extensions almost have to be networked and "webby". Nevertheless, Google has made it so easy to build extensions for Chromium that it's hard to ignore.

We'll go over the structure of the Mozilla Platform and XPCOM enough to learn how it works and get our bearings. Although we will not be demonstrating the creation of an XPCOM component, we'll review how it is done in C++, JavaScript, and even Python. Then we'll go over the JavaScript API to XPCOM, and briefly mention the binding for Python as well.  With a grasp on XPCOM we'll skip ahead a little bit and explore XUL, Mozilla's XML user interface markup language.

With XPCOM and XUL under our belts we'll stitch together a GUI build tool with JavaScript.  If all goes well we'll move into the much simpler JavaScript interface for Chromium. There are a few basic concepts to understand first, like the walled sandboxes, but after that it's a simple matter of finding our way around the JavaScript API. Given some time, we'll build the same GUI build tool on the Chromium platform as well.

### Lightning Talks

In lieu of lightning talks this month, Sean's going to talk a bit about the existing [MHVLUG Officers](/content/officer-roles) proposal on the table, and drive a bit of discussion around that subject.  This will start at around 6:00 and run till 6:30ish when the main lecture will start.

### Presenter's Materials

[Presentation](http://www.kixx.name/presentations/browser_extensions.html)<br />[Interesting Links](http://www.delicious.com/kristoffwalk/browser.extension.talk)