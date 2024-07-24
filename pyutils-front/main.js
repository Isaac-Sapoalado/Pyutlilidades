async function iniciar(){
    var div = document.getElementById("login-dados")
    if (!(sessionStorage.getItem("token")==null)){
        var nome = sessionStorage.getItem('username')
        div.innerHTML = `Olá, ${nome}`
        console.log('token')
    }else{
        var link = document.createElement("a")
        var btn = document.createElement("button")
        btn.innerText = 'cadstrar/logar'
        link.href = 'https://pyutilidades.vercel.app/auth/cadastro.html'
        link.appendChild(btn)
        console.log('login-dado')
    }

}
console.log('iniciar')
iniciar()