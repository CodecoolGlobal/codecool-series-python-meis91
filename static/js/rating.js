
async function getSeriesRating() {
    const tbody = document.getElementsByClassName("tbody")[0];
    let htmlTable = ""
    let response = await fetch("/api/rating");
    let shows = await response.json();
    for (let show of shows) {
        htmlTable += `
                    <tr>
                        <td>${ show['title'] }</td>
                        <td>${ show['actor_count'] }</td>
                        <td>${ show['rating_average'] }</td>
                    </tr>  
                    `
    };
    tbody.innerHTML = htmlTable;
};

getSeriesRating();

