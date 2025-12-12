const botao = document.getElementById("seleciona-tema")
// const icon = document.getElementById("icons")

botao.addEventListener("click", () => {
    const atual = document.documentElement.getAttribute("data-theme");
    const novo = atual === "escuro" ? "claro" : "escuro";
    document.documentElement.setAttribute("data-theme", novo);
    localStorage.setItem("tema", novo);
    // document.body.classList.toggle("escuro");
    // const escuro = document.body.classList.contains("escuro")
    // // icon.src = escuro ? "imagens/sol.ico" : "imagens/lua.svg";
    // localStorage.setItem("temas", escuro? "escuro" : "claro");
});

//APLICA TEMA SALVO
const saved = localStorage.getItem("temas")
// if (saved === "escuro"){
//     document.body.classList.add("escuro");}
if (salvo) {
document.documentElement.setAttribute("data-theme", salvo);
}
