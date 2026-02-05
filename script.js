function checkURL(){
    let url = document.getElementById("urlInput").value;

    fetch("/check",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({url:url})
    })
    .then(res=>res.json())
    .then(data=>{
        let box = document.getElementById("resultBox");
        box.innerHTML = data.result;
        box.className = data.status;
    });
}
