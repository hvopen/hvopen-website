require 'icalendar'

module Jekyll

  class CalendarGenerator < Generator
    safe true

    def generate(site)
      cal = Icalendar::Calendar.new
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

      events.docs.each do |event|
        if event.respond_to?(:meetup_id)
            cal.event do |e|
             e.dtstart = Icalendar::Values::DateTime.new event.dtstart, 'tzid' => "America/New_York"
             e.dtend = Icalendar::Values::DateTime.new event.dtend, 'tzid' => "America/New_York"
             e.summary = event.title
             e.description = event.content
             e.uid = "calendar.#{event.slug}-#{event.meetup_id}@hvopen.org"
             e.url = "https://hvopen.org#{event.url}"
             e.dtstamp = Time.new.strftime("%Y%m%dT%H:%M:%S")
           end
        end
      end


      file = File.new(File.join(site.source, "events.ics"), "w")
      puts cal.to_ical
      file.write(cal.to_ical)
      file.close()

      site.static_files << Jekyll::StaticFile.new(site, site.source, "/", "events.ics")
    end
  end
end
