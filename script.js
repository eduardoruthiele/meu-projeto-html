console.log("Página carregada");

const itens = document.querySelectorAll(".ranking-tenistas li");

itens.forEach((item) => {
  item.addEventListener("click", () => {
    item.style.backgroundColor = "#d9ffd9";
    setTimeout(() => {
      item.style.backgroundColor = "";
    }, 300);
  });
});
