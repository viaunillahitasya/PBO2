<?php
require_once 'database.php';
require_once 'Pengembalian.php';
$db = new MySQLDatabase();
$pengembalian = new Pengembalian($db);
$id=0;
$id_buku=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_buku'])){
            $id_buku = $_GET['id_buku'];
        }
        if($id>0){    
            $result = $pengembalian->get_by_id($id);
        }elseif($id_buku>0){
            $result = $pengembalian->get_by_id_buku($id_buku);
        } else {
            $result = $pengembalian->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new pengembalian
        $pengembalian->id_anggota = $_POST['id_anggota'];
        $pengembalian->id_buku = $_POST['id_buku'];
        $pengembalian->tanggal_pengembalian = $_POST['tanggal_pengembalian'];
        $pengembalian->denda = $_POST['denda'];
       
        $pengembalian->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian not created.';
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
        if(isset($_GET['id_buku'])){
            $id_buku = $_GET['id_buku'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $pengembalian->id_anggota = $_PUT['id_anggota'];
        $pengembalian->id_buku = $_PUT['id_buku'];
        $pengembalian->tanggal_pengembalian = $_PUT['tanggal_pengembalian'];
        $pengembalian->denda = $_PUT['denda'];
        if($id>0){    
            $pengembalian->update($id);
        }elseif($id_buku<>""){
            $pengembalian->update_by_id_buku($id_buku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['id_buku'])){
            $id_buku = $_GET['id_buku'];
        }
        if($id>0){    
            $pengembalian->delete($id);
        }elseif($id_buku>0){
            $pengembalian->delete_by_id_buku($id_buku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian delete failed.';
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
