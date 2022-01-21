<html>
<head>

<h1>Automatic IP Dumper</h1>
<style>

table
{
border-style:solid;
border-width:2px;
border-color:pink;
}

</style>
</head>

<body bgcolor="#EEEEEE">
<?php

$db = new SQLite3('data.db');
$res = $db->query('SELECT * FROM IPLog ORDER BY Date DESC');

echo "<table border='1'>
<tr>
<th>Date</th>
<th>Local IP</th>
<th>Public IP</th>
<th>Location</th>
<th>Hostname</th>
<th>ISP</th>
<th>Country Code</th>
</tr>";

while ($row = $res->fetchArray())
  {
  echo "<tr>";
  echo "<td>" . $row['Date'] . "</td>";
  echo "<td>" . $row['Local_IP'] . "</td>";
  echo "<td>" . $row['Public_IP'] . "</td>";
  echo "<td>" . $row['Location'] . "</td>";
  echo "<td>" . $row['Hostname'] . "</td>";
  echo "<td>" . $row['ISP'] . "</td>";
  echo "<td>" . $row['Country'] . "</td>";
  echo "</tr>";
  }

echo "</table>";
?>

</body>
</html>