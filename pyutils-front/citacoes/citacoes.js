
async function get(){
    var dado;
    fet = await fetch("http://127.0.0.1:8000/api/cita/", {
        mode: 'cors',
        method: "GET",
        headers: {
            'Content-Type':'application/json'
        }
    }

    )
    .then(Response => Response.json()).then(data => {
        dado = data
    })
    .catch(error => console.log(error))
    
    adicionar(dado)

}

function adicionar(lista){
    textcard = document.getElementById('cita_texto')
    autor = document.getElementById('autor')
    textcard.innerText = lista.citacao
    autor.innerText = "autor:" + lista.autor
}