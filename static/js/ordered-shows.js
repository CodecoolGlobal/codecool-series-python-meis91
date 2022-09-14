const tableBody = document.getElementsByClassName("tbody")[0];
const titleHeader = document.getElementById("title")

console.log(tableBody);


titleHeader.addEventListener("click", function(){
    let direction = titleHeader.getAttribute("data-direction");
    console.log(direction)
    if (direction == "DESC"){
        titleHeader.setAttribute("data-direction","ASC");
        let newDirection = titleHeader.getAttribute("data-direction");
        console.log(newDirection);
        orderedShows(newDirection);
    } else {
        titleHeader.setAttribute("data-direction","DESC");
        console.log(titleHeader.getAttribute("data-direction"));
        let newDirection = "DESC";
        orderedShows(newDirection);
    };
});


async function orderedShows(direction){
    let html = "";
    let params = new URLSearchParams();
    params.set("direction", direction);
    let response = await fetch("api/ordered-shows" + "?" + params.toString());
    let shows = await response.json();
    console.log(shows)
    for(let show of shows){
       html +=  ` <tr>
                    <td>${show.title}</td>
                    <td>${show.episode_count}</td>
                    <td>${show.rating}</td>
                </tr> `
    };
    tableBody.innerHTML = html;
};


orderedShows(direction="DESC")