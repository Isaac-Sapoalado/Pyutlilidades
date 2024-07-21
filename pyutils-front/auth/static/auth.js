async function cadastro(){
    var form = form_elements()
    r = await fetch(
        "http://127.0.0.1:8000/auth/cadastrar/",{
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
        }).then(response => response.json()).then(dado => {return dado})
        .catch(error => console.log(error))
}
async function login(){
    var form = form_elements()
    data = await fetch(
        "http://127.0.0.1:8000/auth/login/",{
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
            sessionStorage.setItem('user',dado.user)
            sessionStorage.setItem('token',('Token ' + dado.access_token))
        })
        .catch(error => autherror(error))
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