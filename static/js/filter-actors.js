const searchInput = document.getElementById("actor-name");
const list = document.getElementById("actors")
let searchTerm = "";

searchInput.addEventListener('input', event =>{
    let searchGenre = document.getElementById("genre-choice").value;
    searchTerm = event.target.value;
    getActor(searchGenre, searchTerm);
});

async function getActor(searchGenre, searchTerm){
    let html = ""
    let params = new URLSearchParams();
    params.set("genre", searchGenre);
    params.set("actor", searchTerm);
    let response = await fetch("api/search/actor" + "?" + params.toString());
    let result = await response.json();

    for(let actor of result){
        html += `
            <li>${actor.name}</li>
        `
    };
    list.innerHTML = html;
};