const list = document.getElementById("actors-birthday");


async function getActorsBirthday(){
    let html = "";
    let response = await fetch("/api/actors/birthday");
    let actors = await response.json();
    for(let actor of actors){
        html += `            
            <li  id="${actor.name}" data-birthday="${actor.bday_day}">
                <div class="tooltip"> ${actor.name}
                    <span class="tooltiptext">{actor.bday_day}</span>
</              </div>
            </li>
               
                `
    };
    list.innerHTML = html;
    let actorsList = document.querySelectorAll(".actors");
    console.log(actorsList);


};

getActorsBirthday();
