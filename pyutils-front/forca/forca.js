const palavra = "palavra"
var outpalavra = ''
var tentativas = 5

function gerar_linhas(){

    var tab = document.getElementById("tabela")
    tab.replaceChildren([])
    var tr = document.createElement("tr")
    var inp = document.getElementById("chute")
    var btn = document.getElementById("chutebtn")
    inp.readOnly = false
    inp.value = ''
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
        if (text === palavra[i]){
            var div = document.getElementById(i)
            div.innerHTML = text
            verificar_acerto()
            acerto = true
        }
    }
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
            btn.innerHTML = 'Jogar novamente',btn.onclick = function(){gerar_linhas()}
        }
    }
}

function verificar_acerto(){

    for (i in palavra){
        var div = document.getElementById(`${i}`)
        outpalavra += div.innerHTML
    }
    if (outpalavra === palavra){
        var inp = document.getElementById("chute")
            var btn = document.getElementById("chutebtn")
            inp.readOnly = true
            inp.value = `Você venceu, a palavra correta é:\n(${palavra})`
            btn.innerHTML = 'Jogar novamente'
    }else{
        outpalavra = ''
    }
}


gerar_linhas()