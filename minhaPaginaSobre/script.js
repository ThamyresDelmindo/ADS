let botao = document.getElementById('botao');
botao.style.background="pink";

botao.addEventListener("mouseover",e =>{
    botao.style.background="red"
});

botao.addEventListener("mouseout",e =>{
    botao.style.background="pink"
});

document.getElementById('botao').addEventListener('click', function(){
    const mensagens = [
        "Você é capaz de coisas incríveis hoje! 🌟", 
        "Cada clique é um passo rumo aos seus sonhos. 🚀",
        "O segredo do progresso é começar. 💪",
        "Você está mais perto do que imagina! 🔥",
        "A persistência transforma o 'não' em 'agora'! ✨",
        "Sorria! Você está programando seu futuro. 😊",
        "Grandes códigos começam com pequenos cliques. 💻"
    ];


const mensagemDiv = document.getElementById('mensagem');
    mensagemDiv.innerHTML = '';

mensagens.forEach(msg => {
        mensagemDiv.innerHTML += msg + '<br><br>'; 
    });
    
mensagemDiv.classList.add('mostrar');

if (mensagemDiv.style.display === 'none') {
            // mostra a msg
           mensagemDiv.style.display = 'block' 
} else {
            // Oculta a mensagem
            mensagemDiv.style.display = "none";
        }
});