const userName = '{{ user_name }}'; // substitua com o nome do usuário
const overlay = document.querySelector('.overlay');
const welcomeMessage = document.querySelector('.welcome-message');

// Verificamos se o cookie "welcome_seen" existe
if (!getCookie('welcome_seen')) {
	overlay.classList.add('show'); // exibimos o overlay

	welcomeMessage.innerHTML = `Olá, seja bem vindo, ${userName}!`;

	setTimeout(() => {
		welcomeMessage.style.opacity = 1; // efeito de fade-in
	}, 1000); // após 1 segundo

	setTimeout(() => {
		welcomeMessage.style.opacity = 0; // efeito de fade-out
		overlay.classList.remove('show'); // escondemos o overlay
		setCookie('welcome_seen', 'true', 30); // setamos o cookie para 30 dias
	}, 5000); // após 5 segundos
}

// Função para setar um cookie
function setCookie(cname, cvalue, exdays) {
	const d = new Date();
	d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
	let expires = 'expires=' + d.toUTCString();
	document.cookie = cname + '=' + cvalue + ';' + expires + ';path=/';
}

// Função para obter um cookie
function getCookie(cname) {
	let name = cname + '=';
	let decodedCookie = decodeURIComponent(document.cookie);
	let ca = decodedCookie.split(';');
	for (let i = 0; i < ca.length; i++) {
		let c = ca[i];
		while (c.charAt(0) == ' ') {
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
			return c.substring(name.length, c.length);
		}
	}
	return '';
}