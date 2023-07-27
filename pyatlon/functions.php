<?php
include("database.php");
function printCode($source_code)
{

	if (is_array($source_code))
		return false;
  
	$source_code = explode("\n", str_replace(array("\r\n", "\r"), "\n", $source_code));
	$line_count = 1;
    $formatted_code='';
	foreach ($source_code as $code_line)
	{
		$formatted_code .= '<tr><td>'.''.'</td>';
		$line_count++;
	  
		if (preg_match('?(php)?', $code_line))
			$formatted_code .= '<td>'. str_replace(array('<code>', '</code>'), '', highlight_string($code_line, true)).'</td></tr>';
		else
			$formatted_code .= '<td>'.preg_replace('(&lt;\?php&nbsp;)', '', str_replace(array('<code>', '</code>'), '', highlight_string('<?php '.$code_line, true))).'</td></tr>';
	}

	return '<table style="font: 1em Consolas, \'andale mono\', \'monotype.com\', \'lucida console\', monospace;">'.$formatted_code.'</table>';
}

function getPrimaryKey($conn,$tbname){
    $result = $conn->query("DESCRIBE $tbname");

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            if (strpos($row["Key"], "PRI") !== false) {
                $val = $row["Field"];
                break;
            }
        }
    } else {
        $val ='';
    }
    return $val;
}

function getUnique($conn,$tbname){
    $result = $conn->query("DESCRIBE $tbname");
    $val="";

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            if (strpos($row["Key"], "UNI") !== false) {
                $val = $row["Field"];
            }
        }
    } else {
        $val = "";
    }
    return $val;
}

function getTotalFields($conn, $tbname){
    $result = $conn->query("DESCRIBE $tbname");
    if($result){
        $numrows = $result->num_rows;
    } else {
        $numrows = 0;
    }
    
    return $numrows;
}

function getEnumValues($conn, $dbname, $tbname, $column){
    $x=array();
    $result = $conn->query("SELECT COLUMN_TYPE FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_SCHEMA = '$dbname' AND TABLE_NAME = '$tbname' AND COLUMN_NAME = '$column'");
    $data = mysqli_fetch_array($result);
    $val = str_replace("enum","",$data["COLUMN_TYPE"]);
    //$val = str_replace("(","",$val);
    //$val = str_replace(")","",$val);
    //$val = str_replace("'",'',$val);
    //$x = explode(",",$val);
    return $val;
}

function getColumnType($conn, $dbname, $tbname, $column){
    $result = $conn->query("SELECT COLUMN_NAME,DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_SCHEMA = '$dbname' AND TABLE_NAME = '$tbname' AND COLUMN_NAME='$column'");
    $data=mysqli_fetch_array($result);
    $val = $data['DATA_TYPE'];
    return $val;
}
?>