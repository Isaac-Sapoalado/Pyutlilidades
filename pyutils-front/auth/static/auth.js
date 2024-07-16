async function cadastro(){
    r = await fetch(
        "http://127.0.0.1:8000/auth/cadastro/",{
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                'username':'isaac',
                'email':'sapoalado',
                'password':'3'
            })
        }).then(response => response.json()).then(dado => {return dado})
    
        
}
async function login(){
    r = await fetch(
        "http://127.0.0.1:8000/auth/login/",{
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                'username':'isaac',
                'email':'sapo070@gmail.com',
                'password':'senha'
            })
        }).then(response => response.json()).then(dado => {return dado})

    sessionStorage.setItem('user',r.user)
    sessionStorage.setItem('token',('Token ' + r.access_token))

}
console.log('ola')