<?php 

$x=1;
$y=1;
$z=1;

for($i=1; $i<3000; $i++){

	$z=$i;

	for ($j=1; $j<3000 && $j<$i; $j++) {

		$y=$j;

		for ($k=1; $k<3000 && $k<$j ; $k++){

			$x=$k;

			if($y%$x!=0 && $z%$x!=0){


				$zz = $x*$x + $y*$y;
				
				if($z==sqrt($zz)){

					if($x*$y/2==666666){

						echo 'x = ' . $x . '<br>';
						echo 'y = ' . $y . '<br>';
						echo 'z = ' . $z . '<br>';
					}
				}
				

			}	
		
		}
	}
}