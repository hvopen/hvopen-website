# coding: utf-8
module Jekyll
  class MapTag < Liquid::Tag

    def initialize(tag_name, text, tokens)
      super
      @text = text
    end

    def render(context)
      <<-MAP
<div>#{@text} Why </div>
<div id="mapid" class="location-map"></div>
 <script language="javascript">
    var mymap = L.map('mapid').setView([41.68790, -73.8968], 16);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1Ijoic2RhZ3VlIiwiYSI6ImNqZW1vdjQ0bDBuYm4zM3FtMmg2NWluYjAifQ.IMna_1cRxM3XgrXUn2QxGQ'
    }).addTo(mymap);
  var marker = L.marker([41.6879, -73.8968]).addTo(mymap);
  marker.bindPopup("<b>300 Rockefeller Hall</b><br>3rd Floor Auditorium").openPopup();

  var myIcon = L.icon({
      iconUrl: 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Parking_icon.svg/32px-Parking_icon.svg.png',
      iconSize: [32, 32],
      iconAnchor: [22, 94],
      popupAnchor: [-3, -76],
  });
  var parking = L.marker([41.6896, -73.8970], {icon: myIcon}).addTo(mymap);
 </script>

        MAP
    end
  end
end

Liquid::Template.register_tag('map', Jekyll::MapTag)
