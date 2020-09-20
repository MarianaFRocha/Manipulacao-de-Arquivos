XLSX = require('xlsx');

const path = require('path');
const fs = require('fs');
const directoryPath = path.join(__dirname, 'UserDefinition');

// let fileName = "FM4FSUMD-04Struct"

// const workBook = XLSX.readFile("\UserDefinition\\" + fileName + ".xls");
// XLSX.writeFile(workBook, fileName + ".csv", { bookType: "csv" });

fs.readdir(directoryPath, function (files) {
    files.forEach(function (file) {
        let fileName = file.toString()
        fileName = fileName.substr(0, fileName.length -4);

        const workBook = XLSX.readFile("\UserDefinition\\" + fileName + ".xls");
        XLSX.writeFile(workBook, fileName + ".csv", { bookType: "csv" });

        console.log(fileName);
    });
});