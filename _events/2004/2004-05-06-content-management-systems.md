---
dtend: 2004-05-06 20:00:00 -0400
dtstart: 2004-05-06 18:00:00 -0400
location: Mid Hudson Library System Auditorium
mhvlug_url: /meetings/2004/content-management-systems
presenter: Alan Snyder
redirect_from:
- /meetings/2004/content-management-systems
title: Content Management Systems
type: meeting
---


Alan Snyder presented "Open Source Content Management Systems". He introduced the concept of using a Content Management System (CMS) for managing a website, and the pros and cons versus more traditional methods. There were also demos of several popular CMS's.

***My presentation notes are below (please bear in mind this is done from memory...)***

<a name="CMS_Introduction" id="CMS_Introduction"></a>

###  CMS Introduction 

I wanted to cover true CMS packages, and not authoring tools nor scripting methods, both of which I introduced during the first part of my presentation. Therefore, the definition of a "CMS" that I used (and will use now to cover what I'll be describing later on) is a server-side software package which enables user(s) to easily create, manage, and maintain content (pages, blogs, forums, documents, images, etc.) for a web site. This is a broad definition but I think it's a legitimate description of what a CMS is and does. For my presentation, I focused on Open Source CMS packages. Be aware that there are a number of proprietary and/or commercial CMS packages available for purchase. I won't discuss these any further.

Let's continue...

<a name="Quick_Overview" id="Quick_Overview"></a>

###  Quick Overview 

What are CMS's used for? Well, here's the more popular uses for a CMS system...
- Blogs
- Forums - think support pages and such
- Wikis (FYI - this site runs on a CMS package known as "MoinMoin" [http://moinmoin.wikiwikiweb.de/](http://moinmo.in/))
- Static Pages (i.e. home pages, corporate pages, informational pages, etc.)
- Frequently Asked Questions (FAQ's)
- Image Galleries
- File storage and organization
- Store Front
- ... and much ***much*** more!

In fact, CMS systems as a whole can do probably anything you're looking to do. It's most likely a matter of finding the right CMS package for your needs and tailoring it as desired. We'll talk about finding CMS packages and customizing them later on. For now, let's see if we can define what it is you need to look for in a CMS system.

<a name="Features" id="Features"></a>

####  Features 

Before you choose a CMS system, you should at least have a basic set of requirements for what you need your site to do. Will it be just a blog? Will it have one home page and some static pages, like a corporate site? Will it need full-blown user support with wikis, forums, chat, personal home pages, workflow, approval processes, and so on. You should make a checklist for yourself of all the features that you'd like to have on your site. Keep in mind that some CMS's ***don't*** allow you to add new features. Most do, but not all. The more comprehensive packages allow you to either turn on/off features as you see fit, and some let you download 'plug-ins' and additional components to give your site more flexibility. The system you choose plays a very critical part in how much you can expand your site (if you even want to at all). If you're sure you just need a simple set of static pages, then almost anything will do. If you think you may be getting into managing multiple blogs, or maybe have an e-commerce store front some day, then you probably want to stick with the more feature-rich systems.

<a name="Hardware_and_Software_Requirements" id="Hardware_and_Software_Requirements"></a>

####  Hardware and Software Requirements 

The majority of open source CMS systems run on the standard LAMP stack (Linux, Apache, [MySQL](http://old.mhvlug.org/MonthlyMeetings/2004/05?title=MySQL&amp;action=edit&amp;redlink=1) (and even [PostgreSQL](http://old.mhvlug.org/MonthlyMeetings/2004/05?title=PostgreSQL&amp;action=edit&amp;redlink=1)), and PHP/Perl/Python). It is a very rare bird to find one that doesn't run on this. The biggest factors that will drive the hardware and software you'll need to host your site will be...
- Feature set
- Number of users
- Storage and growth rate of your site
- Responsiveness (i.e. speed)
- Complexity (i.e. redundancy, failover, etc.)

For this article, I'll only focus on the first three. Responsiveness (tweaking your setup for speed) and overall complexity are really topics for another talk. <overstatement-of-the-day> As a general rule of thumb, the bigger and more complex the site, the more hardware you're gonna need. :) </overstatement-of-the-day>

In terms of the langauges used to write the CMS itself (the "P" in LAMP) - you should choose a CMS that fits your needs and your skills. By "skills" I mean ability to not only configure and install the CMS itself (which is usually a straight-forward case of reading the README file - RTFM!), but also the ability to customize and personalize it for your needs. When it comes to the langauge that a CMS is written in, it really only becomes important when you want to peek behind the scenes and maybe change something that the package itself doesn't provide an interface or configuration file for doing. With this in mind, if you don't want to touch any code on the back end (which is not really as scary as it may sound), then look for a package that has an extensive configuration GUI. Otherwise, you can keep your options more open and if you're willing to roll up your sleeves and dive in, you can go with pretty much anything.

***Advice***: *The most popular language used to write the Open Source CMS's is without a doubt PHP. If you plan on doing any sort of advanced administration on your site, it is well worth your time to learn PHP. In fact, it's worth the time to learn at least the basics of whatever language was used to write the CMS you choose.*

***Choosing a CMS***

There are over one hundred Open Source CMS packages available on the Internet. If you google for "Open Source" "Content Management Systems" (the quotes are important because they tell google to find those exact phrases paired together), you'll find that the very first search result is this site [http://www.la-grange.net/cms](http://www.la-grange.net/cms) which does a pretty good job of listing about 90 CMS systems of all kinds and gives a very brief description of what each does (some more brief than others, but overall a nice start). I recommend this site for newbies looking for a good breadth of what CMS systems are out there.

Another site with good CMS links and resources is [http://www.opensourcecms.com](http://www.opensourcecms.com). This site does a tremendous job of organizing and categorizing CMS systems. Not to mention, the site itself is very professional looking and is in fact run by a CMS system called 'Mambo' which can be found at [http://www.mambocms.com](http://www.mambocms.com). The site lists all of the major Open Source CMS packages as well as screen shots of what each looks like (for most packages anyway), and what the package's home page itself says about that CMS. Additionally, users can post feed-back and rate each CMS on a scale from 1 to 10. This site is the closest I've seen to being ***the*** comprehensive summary of CMS systems.

A Time to Play

Regardless of how you search for a CMS package, you should now have some basic requirements in your mind that you'd like to have for your site, and also some idea of the hardware and software that you'll need to get your site up and running. After perousing google, and the sites listed in this section, you should narrow your choices down to maybe 2-5 different packages that you think will suit your needs. From this set of candidate packages, go to each of their web sites, and join the mailing lists. Spend about a week or even two talking with users and others about what they like most and what they dislike most about each package. Invariably, someone has tried all the packages that you've selected as candidates to use and they will be able to guide you more to your final choice.

Also, more often than not, the home page for a particular CMS package will be created and hosted by that CMS package itself. So, if you want to see what a CMS looks like 'in action' you can usually just go to that package's web site. Some sites even let you play with your personal preference settings like layouts, color schemes, fonts, etc. Take advantage of this. CMS packages have come a very long way and provide you with a ton of options for configuration and layout schemes. Choosing one is very much a matter of personal taste mixed with functional requirements. Choose the one that you feel will best suit your site.

***Advice***: *Don't be afraid to take chances and especially to make mistakes. It may take a few months to get your site to be just the way you want it. You may even go through 3 or 4 different packages and setups before you find the one that suits you best. I can personally attest to about 6 months of trying out different packages and features and learning before I could really decide on what package suited me for my needs. Learning is a very important part of the journey of finding the right system for your site. Have fun with it and play as much as you can. In the long run, you'll be glad you did.*

***What can $that_cms do?***

I've personally used a few of the more popular systems out there, and I host and admin a few also. So, I can speak with some semblance of authority on these packages. Here, I'll just outline quickly what each of the packages I have experience with can do and for the ones I don't have experience with, I'll just summarize them as best possible. Consider this a cheat-sheet for your research.

***Legend***
- UPG = Upgradable, meaning the package allows you to download new functional features as "modules" or "components".
- TH = Themable, meaning you can choose different color schemes for personalization.
- SK = Skinnable, meaning you can change the physical layout of the site by moving sections around, changing the order of things, etc.
|CMS System Name|Features|Expandability|Software Requirements|The Good|The Bad| 
|[Tiki Wiki](http://tiki.org/)|Blog, Forums, FAQ's, Directories, Image Galleries, File Galleries, Search, Workflow,|TH, SK|LAMP|Easy to use, easy to setup, well-written documentation and scripts. Great support community|I got hacked into through a vulnerability in this package. It's been fixed, but that incident left a sting.| 
|[Blog::CMS](http://blogcms.com)|Blog|TH, SK|LAMP|Fairly simple to use blog. Nice layout and scheme. Lots of advanced blog features.|Limited to blog only functionality. More difficult for newbies| 
|[Drupal](http://drupal.org)|Blogs, Forums, Pages, Polls, Stories, Book collaboration, taxonomies|UPG, TH, SK|LAMP|Simple, elegant layout. Easy to use controls and configuration. Very readable and user-friendly. Extensive set of features.|Nothing really. The feature set and ease of use meet its goals of being an easy to use and feature rich CMS system.| 
|Mambo|Blog, News, Stories, FAQ|UPG, TH, SK|LAMP|Extremely professional looking, very graphics intensive, geared towards high-end users and requirements. Very expandable and flexible|Not for beginners (that's not necessarily a bad though). Learning curve is a bit high| 
|[Zope](http://www.zope.org)|Zope is not a CMS system in and of itself. It's more of a framework on top of which CMS's (like [Plone](http://www.plone.org)) are built.|UPG, TH, SK|MySQL, Postgres, Python|Phenomenal programmability, scriptable, excellent foundation for custom CMS sites (i.e. if you wanted to build your own eBay or other custom site).|Extremely high learning curve, but well worth it for custom or complicated sites| 
|[Plone](http://www.plone.org)|Plone is a CMS built on top of the Zope framework. Out of the box it supports forums, documents, workflow, and a few other features.|UPG, TH, SK|MySQL, Postgres, Python, Zope|All the benefits of Zope above, but with a nice, easy to use interface. Plone is more of a document management system than an all-purpose CMS. Smaller learning curve than Zope. Well suited for high-end sites requiring extreme customization.|Very much over-kill for a basic CMS site. Fairly high learning curve - Zope understanding is very helpful but not required.| 
|WordPress|WordPress is an extremely popular blogging system. It's extremely easy to use and install and includes all the necessities for blogging - nothing more.|UPG, TH, SK|MySQL, PHP|Simple. Small footprint. Very well supported. Over 200 themes and skins available.|Not very expandable, but for just a blog system, this is highly recommended!| 

There are plenty more CMS systems out there as I've indicated earlier. An exhaustive summary list would be very difficult to put together, so I encourage you to browse the web using the resources above to find exactly what you're looking for.