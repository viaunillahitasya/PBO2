<?php
//Simpanlah dengan nama file : Pengembalian.php
require_once 'database.php';
class Pengembalian 
{
    private $db;
    private $table = 'pengembalian';
    public $id_anggota = "";
    public $id_buku = "";
    public $tanggal_pengembalian = "";
    public $denda = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_id_buku(int $id_buku)
    {
        $query = "SELECT * FROM $this->table WHERE id_buku = $id_buku";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`id_anggota`,`id_buku`,`tanggal_pengembalian`,`denda`) VALUES ('$this->id_anggota','$this->id_buku','$this->tanggal_pengembalian','$this->denda')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET id_anggota = '$this->id_anggota', id_buku = '$this->id_buku', tanggal_pengembalian = '$this->tanggal_pengembalian', denda = '$this->denda' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_id_buku($id_buku): int
    {
        $query = "UPDATE $this->table SET id_anggota = '$this->id_anggota', id_buku = '$this->id_buku', tanggal_pengembalian = '$this->tanggal_pengembalian', denda = '$this->denda' 
        WHERE id_buku = $id_buku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_id_buku($id_buku): int
    {
        $query = "DELETE FROM $this->table WHERE id_buku = $id_buku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>