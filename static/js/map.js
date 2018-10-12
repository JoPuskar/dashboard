
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

	info.update = function (props, gapa_status) {
		this._div.innerHTML = (props ? '<b>' + props.FIRST_GaPa+' '+
			 props.FIRST_Type + '</b><br />' + gapa_status + '% Completed'
			: 'Hover over a municipality');
	};

	info.addTo(map);


	// get color depending on population density value
	function getColor(d) {
		return d > 80 ? '#00bd00' :
				d > 60  ? '#e1ff00' :
				d > 40  ? '#ffff00' :
				d > 20  ? '#ffbf00' :
							'#ff8000' ;
	
	}

	function style(layer, completion_status) {
		//console.log(layer);
		var hidegapa = layer.feature.properties.FIRST_GaPa;
		if(hidegapa == "Chum Nubri" || hidegapa == "Sulikot" || hidegapa == "Bhimsen" || hidegapa == "Shivapuri" || hidegapa == "Panchakanya" || hidegapa == "Langtang National Park" || hidegapa == "Shivapuri Watershed and Wildlife Reserve"){
			console.log("change color");
			return {
				weight: 2,
				opacity: 0,
				color: 'black',
				//dashArray: '3',
				fillOpacity: 0,
				fillColor: "#ddd"
			};
		}
		else {
			console.log("dont change color");
			return {
				weight: 2,
				opacity: 1,
				color: 'white',
				//dashArray: '3',
				fillOpacity: 0.7,
				fillColor: getColor(completion_status)
			};
		}


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

	var nepal_district = new L.TopoJSON();
	$.getJSON(district_nepal)
	  .done(addTopoDataDistrict);

	function addTopoDataDistrict(topoData){
	  nepal_district.addData(topoData);
	  nepal_district.addTo(map);
	  nepal_district.eachLayer(handleNepalDistrict);
	  //map.fitBounds(district.getBounds());
	}


	function handleNepalDistrict(layer)
	{
			layer.setStyle({
				fillColor : 'red',
				fillOpacity: 0,
				color:'black',
				weight:1,
				opacity:0.6
			});


		layer.bindLabel(layer.feature.properties.DISTRICT);
		nepal_district.bringToBack();
        layer.on('click',function(e){

			//layer.bindPopup(layer.feature.properties.DISTRICT);


        });
        if(map.hasLayer(district)){
        	//district.bringToFront();
        }
        
	}







	district = new L.TopoJSON();
	$.getJSON(district_json)
	  .done(addTopoData);

	function addTopoData(topoData){
	  district.addData(topoData);
	  setTimeout(function(){
	  		district.addTo(map);
	  }, 1000);

	  district.eachLayer(handleLayer);
	  //map.fitBounds(district.getBounds());
	}




	//extract gorkha and nuwakot layers from whole district layer
		gorkhaLayer = [];
		nuwaLayer = [];
		//end



	function handleLayer(layer)
	{
		//console.log(layer);
		if(layer.feature.properties.DISTRICT == "GORKHA"){
			gorkhaLayer = layer;
			//console.log(layer);
		}
		else if(layer.feature.properties.DISTRICT == "NUWAKOT"){
			nuwaLayer = layer;
		}


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
        	var distSelected = e.target.feature.properties.DISTRICT.toLowerCase();
            if(distSelected == 'gorkha') {
            	nuwaLayer.setStyle({
					fillColor : '#00628e',
					fillOpacity: 0.8,
					color:'black',
					weight:1,
					opacity:0.6
				});

            	//console.log(e.target.feature.properties.DISTRICT.toLowerCase());
            	$("#gorkha").attr("selected","selected");
            	$("#nuwakot").removeAttr("selected");
            	$("#nuwakot-palika-select").css("display","none");
            	$("#gorkha-palika-select").css("display","block");

            	changeOverall(distSelected);

			//show legend and info div
            $('.legend').css('display','block');
            $('.info').css('display','block');

             //add point markers
              stfc_gorkha.addTo(map);
              
              if(map.hasLayer(stfc_nuwakot)){
              	map.removeLayer(stfc_nuwakot);
              }
              
             //add point markers end

            }
			else {

            	gorkhaLayer.setStyle({
					fillColor : '#00628e',
					fillOpacity: 0.8,
					color:'black',
					weight:1,
					opacity:0.6
				});

            	$("#nuwakot").attr("selected","selected");
            	$("#gorkha").removeAttr("selected");
            	$("#gorkha-palika-select").css("display","none");
            	$("#nuwakot-palika-select").css("display","block");
            	changeOverall(distSelected);

            	//show legend and info div
            	$('.legend').css('display','block');
            	$('.info').css('display','block');


             //add point markers
              stfc_nuwakot.addTo(map);
              stfc_nuwakot.bringToFront();
              if(map.hasLayer(stfc_gorkha)){
              	map.removeLayer(stfc_gorkha);
              }
              
             //add point markers end

            }




        });
	}



		function resetStyle(resetcolor){

			//console.log(gorkhaLayer);

			//reset district color after municipality is loaded
			if(resetcolor == "gorkha"){
				gorkhaLayer.setStyle({
					fillColor : '#00628e',
					fillOpacity: 0,
					color:'black',
					weight:1,
					opacity:1
				});
			}
			else if(resetcolor == "nuwakot"){
				nuwaLayer.setStyle({
					fillColor : '#00628e',
					fillOpacity: 0,
					color:'black',
					weight:1,
					opacity:1
				});
			}
		}

	function loadMunicipality(district){

		if(district == "GORKHA"){

			resetStyle("gorkha");


			$("#gorkha").attr("selected","selected");

			if(map.hasLayer(nuwakot)){
				map.removeLayer(nuwakot);
				//setStyle();
			}
			gorkha = new L.TopoJSON();

			$.getJSON(gorkha_json)
			  .done(addTopoData);

			function addTopoData(munData){
			  gorkha.addData(munData);
			  gorkha.addTo(map);
			  gorkha.eachLayer(handleMun);
			  map.fitBounds(gorkha.getBounds(),[-50,-50]);
			  if(map.hasLayer(stfc_gorkha)){
			  	stfc_gorkha.bringToFront();
			  }
			  		  
			  
			}	
		}
		else if(district == "NUWAKOT"){

			resetStyle("nuwakot");

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
			  if(map.hasLayer(stfc_nuwakot)){
			  	stfc_nuwakot.bringToFront();
			  }
			}
		}
	}

	var previousMun = null;
	var previousMunText = "";

	function handleMun(layer){

		var gapa_status = 0;

		if(layer.feature.properties.FIRST_DIST.toLowerCase() == "gorkha") {
			for(var i = 0; i<completion_status_gorkha.length;i++) {
				if(completion_status_gorkha[i][layer.feature.properties.FIRST_GaPa] != undefined) {
                    gapa_status = completion_status_gorkha[i][layer.feature.properties.FIRST_GaPa];
                    //console.log(completion_status_gorkha);
                }
            }
        }
        else {
			for(var i = 0; i<completion_status_nuwakot.length;i++) {
				if(completion_status_nuwakot[i][layer.feature.properties.FIRST_GaPa] != undefined) {
                    gapa_status = completion_status_nuwakot[i][layer.feature.properties.FIRST_GaPa];
                    //console.log(completion_status_nuwakot);
                }
            }
		}

		layer.setStyle(style(layer, gapa_status));
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
        	//console.log(e);

			var clickedMun = e.target.feature.properties.FIRST_GaPa+"_m";
			console.log(e.target.feature.properties);
			if(e.target.feature.properties.FIRST_DIST.toLowerCase() == "gorkha"){

				if(previousMunText != ""){
					var previousElement = document.getElementById(previousMunText.toLowerCase());

					previousElement.removeAttribute("selected");
				}

				var Element = document.getElementById(clickedMun.toLowerCase());

				Element.setAttribute("selected", "selected");
				gorkhaChange(clickedMun.toLowerCase());
				console.log(clickedMun);
				console.log("gorkhachange called");
            	//$("#nuwa-palika-select").css("display","none");
            	//$("#gorkha-palika-select").css("display","block");

				previousMunText = clickedMun.toLowerCase();
			}
			else {

				if(previousMunText != ""){
					var previousElement = document.getElementById(previousMunText.toLowerCase());

					previousElement.removeAttribute("selected");
				}

				var Element = document.getElementById(clickedMun.toLowerCase());
				//console.log(Element);

				Element.setAttribute("selected","selected");
				nuwaChange(clickedMun.toLowerCase());
				console.log("nuwachange called");

				previousMunText = clickedMun.toLowerCase();
			}





        	map.fitBounds(layer.getBounds());
            // $('.col-md-5').hide();
            // $("#" + $(this).val()).show();
        	if(previousMun!=null){
        		previousMun.target.setStyle({'color':'white','weight':1});
        	}
        	e.target.setStyle({'color':'white','weight':6});
        	previousMun = e;



        });
        layer.on('mouseover',function(e){//console.log("mousein munci");
			//e.target.setStyle({'weight':'3'});
			info.update(layer.feature.properties , gapa_status);
		}).on('mouseout',function(e){
			//e.target.setStyle({'weight':'1'});
			info.update();
		});

	}


	$("#inputDistrict").on('change',function(){ //console.log("input district");
		console.log($("#inputDistrict option:selected")[0].id);
		var distSelected = $("#inputDistrict option:selected")[0].id;
		if(distSelected == "gorkha"){
			if(!map.hasLayer(gorkha)){
				loadMunicipality("GORKHA");
			}
			console.log("Test");
			if(map.hasLayer(nuwakot)){
				map.removeLayer(nuwakot);
			}
			map.addLayer(stfc_gorkha);
			if(map.hasLayer(stfc_nuwakot)){ console.log("stfc nuwakot asjdfljaslfjsalfjls");
				map.removeLayer(stfc_nuwakot);
			}



            	nuwaLayer.setStyle({
					fillColor : '#00628e',
					fillOpacity: 0.8,
					color:'black',
					weight:1,
					opacity:0.6
				});

		}
		else if(distSelected == "nuwakot"){
			if(!map.hasLayer(nuwakot)){
				loadMunicipality("NUWAKOT");
			}
			if(map.hasLayer(gorkha)){
				map.removeLayer(gorkha);
			}
			map.addLayer(stfc_nuwakot);
			if(map.hasLayer(stfc_gorkha)){
				map.removeLayer(stfc_gorkha);
			}

			gorkhaLayer.setStyle({
					fillColor : '#00628e',
					fillOpacity: 0.8,
					color:'black',
					weight:1,
					opacity:0.6
				});
			
		}
		else{

			map.setView([28.169000, 85.014803],9);

			if(map.hasLayer(gorkha)){
				map.removeLayer(gorkha);
			}
			
			if(map.hasLayer(nuwakot)){
				map.removeLayer(nuwakot);
			}

			if(map.hasLayer(stfc_nuwakot)){
				map.removeLayer(stfc_nuwakot);
			}
			if(map.hasLayer(stfc_gorkha)){
				map.removeLayer(stfc_gorkha);
			}

			gorkhaLayer.setStyle({
				fillColor : '#00628e',
				fillOpacity: 0.8,
				color:'black',
				weight:1,
				opacity:0.6
			});
			nuwaLayer.setStyle({
				fillColor : '#00628e',
				fillOpacity: 0.8,
				color:'black',
				weight:1,
				opacity:0.6
			});
		}
	});

	$("#inputGorkhaPalika").on('change',function(){
	    console.log("input gorkha palika");

		var selected_gaupalika = $("#inputGorkhaPalika option:selected")[0].id.toLowerCase();

         $.each(gorkha.getLayers(), function (key, data) {
             var gaunpalika = data.feature.properties.FIRST_GaPa.toLowerCase();
             gaunpalika = gaunpalika+"_m";
             console.log(selected_gaupalika + "Selected");
             console.log(gaunpalika);
             if (gaunpalika == selected_gaupalika) {
                 map.fitBounds(data.getBounds());
             }
         });
	});

	$("#inputNuwaPalika").on('change',function(){

		var selected_gaupalika = $("#inputNuwaPalika option:selected")[0].id;
		$.each(nuwakot.getLayers(), function (key, data) {

             var gaunpalika = data.feature.properties.FIRST_GaPa.toLowerCase();
             gaunpalika = gaunpalika+"_m";
             console.log(selected_gaupalika + "Selected");
             console.log(gaunpalika);
             if (gaunpalika == selected_gaupalika) {
                 map.fitBounds(data.getBounds());
             }
         });
	});




	//plot markers

	var circlemarkerColor = ["red","green","blue","purple"," #33a8ff","aqua"];
	var markerLabel = ["District Office","Area Office","Municipality Office","Rural Municipality Office", "STFC","Building Permit Studio"];
	stfc_gorkha = new L.geoJson.ajax("http://eoi.naxa.com.np/visualizations/api/stfc-locations/?district_name=Gorkha", {
					pointToLayer: function (feature,latlng){
						//var url = "";
						var fill_color = "";
						if(feature.properties.type.toLowerCase() == "district office"){
							//url = 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png';
							fill_color = circlemarkerColor[0];
						}
						else if(feature.properties.type.toLowerCase() == "area office"){
							fill_color = circlemarkerColor[1];
							//url = 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png';
						}
						else if(feature.properties.type.toLowerCase() == "nagarpalika office"){
							fill_color = circlemarkerColor[2];
							//url = 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png';
						}
						else if(feature.properties.type.toLowerCase() == "gaupalika office"){
							fill_color = circlemarkerColor[3];
							//url = 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-orange.png';
						}
						else if(feature.properties.type.toLowerCase() == "stfc" ){
							fill_color = circlemarkerColor[4];
							//url ='https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-yellow.png';

						}
						else if(feature.properties.type.toLowerCase() == "building permit studio"){
							fill_color = circlemarkerColor[5];
							//url = 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-violet.png';
						}
						// var icon = L.icon({
						//     iconUrl: url,
						//     //shadowUrl: 'leaf-shadow.png',

						//     // iconSize:     [38, 95], // size of the icon
						//     // shadowSize:   [50, 64], // size of the shadow
						//     // iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
						//     // shadowAnchor: [4, 62],  // the same for the shadow
						//     // popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
						// });
						// console.log(latlng);
						var marker = L.circleMarker([latlng.lng,latlng.lat], {
							radius:5,
							fillColor: fill_color,
							color: 'black', 
							fillOpacity: 1,
							weight:1
						});
						return marker;

					},
                    onEachFeature: function (feature, layer) {
                        
						var popUpContent = "";
                        popUpContent += '<table style="width:100%;" id="District-popup" class="popuptable">';
                        //console.log(feature);
						for (data in layer.feature.properties) {
                            
                            //var dataspaced = underscoreToSpace(data);
							//console.log(data);
							data1 = data.replace("_"," ");
							data1 = data1.charAt(0).toUpperCase()+data1.substr(1);
                            popUpContent += "<tr>" + "<td>" + data1 + "</td>" + "<td>" + "  " + layer.feature.properties[data] + "</td>" + "</tr>";
							//console.log(popUpContent);
					   }
                        popUpContent += '</table>';
						//console.log(popUpContent);
                        //layer.bindLabel(feature.properties['DISTRICT'], { 'noHide': true, id:"labelDiv" });

                        

                        layer.bindPopup(L.popup({
                            closeOnClick: true,
                            closeButton: true,
                            keepInView: true,
                            autoPan: true,
                            maxHeight: 200,
                            minWidth: 250,
                            popupAnchor:  [-3, -76]
                        }).setContent(popUpContent));

                        // layer.on("mouseover", function (e) {
                        //          e.target.setStyle({weight:2});
                        //          $("#labelDiv").html("<table class='popuptable'><tr><td><h5><b>Layer:</b> District</h5></td></tr><tr><td><h5><b>Name:</b> "+feature.properties['DISTRICT']+"</h5></td><tr></table>");
                        // }).on("mouseout", function(e){
                        //          e.target.setStyle({weight:1});
                        //          $("#labelDiv").html("");
                        // });

                    }
                });
                stfc_gorkha.on('data:loaded', function (data) {
                    // stfc_gorkha.setStyle({
                    //         fillColor: randomColor(),
                    //         weight: 1,
                    //         opacity: 1,
                    //         color: 'black',
                    //         dashArray: '3',
                    //         fillOpacity: 1
                    // });
                   
                    console.log("stfc Layer Added");
                    // 
                });
                //stfc_gorkha.addTo(map);
                //stfc_gorkha.bringToFront();



                stfc_nuwakot = new L.geoJson.ajax("http://eoi.naxa.com.np/visualizations/api/stfc-locations/?district_name=Nuwakot", {
					pointToLayer: function (feature,latlng){
						var fill_color = "";
						if(feature.properties.type.toLowerCase() == "district office"){
							//url = 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-blue.png';
							fill_color = circlemarkerColor[0];
						}
						else if(feature.properties.type.toLowerCase() == "area office"){
							fill_color = circlemarkerColor[1];
							//url = 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png';
						}
						else if(feature.properties.type.toLowerCase() == "nagarpalika office"){
							fill_color = circlemarkerColor[2];
							//url = 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png';
						}
						else if(feature.properties.type.toLowerCase() == "gaupalika office"){
							fill_color = circlemarkerColor[3];
							//url = 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-orange.png';
						}
						else if(feature.properties.type.toLowerCase() == "stfc" ){
							fill_color = circlemarkerColor[4];
							//url ='https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-yellow.png';

						}
						else if(feature.properties.type.toLowerCase() == "building permit studio"){
							fill_color = circlemarkerColor[5];
							//url = 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-violet.png';
						}
						// var icon = L.icon({
						//     iconUrl: url,
						//     //shadowUrl: 'leaf-shadow.png',

						//     // iconSize:     [38, 95], // size of the icon
						//     // shadowSize:   [50, 64], // size of the shadow
						//     // iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
						//     // shadowAnchor: [4, 62],  // the same for the shadow
						//     // popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
						// });
						//console.log(latlng);
						var marker = L.circleMarker([latlng.lng,latlng.lat], {
							radius:5,
							fillColor: fill_color,
							color: 'black', 
							fillOpacity: 1,
							weight:1
						});
						return marker;

					},
                    onEachFeature: function (feature, layer) {
                        
						var popUpContent = "";
                        popUpContent += '<table style="width:100%;" id="District-popup" class="popuptable">';
                        console.log(feature);
						for (data in layer.feature.properties) {
                            
                            //var dataspaced = underscoreToSpace(data);
							data1 = data.replace("_"," ");
							data1 = data1.charAt(0).toUpperCase()+data1.substr(1);
                            popUpContent += "<tr>" + "<td>" + data1 + "</td>" + "<td>" + "  " + layer.feature.properties[data] + "</td>" + "</tr>";
							//console.log(popUpContent);
					   }
                        popUpContent += '</table>';
						//console.log(popUpContent);
                        //layer.bindLabel(feature.properties['DISTRICT'], { 'noHide': true, id:"labelDiv" });

                        

                        layer.bindPopup(L.popup({
                            closeOnClick: true,
                            closeButton: true,
                            keepInView: true,
                            autoPan: true,
                            maxHeight: 200,
                            minWidth: 250
                        }).setContent(popUpContent));

                        // layer.on("mouseover", function (e) {
                        //          e.target.setStyle({weight:2});
                        //          $("#labelDiv").html("<table class='popuptable'><tr><td><h5><b>Layer:</b> District</h5></td></tr><tr><td><h5><b>Name:</b> "+feature.properties['DISTRICT']+"</h5></td><tr></table>");
                        // }).on("mouseout", function(e){
                        //          e.target.setStyle({weight:1});
                        //          $("#labelDiv").html("");
                        // });

                    }
                });
                stfc_nuwakot.on('data:loaded', function (data) {
                    // stfc_nuwakot.setStyle({
                    //         fillColor: randomColor(),
                    //         weight: 1,
                    //         opacity: 1,
                    //         color: 'black',
                    //         dashArray: '3',
                    //         fillOpacity: 1
                    // });
                   
                    console.log("stfc Layer Added");
                    // 
                });
                //stfc_nuwakot.addTo(map);
                //layerswitcher.addOverlay(stfc_gorkha,"STFC Locations Gorkha");
                //layerswitcher.addOverlay(stfc_nuwakot,"STFC Locations Nuwakot");
	//plot markers end







	var legend = L.control({position: 'bottomright'});

	legend.onAdd = function (map) {

		var div = L.DomUtil.create('div', 'info legend'),
			grades = [0, 20, 40, 60, 80],
			labels = ['<strong>Reconstruction Progress</strong>'],
			from, to;
		//div.classList.add("col-md-12");

		for (var i = 0; i < grades.length; i++) {
			from = grades[i];
			to = grades[i + 1];

			labels.push(
				'<div style="background:' + getColor(from + 1) + '; width: 15px; height:15px; display: inline-block; padding-top:5px;"></div><font class = "legend-text"> ' +
				from + (to ? '&ndash;' + to + "%" : '%+')+'</font>');
		}

		labels_marker = ['<strong>STFC Offices</strong>'];
			

		for (var i = 0; i < circlemarkerColor.length; i++) {

			labels_marker.push(
				'<div class="dot" style="background:' + circlemarkerColor[i] + '; width: 15px; height:15px; display: inline-block; padding-top:5px;"></div><font class = "legend-text"> ' +
				markerLabel[i]+'</font>');
		}

		div.innerHTML = '<table><tr><td style="padding:5px;"><div class = "locations" style = "font-size:10px !important;">'+ labels_marker.join('<br>')+'</div></td>' +'<td style="padding:5px;"><div class = "progress" style="display:inline;">'+labels.join('<br>')+'</div></td></tr></table>';
		return div;
	}
	legend.addTo(map);


		