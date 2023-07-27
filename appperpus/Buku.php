<?php
//Simpanlah dengan nama file : Buku.php
require_once 'database.php';
class Buku 
{
    private $db;
    private $table = 'buku';
    public $kodebuku = "";
    public $judul = "";
    public $kategori = "";
    public $pengarang = "";
    public $penerbit = "";
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
    public function get_by_kodebuku(int $kodebuku)
    {
        $query = "SELECT * FROM $this->table WHERE kodebuku = $kodebuku";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodebuku`,`judul`,`kategori`,`pengarang`,`penerbit`) VALUES ('$this->kodebuku','$this->judul','$this->kategori','$this->pengarang','$this->penerbit')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodebuku = '$this->kodebuku', judul = '$this->judul', kategori = '$this->kategori', pengarang = '$this->pengarang', penerbit = '$this->penerbit' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodebuku($kodebuku): int
    {
        $query = "UPDATE $this->table SET kodebuku = '$this->kodebuku', judul = '$this->judul', kategori = '$this->kategori', pengarang = '$this->pengarang', penerbit = '$this->penerbit' 
        WHERE kodebuku = $kodebuku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodebuku($kodebuku): int
    {
        $query = "DELETE FROM $this->table WHERE kodebuku = $kodebuku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>