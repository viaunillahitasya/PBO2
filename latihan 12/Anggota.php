<?php
//Simpanlah dengan nama file : Anggota.php
require_once 'database.php';
class Anggota 
{
    private $db;
    private $table = 'anggota';
    public $nim = "";
    public $nama = "";
    public $alamat = "";
    public $jk = "";
    public $prodi = "";
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
    public function get_by_nim(int $nim)
    {
        $query = "SELECT * FROM $this->table WHERE nim = $nim";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`nim`,`nama`,`alamat`,`jk`,`prodi`) VALUES ('$this->nim','$this->nama','$this->alamat','$this->jk','$this->prodi')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET nim = '$this->nim', nama = '$this->nama', alamat = '$this->alamat', jk = '$this->jk', prodi = '$this->prodi' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_nim($nim): int
    {
        $query = "UPDATE $this->table SET nim = '$this->nim', nama = '$this->nama', alamat = '$this->alamat', jk = '$this->jk', prodi = '$this->prodi' 
        WHERE nim = $nim";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_nim($nim): int
    {
        $query = "DELETE FROM $this->table WHERE nim = $nim";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>