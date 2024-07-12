function calculadora(x){
    var txt = document.getElementById("texto")
    switch (x) {
        case "AC":
            
            txt.innerText = ""
            break;
        case "=":
            try {
                txt.innerText = eval(calcular(txt.textContent))
            } catch (error) {
                console.log("tem que ser muito burro mermo.")
            }
            

            break;
    
        default:
                txt.innerText = txt.textContent+x
            break;
    }

}
function calcular(equ){
    new_equ = ""
    for (i in equ){
        if (equ[i] === "÷" || equ[i] === "×"){
            new_equ += formatar(equ[i])
            continue
        }
        new_equ += equ[i]

    }
    return new_equ
}
function percorrer(palavra){
    letra = ""
    for (i in palavra){
        letra = palavra[i]
    }
    return letra
}
function formatar(x){
    switch (x) {
        case "÷":
            return "/"
            break;
        
        case "×":
            return "*"
        default:

            break;
    }
}