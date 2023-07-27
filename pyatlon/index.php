
<?php
include_once("database.php");
include_once("functions.php");

$sql = "SHOW TABLES";
$result = $conn->query($sql);
?>

<!doctype html>
<html lang="en">
<head>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="fonts/icomoon/style.css">
<link rel="stylesheet" href="css/owl.carousel.min.css">

<link rel="stylesheet" href="css/bootstrap.min.css">

<link rel="stylesheet" href="css/style.css">
<title>Generate PHP Class</title>
<body>
<div class="content">
    <div class="container">
        <h2 class="mb-5">PyAthlon v1.0
            <small class="d-block kecil">Generate REST-API Application Using Python-PHP-MySQL</small></h2>
        <div class="table-responsive custom-table-responsive">
            <table class="table custom-table">
                <thead>
                    <tr>
                        <th scope="col">No</th>
                        <th scope="col">Table Name</th>
                        <th scope="col">Primary Key</th>
                        <th scope="col">Unique Key</th>
                        <th scope="col">Generate</th>
                    </tr>
                </thead>
                <tbody>
                <?php
                    $i=1;
                    while($row = $result->fetch_array()) {
                        $pk = getPrimaryKey($conn,$row[0]);
                        $unik = getUnique($conn,$row[0]);
                ?>
                    <tr scope="row">
                        <td><?php echo $i; ?></td>
                        <td><a href="#"><?php echo $row[0]; ?></a></td>
                        <td><?php echo $pk; ?><small class="d-block">Primary Key name</small></td>
                        <td><?php echo $unik; ?><small class="d-block">Unique Key name</small></td>
                        <td>
                            <a href="http://localhost/pyathlon/gen_php_class.php?table=<?php echo $row[0]; ?>" target="_blank">PHP Class</a> | 
                            <a href="http://localhost/pyathlon/gen_php_api.php?table=<?php echo $row[0]; ?>" target="_blank">PHP API</a> |
                            <a href="http://localhost/pyathlon/gen_py_class.php?table=<?php echo $row[0]; ?>" target="_blank">Python Class</a> |
                            <a href="http://localhost/pyathlon/gen_py_form.php?table=<?php echo $row[0]; ?>" target="_blank">TKinter Form</a>
                        </td>
                    </tr>
                <?php
                        $i++;
                    }
                ?>
                </tbody>
            </table>
        </div>
        <h2 class="mb-5">
            <small class="d-block kecil">Copyrights@2023, Created by : Freddy Wicaksono, M.Kom</small></h2>
    </div>
</div>
<script src="js/jquery-3.3.1.min.js"></script>
<script src="js/popper.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/main.js"></script>
</body>
</html>
<?
$conn->close();
?>