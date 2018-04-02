# HV Open Plugins #

There are a few custom plugins to make the site easier to
consume. This is an explanation of them.

## location ##

We have over 180 events in the site, however we have a relatively
small number of locations where we doing things. It's important that
every event specifies it's location, but it's easier to do that by
reference.

Very early in the rendering process we use the `event.location` field
to lookup a `location`, and provide the entire `location` document as
the `event.locobj` field. We also render the location address as
`location.addr_html` so that it can be included in documents. This
simplifies a lot of logic that you'd have to do with jekyll tags.

## map ##

I'm very visual, so I think that locations should have maps. The map
plugin is jekyll tag that renders a leaflet.js field. It only works on
`location` pages as it uses `page.context` magic.

## cal ##

This creates a top level `events.ics` file from all the events in the
site. This can be consumed by other services for structured
information on events.

## netlify_redirect ##

This is a mixin to the `jekyll-redirect-from` plugin that changes it's
output format to be a netlify `_redirects` file. This is much faster
to render than ~ 200 redirect pages, and it is more crawler friendly.
