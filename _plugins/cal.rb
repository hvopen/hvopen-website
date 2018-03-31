require 'icalendar'

module Icalendar
  class Event
    optional_single_property :x_alt_desc
  end
end

class PageWithoutAFile < Jekyll::Page
  def read_yaml(*)
    @data ||= {}
  end
end

module Jekyll
  class CalendarGenerator < Generator
    safe true

    def location(site, location)
      address = "#{location.data["title"]}"
      if defined? location.data["subtitle"]
        address += "\n#{location.data["subtitle"]}"
      end
      if defined? location.data["address"]
        address += "\n#{location.data["address"]}"
      end
      if defined? location.data["address1"]
        address += "\n#{location.data["address1"]}"
      end
      if defined? location.data["city"]
        address += "\n#{location.data["city"]}"
      end
      if defined? location.data["state"]
        address += ", #{location.data["state"]}"
      end
      if defined? location.data["zip"]
        address += " #{location.data["zip"]}"
      end
      return address
    end

    def generate(site)
      cal = Icalendar::Calendar.new
      cal.x_wr_calname = "HVOpen Events Calendar"

      cal.timezone do |t|
        t.tzid = "America/New_York"

        t.daylight do |d|
          d.tzoffsetfrom = "-0500"
          d.tzoffsetto   = "-0400"
          d.tzname       = "EDT"
          d.dtstart      = "19700308T020000"
          d.rrule        = "FREQ=YEARLY;BYMONTH=3;BYDAY=2SU"
        end

        t.standard do |s|
          s.tzoffsetfrom = "-0400"
          s.tzoffsetto   = "-0500"
          s.tzname       = "EST"
          s.dtstart      = "19701101T020000"
          s.rrule        = "FREQ=YEARLY;BYMONTH=11;BYDAY=1SU"
        end
      end

      events = site.collections["events"]
      converter = site.find_converter_instance(Jekyll::Converters::Markdown)

      events.docs.each do |event|
        if event.respond_to?(:meetup_id)
          html = converter.convert(event.content)
          cal.event do |e|
            e.dtstart = Icalendar::Values::DateTime.new event.data["dtstart"], 'tzid' => "America/New_York"
            e.dtend = Icalendar::Values::DateTime.new event.data["dtend"], 'tzid' => "America/New_York"
            e.summary = event.data["title"]
            e.description = event.content
            e.uid = "calendar.#{event.data["slug"]}-#{event.data["meetup_id"]}@hvopen.org"
            e.url = "https://hvopen.org#{event.url}"
            e.location = self.location(site, event.data["locobj"])
            e.dtstamp = Time.new.strftime("%Y%m%dT%H%M%S")
            e.x_alt_desc = html
            e.x_alt_desc.ical_param('fmttype', "text/html")
          end
        end
      end

      page = PageWithoutAFile.new(site, "", "", "events.ics")
      page.content = cal.to_ical
      page.data["layout"] = nil
      site.pages << page
    end
  end
end
