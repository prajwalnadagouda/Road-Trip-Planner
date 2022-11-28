
var count=0;
var map;
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
function callApi(url, img) {
    const xhr = new XMLHttpRequest();
    xhr.responseType = 'json';
    xhr.onreadystatechange = () => {
    if(xhr.readyState === XMLHttpRequest.DONE) {
        results=xhr.response;
        var latdis,longdis;
        var marker;
        var iconOptions = {
            iconUrl: img,
            iconSize: [20, 20]
        }
        var customIcon = L.icon(iconOptions);
        var markerOptions = {icon: customIcon}
        for(var propt in results){
            latdis=results[propt][1];
            longdis=results[propt][2];
           
            var marker=L.marker([latdis,longdis],markerOptions).addTo(map);
            marker.bindPopup(results[propt][0]).openPopup();
        }
        return xhr.response;
    }
    };
    xhr.open('GET',url);
    xhr.send();
}
async function myFunction() {
    if(count>0){
        map.remove();
    }
    count+=1;
    var startaddress = document.getElementById("startcity").value+", CA";
    var endaddress = document.getElementById("endcity").value+", CA";
    var journeydate = document.getElementById("plandate").value;
    console.log(journeydate);
    var slong=0;
    var slat;
    var elong;
    var elat;
    var OpenStreetMapProvider = window.GeoSearch.OpenStreetMapProvider;
    var provider = new OpenStreetMapProvider();
    var results =  provider.search({ query: startaddress});
    results.then(
        function(value) { slong=(value[0].x);  slat=parseFloat(value[0].y);},
        function(error) { console.log(error); }
    );
    results =  provider.search({ query: endaddress});
    results.then(
        function(value) {  elong=parseFloat(value[0].x);  elat=parseFloat(value[0].y);},
        function(error) { console.log(error); }
    );
    await sleep(1000);

    map = L.map('map', {
        center: [(slat+elat)/2, (slong+elong)/2],
        zoom: 6
    });
    // L.Routing.control({ waypoints: [ L.latLng(slat, slong), L.latLng(elat, elong) ] }).addTo(map);
    // console.log((L.Routing.control({ waypoints: [ L.latLng(slat, slong), L.latLng(elat, elong) ] })));

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);
    L.marker([50.5, 30.5]).addTo(map);
    //
    var latlngs;
    if(slat>elat){
        if(slong>elong){latlngs = [[slat+0.4, slong+0.4],[elat-0.4, slong+0.4],[elat-0.4, elong-0.4],[slat+0.4, elong-0.4]];}
        else{latlngs = [[slat+0.4, slong-0.4],[elat-0.4, slong-0.4],[elat-0.4, elong+0.4],[slat+0.4, elong+0.4]];}
    }
    else{
        if(slong>elong){latlngs = [[slat-0.4, slong+0.4],[elat+0.4, slong+0.4],[elat+0.4, elong-0.4],[slat-0.4, elong-0.4]];}
        else{latlngs = [[slat-0.4, slong-0.4],[elat+0.4, slong-0.4],[elat+0.4, elong+0.4],[slat-0.4, elong+0.4]];}
    }
    var polygon = L.polygon(latlngs, {color: 'red'}).addTo(map);

        
    var lat1=(latlngs[0][0]);
    var long1=(latlngs[0][1]);
    var lat2=(latlngs[2][0]);
    var long2=(latlngs[2][1]);
    var extra;
    if(lat1>lat2){ [lat1,lat2]=[lat2,lat1] }
    if(long1>long2){ [long1,long2]=[long2,long1] }
    extra="l1="+lat1+"&l2="+lat2+"&l3="+long1+"&l4="+long2;
    const xhr = new XMLHttpRequest();
    var url = 'http://3.80.152.179/getevents?'+extra+"&date="+journeydate;
    xhr.responseType = 'json';
    xhr.onreadystatechange = () => {
    if(xhr.readyState === XMLHttpRequest.DONE) {
        results=xhr.response;
        var latdis,longdis;
        var marker;
        var iconOptions = {
            iconUrl: './Images/event.png',
            iconSize: [20, 20]
        }
        var customIcon = L.icon(iconOptions);
        var markerOptions = {icon: customIcon}
        for(var propt in results){
            latdis=results[propt][5];
            longdis=results[propt][6];
           
            var marker=L.marker([latdis,longdis],markerOptions).addTo(map);
            marker.bindPopup(results[propt][2]+" at "+results[propt][4]).openPopup();
        }
        return xhr.response;
    }
    };
    xhr.open('GET',url);
    xhr.send();

    var url = 'http://3.80.152.179/getparks?'+extra;
    callApi(url, './Images/park.png')
    var url = 'http://3.80.152.179/getamusementparks?'+extra;
    callApi(url, './Images/amusement.png')
    var url = 'http://3.80.152.179/getmuseums?'+extra;
    callApi(url, './Images/museum.png')
    var url = 'http://3.80.152.179/getfuelstations?'+extra;
    callApi(url, './Images/fuel.png')
    var url = 'http://3.80.152.179/getrestaurants?'+extra;
    callApi(url, './Images/restaurant.png')



    L.Routing.control({ waypoints: [ L.latLng(slat, slong), L.latLng(elat, elong) ] }).addTo(map);
    // map.off();
    // var polygon = L.polygon([slat-1, slong-1],[slat+1, slong+1],[elat-1, elong-1],[elat+1, elong+1]).addTo(map);
    //
    }