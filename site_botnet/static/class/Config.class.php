<?php

class Config
{
	private $Consulta;

	private function Conectar(){

		define('HOST','localhost');
		define('DB','botnet');
		define('USER','root');
		define('PASS','');

		try{
			return new PDO("mysql:host=".HOST.";dbname=".DB,USER,PASS);
		}
		catch(PDOException $error) {
			echo $error->getMessage();
		}
	}

	public function Logar($usuario, $senha){

		$this->Consulta = $this->Conectar()->prepare("SELECT * FROM usuarios WHERE usuario = :usuario AND senha = :senha");
		$this->Consulta->bindValue(':usuario', $usuario);
		$this->Consulta->bindValue(':senha', $senha);
		$this->Consulta->execute();

		return $this->Consulta->rowCount();
	}

}
