module Jekyll
  class LocationChild < Generator
    safe true
    priority :highest

    def generate(site)
      @locations = {}
      locations = site.collections["locations"]
      locations.docs.each do |loc|
        loc.data["addr_html"] = self.address(loc)
        @locations[loc.data["title"]] = loc
      end

      events = site.collections["events"]
      events.docs.each do |event|
        location = @locations[event.data["location"]]
        if location
          event.data["locobj"] = location
        end
      end
    end

    def address(location)
      address = ""
      if location.data["subtitle"]
        address += "#{location.data["subtitle"]}<br/>"
      end
      if location.data["address"]
        address += "\n#{location.data["address"]}<br/>"
      end
      if location.data["address1"]
        address += "\n#{location.data["address1"]}<br/>"
      end
      if location.data["city"]
        address += "\n#{location.data["city"]}"
      end
      if location.data["state"]
        address += ", #{location.data["state"]}"
      end
      if location.data["zip"]
        address += " #{location.data["zip"]}"
      end
      return address
    end
  end
end
