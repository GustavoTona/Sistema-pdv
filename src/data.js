const divData = document.getElementById("divData")
const data = new Date()
 const horas = data.getHours()+":"+ data.getMinutes()+":"+ data.getSeconds()

const dataAtual = data.getDate()+"/"+data.getMonth()+"/"+data.getFullYear()+ " - " + horas 


divData.innerHTML = dataAtual