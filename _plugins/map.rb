# coding: utf-8

module Jekyll
  class MapTag < Liquid::Tag

    def initialize(tag_name, text, tokens)
      super
      @text = text
    end

    def render(context)
      page = nil
      if @text != ""
        puts "Assigning from text"
        page = context[@text]
      else
        puts "Assigning from page"
        local = context.registers[:page]
        if local["collection"] == "locations"
          page = local
          # TODO(sdague): it would be nice to move the location magic
          # lookup here so that we can just look up, by title, pages
          # that have location attributes without have to assign
          # location on the parent document.
        end
      end

      if page == nil
        puts "ERROR: no location information found"
        return ""
      end

      Jekyll.logger.debug "Adding Map: ", page.url

      popup = "<b>#{page["title"]}</b>"
      if page["subtitle"]
        popup += "<br>#{page["subtitle"]}"
      end

      parking = ""
      if page["parking"]
        parking = "var parking = L.marker(#{page["parking"]}, {icon: myIcon}).addTo(mymap);"
      end

      <<-MAP
<div id="mapid" class="location-map"></div>
 <script language="javascript">
    var mymap = L.map('mapid').setView([#{page["lat"]}, #{page["lon"]}], 16);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1Ijoic2RhZ3VlIiwiYSI6ImNqZW1vdjQ0bDBuYm4zM3FtMmg2NWluYjAifQ.IMna_1cRxM3XgrXUn2QxGQ'
    }).addTo(mymap);
  var marker = L.marker([#{page["lat"]}, #{page["lon"]}]).addTo(mymap);
  marker.bindPopup("#{popup}").openPopup();

  var myIcon = L.icon({
      iconUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Parking_icon.svg/32px-Parking_icon.svg.png',
      iconSize: [32, 32],
      iconAnchor: [32, 32],
      popupAnchor: [-3, -76],
  });
  #{parking}
 </script>

        MAP
    end
  end
end

Liquid::Template.register_tag('map', Jekyll::MapTag)
