<?php
require_once('./dbconnect.php');		//Build the connection to the database

	$town = $_GET['town'];				//Get the variable from the js file

	$stmt = $conn->prepare("SELECT * FROM weather where town=:town");			//Selects the right data which matches the input
	$stmt->bindParam(':town', $town);

	$stmt->execute();			//excute it 
	
	$data = array();			//declare a list whcih will be used to store the output from the database 
	
	while($row = $stmt->fetch()){
		$data[] = $row;			//Storing the output from the database to the list variable
	}

	echo json_encode($data);		//Pass the output using JSON format to js
	
?>
