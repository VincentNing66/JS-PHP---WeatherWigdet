<?php

try{
   	
   	$conn = new PDO("mysql:host=mysql.cms.waikato.ac.nz;dbname=qn6","qn6","my11206882sql");
	$conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
   	} 
catch (PDOException $e) {
   		echo "Database connection error " . $e->getMessage();
   	}

	
	ini_set("error_reporting",E_ALL); 
	ini_set("log_errors","1"); 
	ini_set("error_log","/home/qn6/course_html/compx322assn2/php_errors.txt");

   //Builds the connection, report errors when appeared
?>