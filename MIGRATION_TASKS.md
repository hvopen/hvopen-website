# Migration Tasks #

The majority of HV Open website migration has happened, but there are
a number of more manual things that are needed. Everyone is welcome to
help with these.

## Fix Meeting Pictures ##

Any meetings that had pictures associated with them (e.g. the Swift
meeting had a swif logo), end up with a now broken image link:

```html
<img alt="large_Swift-logo.png"
src="/sites/default/files/large_Swift-logo.png" style="width: 180px;
height: 180px; float: right; margin-left: 5px; margin-right:
5px;"/>Swift is a open-source programming language for iOS, macOS,
Linux, watchOS, and tvOS apps that builds on the best of C and
Objective-C, without the constraints of C compatibility. Swift adopts
safe programming patterns and adds modern features to make programming
easier, more flexible, and more fun. Swift’s clean slate, backed by
the mature and much-loved Cocoa and Cocoa Touch frameworks, is an
opportunity to reimagine how software development works.

```

We instead need the image in the frontmatter portion of the relevant
page. The Kubernetes meeting is a good example:

``` yaml
dtend: 2018-05-02 20:00:00 -0400
dtstart: 2018-05-02 18:00:00 -0400
location: 300 Rockefeller Hall
meetup_id: '247516815'
title: Kubernetes
type: meeting
image: /images/talks/kubernetes_logo.png
image_alt: Kubernetes Logo
---

```

### Checklist for fixing

For each old meeting

* Fetch logo from https://old.mhvlug.org
* Ensure logo size is scaled down to between 200 - 300px wide
* Add logo to images/talks with appropriate naming
  (i.e. swift-logo.png).
* Add `image` and `image_alt` values to frontmatter
* Remove img html tag from markdown
* Submit for github pull request

## Enhance meeting metadata

The following information would be really great to have in our meeting
metadata in the frontmatter:

* speaker
* number of attendees (we typically capture this and add it to the
  associated news item)
* categories / tags:
  https://jekyllrb.com/docs/frontmatter/#predefined-variables-for-posts

This will let us to use this data to help navigate the existing
talks.

## Upload presentations to Internet Archive

We have 1.2 G of digital assets on old.mhvlug.org, which is a mix of
photos and presentations. The presentations are better suited up on
the Internet Archive

(Note: we may want to change the meeting template to make these easier
to find).

### Checklist for fixing

For each old meeting

* Download any attached presentation content from
  https://old.mhvlug.org
  * Note: even if these are up in Google Drive, or some online format,
    it would be great to capture to PDF for long term memory
* Convert to PDF
* Upload to Internet Archive, ensure the Speaker, Date, and Title are
  correct.
* Make sure all presentations are tagged "mhvlug" and "hvopen" to make
  it easy to find the whole collection later
* Edit hvopen markdown files to include links to those presentations
  after the meeting abstract.
