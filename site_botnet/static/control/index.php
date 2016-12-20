<?php
	require_once('../class/Config.class.php');
	$consulta = new Config;

	//Verifica se existe o post logar e se os campos usuario e senha não estão vazios
	if(isset($_POST['logar']) AND !empty(trim($_POST['usuario'])) AND !empty(trim($_POST['senha']))):

		//Faz a consulta se o usuario existe
		if($consulta->Logar($_POST['usuario'],$_POST['senha']) === 1):
			echo "Usuario Existe";
		else:
			echo "Usuario não exite";
		endif;

	else:
		echo "Acesso Negado!";
	endif;
