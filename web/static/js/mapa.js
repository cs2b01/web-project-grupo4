function initMap() {
    
    var map;

    var limites = {
    north: -12.133432,
    south: -12.139371,
    west: -77.022687,
    east: -77.018599
    };

    var markers = [
      ['UTEC - piso 2', -12.135601, -77.022506],
      ['UTEC - Piso 6', -12.135486, -77.022223],
      ['Salomé', -12.137139,  -77.020528],
      ['Rincon Torrepa', -12.136653, -77.020507],
      ['Menu de casa', -12.135239, -77.020970],
      ['D Lucas', -12.135619, -77.021855],
    ];

    //InfoWindow de cada marcador
    var infoWindowContent = [];

    var markerContent = (restName) => {
      var cadena = ['<div class="info_content">' +
        '<h3>' + restName +'</h3>' + '<p>3 opciones de menú</p>'+
        '<a href="/static/'+ restName.replace(/ /g, "") +'.html">Ver menu</a>'];
      return cadena;
    }

    for (var i = 0; i < markers.length; i++) {
      infoWindowContent.push(markerContent(markers[i][0]));
    }

    var infoWindow = new google.maps.InfoWindow(), marker, i;

    map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: -12.136288, lng: -77.021351},
      restriction: {
        latLngBounds: limites,
        strictBounds: false
      },
      zoom: 18,
      disableDefaultUI: true
    });

    map.setOptions({styles: styles['default']});

    //Genera los marcadores con sus respectivos infoWindows
    for( i = 0; i < markers.length; i++ ){
      var position = new google.maps.LatLng(markers[i][1], markers[i][2]);
      var marker = new google.maps.Marker({
        position: position,
        map: map,
        title: markers[i][0]
      });

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
            infoWindow.setContent(infoWindowContent[i][0]);
            infoWindow.open(map, marker);
        }
        })(marker, i));

      marker.setMap(map);
    }
}

var styles = {
        default: [
            {
            featureType: 'poi.business',
            stylers: [{visibility: 'off'}]
          },
          {
            featureType: 'transit',
            elementType: 'labels.icon',
            stylers: [{visibility: 'off'}]
          }
        ],
};

google.maps.event.addDomListener(window, 'load', initialize);