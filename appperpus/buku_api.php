<?php
require_once 'database.php';
require_once 'Buku.php';
$db = new MySQLDatabase();
$buku = new Buku($db);
$id=0;
$kodebuku=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodebuku'])){
            $kodebuku = $_GET['kodebuku'];
        }
        if($id>0){    
            $result = $buku->get_by_id($id);
        }elseif($kodebuku>0){
            $result = $buku->get_by_kodebuku($kodebuku);
        } else {
            $result = $buku->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new buku
        $buku->kodebuku = $_POST['kodebuku'];
        $buku->judul = $_POST['judul'];
        $buku->kategori = $_POST['kategori'];
        $buku->pengarang = $_POST['pengarang'];
        $buku->penerbit = $_POST['penerbit'];
       
        $buku->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku not created.';
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
        if(isset($_GET['kodebuku'])){
            $kodebuku = $_GET['kodebuku'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $buku->kodebuku = $_PUT['kodebuku'];
        $buku->judul = $_PUT['judul'];
        $buku->kategori = $_PUT['kategori'];
        $buku->pengarang = $_PUT['pengarang'];
        $buku->penerbit = $_PUT['penerbit'];
        if($id>0){    
            $buku->update($id);
        }elseif($kodebuku<>""){
            $buku->update_by_kodebuku($kodebuku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kodebuku'])){
            $kodebuku = $_GET['kodebuku'];
        }
        if($id>0){    
            $buku->delete($id);
        }elseif($kodebuku>0){
            $buku->delete_by_kodebuku($kodebuku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku delete failed.';
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