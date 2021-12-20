<?php
//place this before any script you want to calculate time
$time_start = microtime(true); 
$s  = [];
$k=0;
function primeNumbers(){

	global $s,$k;
 	for($a=2 ; $a<1000000; $a++){

 		$z = 0;

 		for($i=2 ; $i<$a ; $i++){

 			if($a%$i == 0){

 				$z=1;
 				break;
 			}
 		
 		}

 		// if($z==0) echo $a . '<br>';
 		
 		if($z==0){
 			$s[$k] = $a;
 			$k++;
 		}
 	}	
  	
  	echo "the primeNumbers";
}


primeNumbers();

for ($i=0; $i < count($s); $i++) { 
	
	echo $s[$i] . '-->' . $i . '<br>'  ;
}


/*

$f=0;

for ($i=0; $i < count($s); $i++) { 
	
	for ($j=0; $j<count($s); $j++) { 

		if($s[$i]*$s[$j]== 806515533049393 ){
			echo $s[$i] . '*' . $s[$j] . ' = 806515533049393' ;
			$f=1;
			break;
		}
	}
	if($f == 1){ break;
		echo "the End";
	}
	
} 
if ($f == 0) {
		echo '<br>Sorry, try again';
	
	}
*/
$time_end = microtime(true);

//dividing with 60 will give the execution time in minutes otherwise seconds
$execution_time = ($time_end - $time_start)/60;

//execution time of the script
echo '<b>Total Execution Time:</b> '.$execution_time.' Mins';
// if you get weird results, use number_format((float)
/*





/*
 $x = [];

 for ($i=0; $i <5 ; $i++) $x[$i] = $i;
 


print_r($x);

for ($i=0; $i < count($x); $i++) { 
	
	echo "<br>" . $x[$i] ;
}
*/