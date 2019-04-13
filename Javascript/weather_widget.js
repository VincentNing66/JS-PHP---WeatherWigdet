function WeatherWidget(container_element){

	var _list = [];		//The variable which will be storing the list of output from database
	var _request ;    	//Variable for sending php request
	var _currentSortOrder = 1; //Variable for sorting usage

	var _ui = {
		sortByTown : null,
		sortByTemp : null,
		selectBox : null,
		container : null,
		titlebar : null,
		selectbar : null,								//Some default user interface properties
		btnbar : null,
		sortByTemp  : null,
		sortByTown : null,
		list : null,
		dom_element : null,
    }; 

	var _createUI = function(){			//Create the main user interface
		_ui.container = container_element;
		_ui.container.className = "monitor";		//Create the container which will contain all functionalies


		_ui.titlebar = document.createElement("div");
		_ui.titlebar.className = "title bars";							
		_ui.titlebar.label = document.createElement("span");			//Create the title bar
		_ui.titlebar.label.innerHTML = " Weather Widget";
		_ui.titlebar.appendChild(_ui.titlebar.label);

		_ui.selectbar = document.createElement("div");
		_ui.selectbar.label = document.createElement("span");
		_ui.selectbar.label.innerHTML = " Select Town : ";				//Create the bar which contain the select box to select cities
		_ui.selectBox = document.createElement("select");
		_ui.selectBox.className = 'section';
		_ui.selectbar.appendChild(_ui.selectbar.label);
		_ui.selectbar.appendChild(_ui.selectBox)
		_ui.selectbar.className = 'bars';


		_ui.placeholderOpt= document.createElement("option");
		_ui.placeholderOpt.innerHTML = 'Select your option';
		_ui.placeholderOpt.value = '';									//Default option for the select box as a placeholder
		_ui.placeholderOpt.selected = true;
		_ui.placeholderOpt.disabled = true;
		_ui.selectBox.appendChild(_ui.placeholderOpt);

		_ui.Dunedin= document.createElement("option");
		_ui.Dunedin.innerHTML = 'Dunedin';
		_ui.Dunedin.onclick = function(){								//Dunedin option for the select box
			_ShowDetail('Dunedin')
			
			}
		_ui.selectBox.appendChild(_ui.Dunedin);

		_ui.Christchurch = document.createElement("option");
		_ui.Christchurch.innerHTML = 'Christchurch';
		_ui.Christchurch.onclick = function(){
			_ShowDetail('Christchurch')									//Christchurch option for the select box
			}
		_ui.selectBox.appendChild(_ui.Christchurch);

		_ui.Tauranga = document.createElement("option");
		_ui.Tauranga.innerHTML = 'Tauranga';
		_ui.Tauranga.onclick = function(){
			_ShowDetail('Tauranga')										//Tauranga option for the select box
			}
		_ui.selectBox.appendChild(_ui.Tauranga);

		_ui.Auckland = document.createElement("option");
		_ui.Auckland.innerHTML = 'Auckalnd';
		_ui.Auckland.onclick = function(){
			_ShowDetail('Auckland')										//Auckland option for the select box
			}
		_ui.selectBox.appendChild(_ui.Auckland);

		_ui.Hamilton = document.createElement("option");
		_ui.Hamilton.innerHTML = 'Hamilton';
		_ui.Hamilton.onclick = function(){
			_ShowDetail('Hamilton')										//Hamilton option for the select box
			}
		_ui.selectBox.appendChild(_ui.Hamilton);

		_ui.Wellington = document.createElement("option");
		_ui.Wellington.innerHTML = 'Wellington';
		_ui.Wellington.onclick = function(e){
			e.
			_ShowDetail('Wellington')									//Wellington option for the select box
			}
		_ui.selectBox.appendChild(_ui.Wellington);


		_ui.btnbar = document.createElement("div");
		_ui.btnbar.label = document.createElement("span");				//The bar which contains two sorting buttons
		_ui.btnbar.label.innerHTML = " Sort By : ";
		_ui.btnbar.appendChild(_ui.btnbar.label);



		_ui.sortByTown = document.createElement("button");
		_ui.sortByTown.innerHTML = 'Town';
		_ui.sortByTown.className = 'btns';								//Town button sorts the list by town name
		_ui.sortByTown.onclick = function(){
			_doSort(1);
			}


		_ui.sortByTemp = document.createElement("button");
		_ui.sortByTemp.innerHTML = 'Max Temp';							//Max Temp button sorts the list by the maximum temperature
		_ui.sortByTemp.className = 'btns';
		_ui.sortByTemp.onclick = function(){
			_doSort(0);
   		}

		_ui.btnbar.appendChild(_ui.sortByTown);
		_ui.btnbar.appendChild(_ui.sortByTemp );						//Append two buttons to the button bar
		_ui.btnbar.className = 'bars';

		_ui.list = document.createElement("div");

		_ui.container.appendChild(_ui.titlebar);
		_ui.container.appendChild(_ui.selectbar);						//Append all bars as a part of the main container
		_ui.container.appendChild(_ui.btnbar);
		_ui.container.appendChild(_ui.list);
	}

	var _initialisa = function(container_element){
		_createUI(container_element);
	}																	//Initialisation whcih will be run the first, it calles _createUI whcih sets up the default user interface
	_initialisa(container_element);

	var _doSort = function(sortBy){
	 	if(sortBy == 1){
	 		_currentSortOrder = 1;	 	
	 	}
	 	else{															//Sorting function which will be called when either 'Town' button or 'Max Temp' button called, recognize them by the input value
	 		_currentSortOrder = 0;
	 	}
		 _refreshWeatherList();
	 }

	var _maxTSort= function(a,b){
		return a.getMaxT() - b.getMaxT();
	}
	
	var _townSort= function(a, b){
		if(a.getTown() > b.getTown()){
			return 1;
		} else if (a.getTown() < b.getTown()){
			return -1;
		} else {
			return 0;
		}
	}

	var _refreshWeatherList = function(){
		if(_ui.list == null)
			return;
		while(_ui.list.hasChildNodes()){
  			_ui.list.removeChild(_ui.list.lastChild);
		}
		if(_currentSortOrder == 1){										//The function which will be called after _doSort function, which checkes the list of data then recognize which function will be used to sort by recognizing which button is clicked
			_list.sort(_townSort); 
		} else {
			_list.sort(_maxTSort);
		}

		for(var i = 0; i < _list.length; i++){
			var wline = _list[i];										//Then append the sorted list back to the UI
			_ui.list.appendChild(wline.getDomElement());
		}
	}

	var _ShowDetail = function (town){
		for(i = 0; i < _list.length; i++){
			if(name == _list[i].getTown()){								//The function which will be called when sending a request to database though php
				alert("Already in list");
				return;
			}
		}
		_request = new XMLHttpRequest();
 		var url = "PHP/weather.php?town=" + town;
		_request.open("GET", url, true);
		_request.onreadystatechange = _addNewWeatherListItem ;
		_request.send(town);
		console.log('twice')
	}
	
	var _addNewWeatherListItem = function(){
		if (_request.readyState = 4){
			if (_request.status == 200) {
				var data = JSON.parse(_request.responseText);			//The response from database, whcih is in JSON format
				if(data.length == 0){
					alert("No found");
					return;
				}
				var town = data[0].town;  	
				var weather = data[0].outlook;  
				var minT =data[0].min_temp;
				var maxT =data[0].max_temp;
				console.log(town)
				console.log(weather )
				console.log(minT )
				console.log(maxT )

				var items = new WLine(town, weather, minT, maxT);	 //create a PhoneLine instance
				_list.push(items); //add it to the _list array
				_refreshWeatherList();  //refresh the UI display on the page
				return false
			}
		}
	}

	var WLine = function(town, outlook, min, max){
		
		var _town = town;
		var _outlook = outlook;
		var _min = min;
		var _max = max;

		var _ui = {
			dom_element:null,
			town_label:null,
			outlook_label:null,
			min_label:null,
			max_label:null,
		}
		var _createUI = function() {
			_ui.dom_element = document.createElement('div');
			_ui.dom_element.className = 'list';

			_ui.town_label = document.createElement('span');
			_ui.town_label.innerHTML = _town;
			_ui.town_label.className = 'listItems';

			_ui.outlook_label = document.createElement('span');
			_ui.outlook_label.innerHTML = _outlook;
			_ui.outlook_label.className = 'listItems';

			_ui.min_label = document.createElement('span');
			_ui.min_label.innerHTML = _min;
			_ui.min_label.className = 'listItems';

			_ui.max_label = document.createElement('span');
			_ui.max_label.innerHTML = _max;
			_ui.max_label.className = 'listItems';

			_ui.dom_element.appendChild(_ui.town_label);
			_ui.dom_element.appendChild(_ui.outlook_label);
			_ui.dom_element.appendChild(_ui.min_label);					//The funtion which takes the value from the database, then print them to the UI list
			_ui.dom_element.appendChild(_ui.max_label);
		}

		this.getDomElement = function(){
			return _ui.dom_element;
		}

		this.getTown = function(){
			return _town;
		}

		this.getOutLook = function(){
			return _outlook;
		}

		this.getMinT = function(){
			return _min;
		}
		
		this.getMaxT = function(){
			return _max;
		}
	
		_createUI();
	}
}


