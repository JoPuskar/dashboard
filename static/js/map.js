
		console.log("Top Map");
		map = L.map("map", {
				center: [28.169000, 85.014803],
				zoom: 9
		});
		
		//map.options.minZoom = 14;
		
		var osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
			attribution: '&copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
		});
		
		googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
			maxZoom: 20,
			subdomains:['mt0','mt1','mt2','mt3']
		});
		googleHybrid = L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
			maxZoom: 20,
			subdomains:['mt0','mt1','mt2','mt3']
		});
		googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
			maxZoom: 20,
			subdomains:['mt0','mt1','mt2','mt3']
		});
		googleTerrain = L.tileLayer('http://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',{
			maxZoom: 20,
			subdomains:['mt0','mt1','mt2','mt3']
		});
		var none = "";
		var baseLayers = {
			"OpenStreetMap": osm,
			"Google Streets": googleStreets,
			"Google Hybrid": googleHybrid,
			"Google Satellite": googleSat,
			"Google Terrain": googleTerrain,
			"None": none
		};
		
		//map.addLayer(osm);
		layerswitcher = L.control.layers(baseLayers, {}, {collapsed: true}).addTo(map);
		


		// control that shows state info on hover
	var info = L.control();

	info.onAdd = function (map) {
		this._div = L.DomUtil.create('div', 'info');
		this.update();
		return this._div;
	};

	info.update = function (props) {
		this._div.innerHTML = (props ? '<b>' + props.FIRST_GaPa+' '+  
			 props.FIRST_Type + '</b><br />' + props.completed + '% Completed'
			: 'Hover over a municipality');
	};

	info.addTo(map);


	// get color depending on population density value
	function getColor(d) {
		return d > 80 ? '#2c7a9e' :
				d > 60  ? '#55b4e0' :
				d > 40  ? '#7ac4e6' :
				d > 20  ? '#98cfe8' :
							'#b5d0dc' ;
	
	}

	function style(layer) {
		console.log(layer);
		return {
			weight: 2,
			opacity: 1,
			color: 'white',
			//dashArray: '3',
			fillOpacity: 0.7,
			fillColor: getColor(layer.feature.properties.completed)
		};
	}



	L.TopoJSON = L.GeoJSON.extend({  
	  addData: function(jsonData) {    
	    if (jsonData.type === "Topology") {
	      for (key in jsonData.objects) {
	        geojson = topojson.feature(jsonData, jsonData.objects[key]);
	        L.GeoJSON.prototype.addData.call(this, geojson);
	      }
	    }    
	    else {
	      L.GeoJSON.prototype.addData.call(this, jsonData);
	    }
	  }
	});

	var district = new L.TopoJSON();
	$.getJSON(district_json)
	  .done(addTopoData);

	function addTopoData(topoData){
	  district.addData(topoData);
	  district.addTo(map);
	  district.eachLayer(handleLayer);
	  //map.fitBounds(district.getBounds());
	}

	function handleLayer(layer)
	{  

		// set some self explanatory attributes
		
		if(layer.feature.properties.DISTRICT == "GORKHA" || layer.feature.properties.DISTRICT == "NUWAKOT"){
			layer.setStyle({
				fillColor : '#00628e',
				fillOpacity: 0.8,
				color:'black',
				weight:1,
				opacity:0.6
			});
			layer.on('mouseover',function(e){//console.log("mousein");
				e.target.setStyle({'weight':'3'});
			}).on('mouseout',function(e){
				e.target.setStyle({'weight':'1'});
			});
		}
		else if(layer.feature.properties.Province == "1"){
			layer.setStyle({
				fillColor : 'red',
				fillOpacity: 0,
				color:'black',
				weight:1,
				opacity:0.6
			});
		}
		else if(layer.feature.properties.Province == "2"){
			layer.setStyle({
				fillColor : 'yellow',
				fillOpacity: 0,
				color:'black',
				weight:1,
				opacity:0.6
			});
		}
		else if(layer.feature.properties.Province == "3"){
			layer.setStyle({
				fillColor : 'green',
				fillOpacity: 0,
				color:'black',
				weight:1,
				opacity:0.6
			});
		}
		else if(layer.feature.properties.Province == "4"){
			layer.setStyle({
				fillColor : 'orange',
				fillOpacity: 0,
				color:'black',
				weight:1,
				opacity:0.6
			});
		}
		else if(layer.feature.properties.Province == "5"){
			layer.setStyle({
				fillColor : 'gray',
				fillOpacity: 0,
				color:'black',
				weight:1,
				opacity:0.6
			});
		}
		else if(layer.feature.properties.Province == "6"){
			layer.setStyle({
				fillColor : 'cyan',
				fillOpacity: 0,
				color:'black',
				weight:1,
				opacity:0.6
			});
		}
		else if(layer.feature.properties.Province == "7"){
			layer.setStyle({
				fillColor : 'magenta',
				fillOpacity: 0,
				color:'black',
				weight:1,
				opacity:0.6
			});
		}


		//console.log(layer);
		/*var popUpContent = "";
            popUpContent += '<table style="width:100%;" id="District-popup" class="popuptable">';
			popUpContent+= "<tr><td>"+layer.feature.properties.DISTRICT+"</td></tr>";
			
            popUpContent += '</table>';
            layer.bindPopup(L.popup({
                closeOnClick: true,
                closeButton: true,
                keepInView: true,
                autoPan: true,
                maxHeight: 200,
                //minWidth: 250
            }).setContent(popUpContent));
*/
		layer.bindLabel(layer.feature.properties.DISTRICT);

        layer.on('click',function(e){
        	loadMunicipality(layer.feature.properties.DISTRICT);

        });
	}

	function loadMunicipality(district){
		if(district == "GORKHA"){

			$("#gorkha").attr("selected","selected");

			if(map.hasLayer(nuwakot)){
				map.removeLayer(nuwakot);
			}
			gorkha = new L.TopoJSON();

			$.getJSON(gorkha_json)
			  .done(addTopoData);

			function addTopoData(munData){  
			  gorkha.addData(munData);
			  gorkha.addTo(map);
			  gorkha.eachLayer(handleMun);
			  map.fitBounds(gorkha.getBounds(),[-50,-50]);
			}	
		}
		else if(district == "NUWAKOT"){

			$("#nuwakot").attr("selected","selected");

			if(map.hasLayer(gorkha)){ console.log("has layer");
				map.removeLayer(gorkha);
			}
			nuwakot = new L.TopoJSON();

			$.getJSON(nuwakot_json)
			  .done(addTopoData);

			function addTopoData(munData){  
			  nuwakot.addData(munData);
			  nuwakot.addTo(map);
			  nuwakot.eachLayer(handleMun);
			  map.fitBounds(nuwakot.getBounds());
			}	
		}
	}

	var previousMun = null;

	function handleMun(layer){

		layer.setStyle(style(layer));
		// set some self explanatory attributes
		/*layer.setStyle
		({
			fillColor : '#00628e',
			fillOpacity: 0.8,
			color:'white',
			weight:1,
			opacity:0.9
		});*/

/*
		console.log(layer);
		var popUpContent = "";
            popUpContent += '<table style="width:100%;" id="District-popup" class="popuptable">';
			popUpContent+= "<tr><td>"+layer.feature.properties.FIRST_GaPa+"</td></tr>";
			
            popUpContent += '</table>';
            layer.bindPopup(L.popup({
                closeOnClick: true,
                closeButton: true,
                keepInView: true,
                autoPan: true,
                maxHeight: 200,
                //minWidth: 250
            }).setContent(popUpContent));

*/
		layer.bindLabel(layer.feature.properties.FIRST_GaPa);

        layer.on('click',function(e){

        	map.fitBounds(layer.getBounds());
        	if(previousMun!=null){
        		//previousMun.target.setStyle({'fillColor':'#00628e'});
        	}
        	//e.target.setStyle({'fillColor':'red'});
        	previousMun = e;

        });
        layer.on('mouseover',function(e){console.log("mousein");
			e.target.setStyle({'weight':'3'});
			info.update(layer.feature.properties);
		}).on('mouseout',function(e){
			e.target.setStyle({'weight':'1'});
			info.update();
		});

	}


	$("#inputDistrict").on('change',function(){ console.log("input district");
		console.log($("#inputDistrict option:selected")[0].id);
		if($("#inputDistrict option:selected")[0].id == "gorkha"){
			if(!map.hasLayer(gorkha)){
				loadMunicipality("GORKHA");
			}
			
			if(map.hasLayer(nuwakot)){
				map.removeLayer(nuwakot);
			}
			
		}
		else if($("#inputDistrict option:selected")[0].id == "nuwakot"){
			if(!map.hasLayer(nuwakot)){
				loadMunicipality("NUWAKOT");
			}
			if(map.hasLayer(gorkha)){
				map.removeLayer(gorkha);
			}
			
			
		}
		else{

			map.setView([28.169000, 85.014803],9);

			if(map.hasLayer(gorkha)){
				map.removeLayer(gorkha);
			}
			
			if(map.hasLayer(nuwakot)){
				map.removeLayer(nuwakot);
			}
		}
	});
	





	var legend = L.control({position: 'bottomright'});

	legend.onAdd = function (map) {

		var div = L.DomUtil.create('div', 'info legend'),
			grades = [0, 20, 40, 60, 80],
			labels = [],
			from, to;

		for (var i = 0; i < grades.length; i++) {
			from = grades[i];
			to = grades[i + 1];

			labels.push(
				'<i style="background:' + getColor(from + 1) + '"></i> ' +
				from + (to ? '&ndash;' + to + "%" : '%+'));
		}

		div.innerHTML = labels.join('<br>');
		return div;
	};

	legend.addTo(map);


		