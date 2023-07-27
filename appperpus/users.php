<?php
	
	//Simpanlah dengan nama file : Users.php
	require_once 'database.php';
	class Users 
	{
	    private $db;
	    private $table = 'users';
	    public $username = "";
	    public $passwd = "";
	    public $rolename = "";
	
	
	
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
	
	    public function get_by_username(int $username)
	    {
	        $query = "SELECT * FROM $this->table WHERE username = $username";
	        $result_set = $this->db->query($query);   
	        return $result_set;
	    }
	
	    public function insert(): int
	    {
	        $query = "INSERT INTO $this->table (`username`,`passwd`,`rolename`) VALUES ('$this->username','$this->passwd','$this->rolename')";
	        $this->db->query($query);
	        return $this->db->insert_id();
	    }
	
	    public function update(int $id): int
	    {
	        $query = "UPDATE $this->table SET username = '$this->username', passwd = '$this->passwd', rolename = '$this->rolename' 
	        WHERE id = $id";
	        $this->db->query($query);
	        return $this->db->affected_rows();
	
	    }
	
	    public function update_by_username($username): int
	    {
	        $query = "UPDATE $this->table SET username = '$this->username', passwd = '$this->passwd', rolename = '$this->rolename' 
	        WHERE username = $username";
	        $this->db->query($query);
	        return $this->db->affected_rows();
	
	    }
	
	    public function delete(int $id): int
	    {
	        $query = "DELETE FROM $this->table WHERE id = $id";
	        $this->db->query($query);
	        return $this->db->affected_rows();
	    }
	
	    public function delete_by_username($username): int
	    {
	        $query = "DELETE FROM $this->table WHERE username = $username";
	        $this->db->query($query);
	        return $this->db->affected_rows();
	    }
	}
	?> 