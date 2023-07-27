<?php
require_once 'database.php';
require_once 'Users.php';
$db = new MySQLDatabase();
$users = new Users($db);
$id=0;
$username=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
	    case 'GET':
	        if(isset($_GET['id'])){
	            $id = $_GET['id'];
	        }
	        if(isset($_GET['username'])){
	            $username = $_GET['username'];
	        }
	
	        if($id>0){    
	            $result = $users->get_by_id($id);
	        }elseif($username>0){
	            $result = $users->get_by_username($username);
	        } else {
	            $result = $users->get_all();
	        }        
	       
	        $val = array();
	        while ($row = $result->fetch_assoc()) {
	            $val[] = $row;
	        }
	        
	        header('Content-Type: application/json');
	        echo json_encode($val);
	        break;
	    
	    case 'POST':
	        // Add a new users
	
	        $users->username = $_POST['username'];
	        $users->passwd = $_POST['passwd'];
	        $users->rolename = $_POST['rolename'];
	       
	        $users->insert();
	        $a = $db->affected_rows();
	
	        if($a>0){
	            $data['status']='success';
	            $data['message']='Data Users created successfully.';
	        } else {
	            $data['status']='failed';
	            $data['message']='Data Users not created.';
	        }
	        header('Content-Type: application/json');
	        echo json_encode($data);
	        break;
	
	
	    case 'PUT':
	        // Update an existing data
	        $_PUT = [];
	        if(isset($_GET['id'])){
	            $id = $_GET['id'];
	        }
	        if(isset($_GET['username'])){
	            $username = $_GET['username'];
	        }
	        parse_str(file_get_contents("php://input"), $_PUT);
	        $users->username = $_PUT['username'];
	        $users->passwd = $_PUT['passwd'];
	        $users->rolename = $_PUT['rolename'];
	
	        if($id>0){    
	            $users->update($id);
	        }elseif($username<>""){
	            $users->update_by_username($username);
	        } else {
	            
	        } 
	        
	        $a = $db->affected_rows();
	
	        if($a>0){
	            $data['status']='success';
	            $data['message']='Data Users updated successfully.';
	        } else {
	            $data['status']='failed';
	            $data['message']='Data Users update failed.';
	        }        
	        header('Content-Type: application/json');
	        echo json_encode($data);
	        break;
	
	    case 'DELETE':
	        // Delete a user
	        if(isset($_GET['id'])){
	            $id = $_GET['id'];
	        }
	        if(isset($_GET['username'])){
	            $username = $_GET['username'];
	        }
	        if($id>0){    
	            $users->delete($id);
	        }elseif($username>0){
	            $users->delete_by_username($username);
	        } else {
	            
	        } 
	        
	        $a = $db->affected_rows();
	
	        if($a>0){
	            $data['status']='success';
	            $data['message']='Data Users deleted successfully.';
	        } else {
	            $data['status']='failed';
	            $data['message']='Data Users delete failed.';
	        }        
	        header('Content-Type: application/json');
	        echo json_encode($data);
	        break;
	
	    default:
	        header("HTTP/1.0 405 Method Not Allowed");
	        break;
	    }
	$db->close()
	?> 