
var foco;
async function post(texto,conc){
    await fetch(
        "http://127.0.0.1:8000/api/tarefa/",{
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify({
                'tarefa':texto,
                'feito':conc
            })
        }
    
        )
        .catch(error => console.log(error))
}

async function put(texto,conc,pk){
    await fetch(
        "http://127.0.0.1:8000/api/tarefa/"+pk,{
            method: 'PUT',
            mode: 'cors',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify({
                'tarefa':texto,
                'feito':conc
            })
        }
    
        )
        .catch(error => console.log(error))
}

async function del(pk){
    await fetch(
        "http://127.0.0.1:8000/api/tarefa/"+pk,{
            method: 'DELETE',
            mode: 'cors',
            headers: {
                'Content-Type':'application/json'
            }
        }
    
        )
        .catch(error => console.log(error))
}


async function get() {
    var recebe;
    var v = await fetch(
    "http://127.0.0.1:8000/api/tarefa/",{
        method: 'GET',
        mode: 'cors',
        headers: {
            'Content-Type':'application/json'
        }
    }

    )
    .then(Response => Response.json()).then(data => {
        recebe = data
    })
    .catch(error => console.log(error))
    
    for (i in recebe){
        obj = [
            recebe[i].tarefa,
            recebe[i].feito,
            recebe[i].pk
            ]
        adcionar(obj)

    }
}

function adcionar(objec=false){
    var conteiner = document.getElementById("div_tarefa")
    if (objec === false){
        var texto = document.getElementById("txt_area")
        
        var txt = texto.value
        if (txt != ""){
            gerar_linha(txt,conteiner,false,novo=true)
            texto.value = ""
            }
    }else{
        gerar_linha(seq=obj[0],chave=obj[2],bol=obj[1])
    }
    
    

}

function gerar_linha(seq,chave,bol,novo=false){
    //inicializado variaveis importantes
    {
    var container = document.getElementById("div_tarefa")
    var img1 = document.createElement("img")
    var img2 = document.createElement("img")
    var box = document.createElement("input")
    var div1 = document.createElement("div")
    var div2 = document.createElement("div")
    var div3 = document.createElement("div")

    div3.className = "divlinha",div3.id=chave
    }
    //configurando icones
    {
    img1.src = "static/editar.png"
    img1.width,img1.height = 30
    img1.onclick = function (){
        editar(div3.id)
    }
    img2.src = "static/lixeira.png"
    img2.width,img2.height = 30
    img2.onclick = function (){
        deletar(div3.id)
    }
    }
    
    box.type = "checkbox",box.name = String('box' + div3.id),box.checked = bol
    box.onclick = function(){
        editar(div3.id,box.checked)
    }
    div1.append(seq)
    div2.appendChild(img1),div2.appendChild(img2),div2.appendChild(box)
    div3.appendChild(div1),div3.appendChild(div2)
    container.appendChild(div3)
    filtrar()
    if (novo){
        post(texto=seq,conc=bol)
    }
    

}

function editar(id,checke=null) {

    var div = document.getElementById(id)
    var text = String(div.firstChild.innerHTML)
    if (checke != null){

        
        put(text,checke,id)

    }else{
        var texto = prompt("novo texto")
        var caixa = document.getElementsByName("box"+id)
        caixa = caixa[0].checked
        if (texto != "" && texto != text){
            var conteiner = document.getElementById("div_tarefa")
            div.children.item(0).innerHTML = texto
            put(texto,caixa,id)
        }
    }
    filtrar()

}

function deletar(id){
    var conteiner = document.getElementById("div_tarefa")
    var div = document.getElementById(id)
    conteiner.removeChild(div)
    del(pk=id)
}


///nao mexer
function trocar_foco(id){
    if (foco != id){
        foco = id
    }
    var b = document.getElementById(id)
    var d = document.getElementsByClassName("segment_button")
    for (i=0;i<d.length; i++){
        d[i].style.backgroundColor = "rgb(27, 27, 27)";
        d[i].style.borderBottom ="none";
    }
    b.style.backgroundColor = "rgb(20, 20, 20)"
    b.style.borderBottom ="1px solid rgb(270, 270, 270)"
    filtrar()
}

function filtrar(){
    
    var conteiner = document.getElementsByClassName("divlinha")
    for (i=0;i<conteiner.length; i++){
        var div = conteiner.item(i)
        box = div.children[1].children[2].checked
        div.style.display = "flex"
        if (foco === "em_andamento" && box==true){
            div.style.display = "none"
        }
        if (foco === "concluido" && box==false){
            div.style.display = "none"
        }
    }
}

get()
