<?php
require_once 'database.php';
require_once 'Peminjaman.php';
$db = new MySQLDatabase();
$peminjaman = new Peminjaman($db);
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
            $result = $peminjaman->get_by_id($id);
        }elseif($id_buku>0){
            $result = $peminjaman->get_by_id_buku($id_buku);
        } else {
            $result = $peminjaman->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new peminjaman
        $peminjaman->id_anggota = $_POST['id_anggota'];
        $peminjaman->id_buku = $_POST['id_buku'];
        $peminjaman->tanggal_peminjaman = $_POST['tanggal_peminjaman'];
        $peminjaman->tangal_kembali = $_POST['tangal_kembali'];
       
        $peminjaman->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman not created.';
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
        $peminjaman->id_anggota = $_PUT['id_anggota'];
        $peminjaman->id_buku = $_PUT['id_buku'];
        $peminjaman->tanggal_peminjaman = $_PUT['tanggal_peminjaman'];
        $peminjaman->tangal_kembali = $_PUT['tangal_kembali'];
        if($id>0){    
            $peminjaman->update($id);
        }elseif($id_buku<>""){
            $peminjaman->update_by_id_buku($id_buku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman update failed.';
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
            $peminjaman->delete($id);
        }elseif($id_buku>0){
            $peminjaman->delete_by_id_buku($id_buku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman delete failed.';
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