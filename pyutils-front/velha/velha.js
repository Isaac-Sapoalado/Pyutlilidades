
var vez = 1


function inicio(){
    var conjunto = document.getElementsByName("divitem")
    var div = document.getElementById("vez")
    div.onclick = ''
    div.innerHTML = 'Vez: player 1'
    vez = 1
    for (i=0;i<9;i++){
        conjunto[i].innerHTML = ''
    }


}



function marcar(id){
    var div = document.getElementById(`${id}`)
    var vez_text = document.getElementById("vez")
    if (div.innerHTML === ''){
        if (vez === 1){
            div.innerHTML = 'X'
            if (verificar_vitoria()){
                vez_text.innerHTML = 'Vitoria do player 1<br>(Clique aqui para jogar novamente)'
                vez = 0
            }else{
                vez_text.innerHTML = 'Vez: player 2'
                vez = -1
            }
            
        }else{
            if (vez === -1){
                div.innerHTML = 'O'
                if (verificar_vitoria()){
                    vez_text.innerHTML = 'Vitoria do player 2<br>(Clique aqui para jogar novamente)'
                    vez = 0
                }else{
                    vez_text.innerHTML = 'Vez: player 1'
                    vez = 1
                }
            }
        }
        if (vez === 0){
            fim()
        }
    }
}

function fim(){
    var div = document.getElementById("vez")
    div.onclick = function(){
        inicio()
    }
}

function verificar_vitoria(){

    var conjunto = document.getElementsByName("divitem")
    //conjunto chato de if's
    {
    if (conjunto[2].innerHTML === conjunto[1].innerHTML && conjunto[1].innerHTML === conjunto[0].innerHTML && !(conjunto[0].innerHTML === '')){
        return true

        }
    if (conjunto[6].innerHTML === conjunto[3].innerHTML && conjunto[3].innerHTML === conjunto[0].innerHTML && !(conjunto[0].innerHTML === '')){
        return true
        }
    if (conjunto[8].innerHTML === conjunto[4].innerHTML && conjunto[4].innerHTML === conjunto[0].innerHTML && !(conjunto[0].innerHTML === '')){
        return true
        }
    if (conjunto[2].innerHTML === conjunto[4].innerHTML && conjunto[4].innerHTML === conjunto[6].innerHTML && !(conjunto[6].innerHTML === '')){
        return true
        }
    if (conjunto[1].innerHTML === conjunto[4].innerHTML && conjunto[4].innerHTML === conjunto[7].innerHTML && !(conjunto[7].innerHTML === '')){
        return true
        }
    if (conjunto[3].innerHTML === conjunto[4].innerHTML && conjunto[4].innerHTML === conjunto[5].innerHTML && !(conjunto[5].innerHTML === '')){
        return true
        }
    if (conjunto[8].innerHTML === conjunto[7].innerHTML && conjunto[7].innerHTML === conjunto[6].innerHTML && !(conjunto[6].innerHTML === '')){
        return true
        }
    if (conjunto[2].innerHTML === conjunto[5].innerHTML && conjunto[5].innerHTML === conjunto[8].innerHTML && !(conjunto[8].innerHTML === '')){
        return true
        }
    }
}