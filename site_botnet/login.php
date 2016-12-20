
<!DOCTYPE html>
<html lang=pt-BR>
<head>
  <meta charset="UTF-8">
  <title>Logar-se</title>
      <link rel="stylesheet" href="/static/app/css/style.css">
</head>

<body>
  	
  	<div class="background-page">
	  	<video autoplay loop>
	  		<source src="/static/app/bg_video/coding.webm" type="video/webm">
	  	</video>
	</div> <!-- fim background-page -->


	<div class="pagina">
		<div class="formulario">
			<form action="login_check" method="post">
				<input type="hidden" name="from_page" value="%(from_page)s" />
				<input type="text" name="username" placeholder="Usuario..." required>
				<input type="password" name="password" placeholder="Digite sua senha..." required><br />
										.
				<input type="submit" value="Logar-se">
			</form>
		</div> <!-- fim formulario -->
	</div> <!-- fim pagina -->

</body>
</html>
