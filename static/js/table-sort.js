/**
 * Sorts a HTML table
 *
 * @param {HTMLTableElement}
 * @param {number}
 * @param {boolean}
 */

function tableSort(table, column, asc= true){
    const directionModifier = asc ? 1 : -1;
    const tableBody = table.tBodies[0];
    const rows = Array.from(tableBody.querySelectorAll("tr"));
    console.log(rows)


//    Sort each row
    const sortedRows = rows.sort((a, b) => {
        const aColText = a.querySelector(`td:nth-child(${column + 1})`).textContent.trim();
        const bColText = b.querySelector(`td:nth-child(${column + 1})`).textContent.trim();

        return aColText > bColText ? (1 * directionModifier) : (-1 * directionModifier);
    });

//    Remove all existing TRs from table
    while (tableBody.firstChild){
        
        tableBody.removeChild(tableBody.firstChild);
    }
//    Re-add the sorted rows
    tableBody.append(...sortedRows);

//    Remember how the colum is sorted at the moment
    table.querySelectorAll("th").forEach(th => th.classList.remove("th-sort-asc", "th-sort-desc"));
    table.querySelector(`th:nth-child(${column +1})`).classList.toggle("th-sort-asc", asc);
    table.querySelector(`th:nth-child(${column +1})`).classList.toggle("th-sort-desc", !asc);
}

document.querySelectorAll(".table-sortable th").forEach(headerCell => {
   headerCell.addEventListener("click", () =>{
      const tableElement = headerCell.parentElement.parentElement.parentElement;
      const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
      const currentIsAscending = headerCell.classList.contains("th-sort-asc");

      tableSort(tableElement, headerIndex, !currentIsAscending);
   });
});