<?php

$nomes = array("Victor", "Theus", "Nanci", "Arlindo");
$emails = array("ba.elias@gmail.com", "euler.santana@yahoo.com", "diogopri2@gmail.com", "chuckymass@gmail.com", "www.jvfm@hotmail.com", "nancibonfim@gmail.com", "caio@dcc.ufba.br");

$flag = 0 ;
$equipe = "";

while (count($nomes) > 0)
{
   $pos = rand(1,count($nomes)) - 1;
    
   $flag = ($flag + 1) % 5;
   
	if ($flag == 1)
		$equipe = "Parte 1";
   	else if ($flag == 2)
   		$equipe = "Parte 2";
   	else if ($flag == 3) 
   		$equipe = "Parte 3";
	else if ($flag == 4)
		$equipe = "Parte 4";
				   
   $msg = "</br>" . $nomes[$pos] . " - " . $equipe . "</br>";

   unset($nomes[$pos]);

   $nomes = array_values($nomes);
   
   echo $msg;

}

?>