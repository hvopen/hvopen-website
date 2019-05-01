[![Netlify Status](https://api.netlify.com/api/v1/badges/65a6b143-3534-477c-87a7-26963e22d36c/deploy-status)](https://app.netlify.com/sites/hvopen-org/deploys)

HV Open Website
================

This is the website that
powers [hvopen.org](https://flamboyant-easley-a326bc.netlify.com/). It
is based on
the [Jekyll Clean](https://github.com/scotte/jekyll-clean) project to
provide a [bootstrap](http://getbootstrap.com) based website which is
very clean and easy to shape into what we needed.

Tour of Content
========================

Jekyll content is based on `collections`, which are markdown formatted
documents with some additional metadata. For HV Open we have the
following content types:

* _events - all events (use `type` field to distinguish between
  meetings and other events)
* _locations - so we don't have to copy/paste that bit into every
  event
* _posts - news items


Making Changes
====================

* Fork [hvopen-website](https://github.com/hvopen/hvopen-website)
* Clone locally
* Make changes
* Commit
* Push
* Open a Pull Request

When you open a pull request the site will be built with netlify,
which will provide a rendering of the whole website. That can be
inspected.

Anything that's merged into `master` branch on the `hvopen-website`
will be built by netlify and deployed within a few minutes. Because of
that it's good to stage in PRs first to allow for quick review.

Running Locally
===============

On Debian / Ubuntu installing the local environment is a small number
of steps.

```
$ sudo apt-get install ruby ruby-dev nodejs ruby-bundler
$ cd hvopen-website/
$ bundler install --path vendor/site
```

You can then run a local server to test with:
```
$ bundler exec jekyll serve --future
```

Now browse to http://127.0.0.1:4000

Future is important, because by default jekyll skips content that is
tagged with future dates (lets you write in advance). We use this
feature for out events.

License
=======

The content of this theme is distributed and licensed under a
![License Badge](/images/cc_by_88x31.png)
[Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/legalcode)

    This license lets others distribute, remix, tweak, and build upon your work,
    even commercially, as long as they credit you for the original creation. This
    is the most accommodating of licenses offered. Recommended for maximum
    dissemination and use of licensed materials.

In other words: you can do anything you want with this theme on any site, just please
provide a link to [the original theme on github](https://github.com/scotte/jekyll-clean)
so I get credit for the original design. Beyond that, have at it!

This theme includes the following files which are the properties of their
respective owners:

* js/bootstrap.min.js - [bootstrap](http://getbootstrap.com)
* css/bootstrap.min.css - [bootstrap](http://getbootstrap.com)
* js/jquery.min.js - [jquery](https://jquery.com)
* images/cc_by_88x31.png - [creative commons](https://creativecommons.org)
* css/colorful.css - [iwootten/jekyll-syntax](https://github.com/iwootten/jekyll-syntax)
