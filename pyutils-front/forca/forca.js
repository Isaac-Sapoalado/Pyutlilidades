var palavra = ''
var outpalavra = ''
var dicas = []
var tentativas = 5

async function pegar_palavra(){
    response = await fetch(
        "http://127.0.0.1:8000/api/palavra/",{
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type':'application/json'
            }
        })
        .then(response => response.json()).then(d => {return d})
        .catch(error => console.log(error))
    
        palavra = response.palavra
        dicas = response.dicas

    comecar()
        
}

function comecar(){
    gerar_linhas()
}

function dica(){
    var div = document.getElementById("dicadiv")
    var tent = document.getElementById("tentativas")
    if (tentativas >= 1){
        if (dicas.length > 0){
            div.innerHTML = 'dicas:' + dicas.pop()
            tentativas -= 1
            tent.innerHTML = tentativas
        }else{
            div.innerHTML = "dicas foram esgotadas"
        }
            
    }else{
        div.innerHTML = "tentativas insuficientes"
    }
}
function gerar_linhas(){

    var tent = document.getElementById("tentativas")
    var btnd = document.getElementById('dicabtn')
    var tab = document.getElementById("tabela")
    tab.replaceChildren([])
    var tr = document.createElement("tr")
    var inp = document.getElementById("chute")
    var btn = document.getElementById("chutebtn")
    tentativas = 5
    tent.innerHTML = tentativas
    inp.readOnly = false
    inp.value = ''
    btnd.hidden = false
    btn.innerHTML = 'chute',btn.onclick = function(){chutar()}

    for (i in palavra){

        tr.appendChild(gerar_letra(id=i))
        if ((Number(i) + 1)%10 === 0){
            tab.appendChild(tr)
            tr = document.createElement("tr")
        }
    }
    tab.appendChild(tr)
}
function gerar_letra(id){

    var td = document.createElement("td")
    var div = document.createElement("div")

    div.id = id,div.className ="div_menor"
    td.appendChild(div)
    return td

}
function chutar(){
    var p = document.getElementById("chute")
    var text = p.value.toLowerCase()
    var acerto = false
    p.value = ''
    for (i in palavra){
        if (text === palavra[i].toLowerCase()){
            var div = document.getElementById(i)
            div.innerHTML = palavra[i]
            acerto = true
        }
    }
    verificar_acerto()
    if (!(acerto)){
        var tent = document.getElementById("tentativas")
        var num = Number(tent.innerText)
        if (num > 0){
            tent.innerHTML = num-1
            tentativas -= 1
        }else{
            var inp = document.getElementById("chute")
            var btn = document.getElementById("chutebtn")
            inp.readOnly = true
            inp.value = `Você perdeu, a palavra correta é:\n(${palavra})`
            btn.innerHTML = 'Jogar novamente',btn.onclick = function(){pegar_palavra()}
        }
    }
}

function verificar_acerto(){

    for (i in palavra){
        var div = document.getElementById(`${i}`)
        outpalavra += div.innerHTML
    }
    if (outpalavra === palavra){
        var btnd = document.getElementById('dicabtn')
        var inp = document.getElementById("chute")
        var btn = document.getElementById("chutebtn")
        inp.readOnly = true
        inp.value = `Você venceu, a palavra correta é:\n(${palavra})`
        btnd.hidden = true
        btn.innerHTML = 'Jogar novamente',btn.onclick = function(){pegar_palavra()}
    }else{
        outpalavra = ''
    }
}


pegar_palavra()