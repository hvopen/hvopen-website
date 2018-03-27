---
layout: post
title: "The New HVOpen Website"
date: 2018-03-26 15:00:00 -0400
excerpt_separator: <!--more-->
---

As part of the rebranding to HVOpen it was time to simplify the
platform for the website at the same time. I had a few requirements
going into this.

* There had to be a way to sync to meetup
* It should be mobile friendly
* The server costs to maintain should be low

<!--more-->

The 3rd genetation of the website was based on Drupal, which worked
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

### Dive into Jekyll ###

Jekyll is a static site generator written in Ruby. One of the more
well known in the space. The source is a bunch of annotated markdown
files, then it compiles HTML out of it. Like any compiler, you pay a
cost up front for that, so builds take noticable time (especially once
you import the 180 old events). However, that build time means a quite
quick website on the other side.

It took about a week to find a base theme that worked for me. I needed
a relatively un-adulterated bootstrap theme. That would give me a
responsive base to work from.

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

### Extending Jekyll ###

It was suggested that I look at a couple of other
