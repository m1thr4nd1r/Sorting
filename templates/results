<?php

if (isset($_POST['elements']) && isset($_POST['things']))
{
	$e = $_POST['elements'];
	$t = $_POST['things'];
	
	$end = strpos($e,';');
	
	while ($end !== FALSE)
	{
		$elements[] = substr($e, 0, $end);
		$end++;
		$e = substr($e,$end);
		$end = strpos($e,';');
	}
	
	$elements[] = $e;
	
	$end = strpos($t,';');
	
	while ($end != FALSE)
	{
		$things[] = substr($t, 0, $end);
		$end++;
		$t = substr($t,$end);
		$end = strpos($t,';');
	}
	
	$things[] = $t;
	
	$selector = -1;
	
	while (count($elements) > 0)
	{
		$pos = rand(0,count($elements)-1);
	
		$selector = ($selector + 1) % count($things);
			
		$result = "</br>" . $elements[$pos] . " - " . $things[$selector] . "</br>";
	
		unset($elements[$pos]);
	
		$elements = array_values($elements);
		 
		echo $result;
	}
}
?>