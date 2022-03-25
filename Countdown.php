<?php

//A: RECORDS TODAY'S Date And Time
$today = time();

//B: RECORDS Date And Time OF YOUR EVENT
$event = mktime(0,0,0,5,15,2022);

//C: COMPUTES THE DAYS UNTIL THE EVENT.
$countdown = round(($event - $today)/86400);

//D: DISPLAYS COUNTDOWN UNTIL EVENT
print "$countdown days until Badcam3 is free";

?>
