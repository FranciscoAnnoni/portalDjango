let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4] },
        { searchable: false, targets: [0] }
    ],
    pageLength: 4,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listProgrammers();

    dataTable = $("#datatable-programmers").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listProgrammers = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/app/list_programmers/");
        const data = await response.json();

        let content = ``;
        data.programmers.forEach((programmer, index) => {
            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${programmer.name}</td>
                    <td>${programmer.country}</td>
                    <td>${programmer.birthday}</td>
                    <td>${programmer.score}</td>
                </tr>`;
        });
        tableBody_programmers.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});