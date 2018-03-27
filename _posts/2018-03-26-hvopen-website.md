---
layout: post
title: "The New HVOpen Website"
date: 2018-03-26 15:00:00 -0400
excerpt_separator: <!--more-->
---

As part of the rebranding to HVOpen it was time to simplify the
platform for the website at the same time. I had a few requirements
going into this.

* There had to be a way to sync to meetup. I hate double data entry.
* It should be mobile friendly / responsive.
* The server costs to maintain should be low. That's both hardware
  resources, but also the time it takes to do regular security
  maintenance of the software stack.
* All the old meeting urls had to be maintained (even if through
  redirects). People put these in their resumes showing that they have
  public speaking experience.

<!--more-->

The 3rd generation of the website was based on Drupal, which worked
well for us. But it was started under the idea that more user
generated content would be hosted there. The reality is, that never
really happened. Also, at the time I was maintaining a Drupal site for
the Poughkeepsie Farm Project, but they migrated off of that nearly 5
years ago.

The website really exists to answer the following questions:

* What's the next meeting
* What other events are coming up
* What other institutional memory should we write down so we don't
  forget, and neither do others

I had originally intended to make the 4th generation be based on
Wordpress. I maintain an instance for
my [blog](https://dague.net). Wordpress' auto update functionally
makes staying up to date on security patches easy. But, after
contributing to Home Assistant and Kubernetes docs, I decided to make
a late change and go with Jekyll instead.

## Dive into Jekyll ##

Jekyll is a static site generator written in Ruby. One of the more
well known in the space. The source is a bunch of annotated markdown
files, then it compiles HTML out of it. Like any compiler, you pay a
cost up front for that, so builds take noticable time (especially once
you import the 180 old events). However, that build time means a quite
quick website on the other side.

It took about a week to find a base theme that worked for me. There
are tons of Jekyll themes out there, but most of them focus on blogs,
resumes, or product pages. I needed a relatively un-adulterated
bootstrap theme. I eventually found (Jekyll
Clean)[https://github.com/scotte/jekyll-clean]. The site is a fork of
that respository, though modified enough that it's origins are not
obvious.

I did look at some other static site systems, but two things made my
decision. Jekyll is designed to be extended, not just with custom
tags, but in a number of ways. I've now written 2 plugins for Jekyll
(more below). Secondly, two of the projects I contribute to use
Jekyll, so anything I learn here can be applied there.

### Embracing Jekyll ###

Jekyll has a concept of posts (blog posts) and pages out of the
box. But you can also build custom types via the collections
mechanism. For HVOpen the custom types are `events` and
`locations`.

With the gen3 website, I realized that we only really have about 6
locations we ever do anything in. It's much easier to provide the
information about a location once, and reference it in events. That
means the location page can include a map if people want to drill down
that far. In the gen3 site that was a custom google map, but with the
greater control in gen4 I can use leaflet.js and have pretty maps
based on Open Street Maps.

Events are key. We have 12 meetings a year, 12 lunches a year, 4
leadership meetings, and then sometimes want to cross promote with
other groups. Events drive the front page (what's next, what's
coming). Events also need enough information that we can sync them to
meetup. That means 2 dates (start and end), location field, and
types.

~~~yaml

collections:
  events:
    output: true
    title: Events
    permalink: /:collection/:year/:month/:title
  locations:
    output: true
    title: Locations
    permalink: /:collection/:title

~~~

These custom types live under `_events` and `_locations` in the
repository respectively.

## Extending Jekyll ##

I've written two custom plugins for Jekyll for the hvopen site, one
for mapping, and one for ical.

### Mapping ###

The
[map plugin](https://github.com/hvopen/hvopen-website/blob/master/_plugins/map.rb) is
used on location pages to inject a custom leaflet.js map for those
pages. It's build as a custom tag that you insert in pages (or
layouts) where you want a map.

[![Leaflet.js map](/images/posts/leaflet-map.png "Example of Leaflet")](/locations/300-rockefeller-hall)

In the old system, I had hand crafted a Google Map and embedded it via
an iFrame. Now this can be done by providing enough metadata in a
`location` that it can be rendered on the fly in a leaflet map. That
includes not only the location pin, but the optional parking marker as
well.

Leaflet is backended by [Mapbox](https://www.mapbox.com/), which
uses [Open Street Map](https://www.openstreetmap.org) data.

### Calendar ###

The
[calendar plugin](https://github.com/hvopen/hvopen-website/blob/master/_plugins/cal.rb) provides
an ical feed for upcoming events. That provides a portable way to
export our events to other services. This was a walk back in time to
the ruby icalander gem, which I was once a maintainer.

The calendar plugin is a jekyll generator, which creates a static page
early in the rendering process, that is then copied into the site for
publication. This took a little more effort to figure out, and some
reading of the jekyll source code itself. Examples around generators
are more scarce.

## Lots of Metadata ##

The primary purpose of the website is to make it easy to find out
about upcoming events. One of the ways to do this was to be better
about structured metadata that search engines, social networks, and
message services use. An article from the slack team
about
[unfurling](https://medium.com/slack-developer-blog/everything-you-ever-wanted-to-know-about-unfurling-but-were-afraid-to-ask-or-how-to-make-your-e64b4bb9254) was
rather inspiring there. That means there are open graph and twitter
card tags in every event.

It also means using the [schema.org](http://schema.org/Event) standard
for describing events:

~~~javascript
{
    "@context": "http://schema.org",
    "@type": "Event",
    "location": {
        "@type": "Place",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Poughkeepsie",
            "addressRegion": "NY",
            "postalCode": "12604",
            "streetAddress": "Vassar College"
        },
        "name": "300 Rockefeller Hall 3rd Floor Auditorium"
    },

    "name": "HVOpen Lecture: Unity 3D Development",

    "startDate": "2018-04-04T18:00:00-04:00",
    "endDate": "2018-04-04T20:00:00-04:00"
}
~~~

These are embedded in every event page header and make the pages more
machine friendly. Some of this may start popping up in the way the
site is displayed in google once the great reindexing is done.

## Meetup Sync ##

We started using meetup about 8 years ago as a way to find new
members. Meetup is good about cross promoting events based on
geography and interests. But the last thing I ever wanted to do was
have to enter events into multiple systems. In the gen3 site I wrote a
custom Drupal plugin that updated meetup inside the save hook.

While Jekyll does support custom commands, because of the way this is
hosted (more in a minute), this is always going to be an offline
activity. But it shouldn't be harder than running a simple sync
command. I wrote
a
[sync script](https://github.com/hvopen/hvopen-website/blob/master/meetup-sync.py) in
python.

The script takes a single argument, which is the event source file
that should be synced. If it already has a meetup_id in it's
frontmatter header, this is an update call. If not, it creates the
event, which returns a meetup_id, and rewrites the file with it
included. Meetup posts support a **very** limited set of html (which
does not include header tags or lists), so this does substantial
massaging to make the meetup post be legible.

There is a wrapper shell script that will look through recent git
history for changed events, and call out to the sync script. That will
eventually end up under cron control, though right now it's manual.

## Netlify Hosting ##

In contributing to the Kubernetes Docs I
discovered [Netlify](https://www.netlify.com/). They automate the
process of building static sites like this. Once of their services is
rendering draft output on pull requests, making it much easier to
review documentation pull requests.

But, they also offer hosting for static sites in their CDN
infrastructure. That includes managing SSL certificates
via [letsencrypt](https://letsencrypt.org/), as well as optimizing
assets for faster load. I decided to embrace that, given that if
anything happens with their service we could easily retarget to local
hosting in about 24 hours.

The slideshow for upcoming events is also now hosted in their
infrastructure at [live.hvopen.org](https://live.hvopen.org).

## Migration of Old Content ##

Before hvopen.org went live, I wanted to make sure all the old
meetings were imported, and that their urls from the old site still
worked. I was able to build a json export view of all the old
meetings, and
a
[tool](https://github.com/hvopen/hvopen-website/blob/master/tools/importer.py) which
took that and wrote them out. The trickiest part of this was scrubbing
and converting the html for the posts into reasonable markdown. The
graphical editor for Drupal makes some weird decisions about
whitespace at time that I had to regex clean up.

Maintaining the stable urls is done with
the
[jekyll-redirect-from](https://github.com/jekyll/jekyll-redirect-from)
plugin. The redirects are listed in the frontmatter header, then when
the site is generated it builds a set of redirect pages at all the old
urls. That ensures that anyone who has listed their talk at MHVLUG in
the past in a resume or article won't have a broken link.

Any migration is imperfect. We have not yet moved over older meeting
notes (we probably will) or non meeting events (we probably
won't). There are also some broken images in the old meetings because
not every image file has been brought over. That's going to be a
slower fixing process as we go.

## Contributing ##

The entire website, including all the custom code I talked about, is
up
on [github](https://github.com/hvopen/hvopen-website). Contributions
are welcomed as pull requests, which allow netlify to build the
proposal and make sure it looks right before we merge. If you want to
fix a broken link or a typo or anything else, please do!

## Jekyll thus far ##

It's been a very interesting learning journey thus far. There are
things I love about Jekyll, like how fast the site is to load for
people. It's consistently sub second response now, the best I could
get on the Drupal stack even after pretty aggressive caching was 3 - 4
seconds. I love how extensible it is, and that with the level of
control I have in the templates and plugins it's actually very easy to
get a site to be exactly what I want. Full CMS stacks have so many
layers between content and rendering that it's often hard to get that.

I don't love the build speed for local development, which seems to
have non-linear slow down on the number of events in the system. At
180 events we're at about 4 minutes on a local build (depending on
your hardware). Unfortunately you can't do the render in parallel. I've
worked around that with a `_config_fast.yml` which excludes all events
prior to 2018.

I also found the documentation on Jekyll extremely lacking. The
[plugins page](https://jekyllrb.com/docs/plugins/) talks about the
different kinds of plugins, but typically provides only one very
simple example. Everything I was trying to do was more complicated
than that, so I ended up having to just read a lot of existing jekyll
plugins, and the jekyll source code to figure out how to do
things. It's one of the advantages of open source, I could do that,
but it would have been nicer if I didn't have to.

Also the jekyll docs don't replicate anything in the liquid template
docs, so you typically have to have both pages up in tabs and flip
back and forth between them to build a unified list of tags in your
head. Documentation that's this normalized is easier to maintain, but
much harder to consume.

Overall I'm very happy with this choice, and that when I did need to
extend jekyll I could do it without modifying core code. I also love
how fast it is for users, and will put up with it being a little
slower to build locally for me.
