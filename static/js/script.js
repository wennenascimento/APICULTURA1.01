const button = document.getElementById('button')
button.addEventListener('click', (event) => {
event.preventDefault()
//alert('butao add')


const nome=document.getElementById('nome')
const email=document.getElementById('email')
const password=document.getElementById('password')

if(nome.value == ''){
alert('insira nome')
}
if(email.value == ''){
alert('insira email')
}

if(password.value == ''){
alert('insira senha')
}
})
