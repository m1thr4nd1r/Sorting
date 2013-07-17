<?php

$nomes = array("Euler", "Diogo", "Dennis", "Java");
$emails = array("ba.elias@gmail.com", "euler.santana@yahoo.com", "diogopri2@gmail.com", "chuckymass@gmail.com", "www.jvfm@hotmail.com", "nancibonfim@gmail.com", "caio@dcc.ufba.br");

for ($i = 0; $i < 4; $i++)
{
   $pos = rand(1,count($nomes)) - 1;
   
   $msg = "</br>" . $nomes[$pos] . " " . ($i + 1) . "</br>";

    unset($nomes[$pos]);

    $nomes = array_values($nomes);
   
    echo $msg;
}

// $flag = 1 ;

// while (count($nomes) > 0)
// {
//    $pos = rand(1,count($nomes)) - 1;
    
//    if ($flag == 1)
//    {
// 	$carro = "Heitor";
// 	$flag = 0;
//    }
//    else
//    {
//         $carro = "Victor";
// 	$flag = 1;
//    }

   // $msg = "</br>" . $nomes[$pos] . " " . $carro . "</br>";

//    unset($nomes[$pos]);

//    $nomes = array_values($nomes);
   
//    echo $msg;

// }

?>