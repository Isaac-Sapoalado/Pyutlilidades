async function cadastro(){
    var form = form_elements()
    r = await fetch(
        "https://pyutilidades.onrender.com/auth/cadastrar/",{
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                'username':form[0].value,
                'email':form[1].value,
                'password':form[2].value
            })
        }).then(response => response.json()).then(dado => {login()})
        .catch(error => console.log(error))
}
async function login(){
    var form = form_elements()
    data = await fetch(
        "https://pyutilidades.onrender.com/auth/login/",{
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                'username':form[0].value,
                'email':form[1].value,
                'password':form[2].value
            })
        })
        .then(response => response.json()).then(dado => {
            sessionStorage.setItem('pk',dado.user.pk)
            sessionStorage.setItem('username',dado.user.username)
            sessionStorage.setItem('token',('Token ' + dado.access_token))
        })
        .catch(error => autherror(error))
    history.back()

    
}

function autherror(erro){
    var form = form_elements
    form[0].value = erro
    form[1].value = erro
    form[2].value = erro
}
function form_elements(){
    var conjunto = [document.getElementById("nome"),
        document.getElementById("email"),
        document.getElementById("senha")]
    return conjunto
}