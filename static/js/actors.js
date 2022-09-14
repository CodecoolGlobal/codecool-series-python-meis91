let actors = document.querySelectorAll(".btn-actors");

for(let actor of actors){
    actor.addEventListener('click', (event) =>{
        let actorShows = document.getElementById("on-shows");
        console.log(event.target)
        console.log(actorShows)
        if(actorShows){actorShows.remove()};
        let actorId = event.target.getAttribute("data-actor-id");
        getActorSeries(actorId, event);
        });
    };

async function getActorSeries(actorId, event){
    let params = new URLSearchParams();
    params.set("actorId", actorId);
    let response = await fetch("/api/actors/show" + "?" + params.toString());
    let shows = await response.json();
    for(let show of shows){
        const node = document.createElement("dd");
        const textNode = document.createTextNode(`  - ${show.title}`);
        node.appendChild(textNode);
        node.setAttribute("id","on-shows");
        event.target.parentElement.appendChild(node);
    };


}

