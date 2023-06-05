echo "const express = require('express');
const sql = require('mssql');
const app = express();
const port = process.env.PORT || 3000;

const config = {
    user: 'aulafinaluser',
    password: 'Aulafinalpassword1',
    server: 'aulafinalserver.database.windows.net', 
    database: 'aulafinaldatabase',
    options: {
        encrypt: true
    }
};

app.get('/estudantes', function(req, res) {
    sql.connect(config).then(() => {
        return sql.query\`SELECT * FROM Estudantes\`;
    }).then(result => {
        res.send(result.recordset);
    }).catch(err => {
        res.status(500).send({ message: \`${err}\`});
    });
});

app.listen(port, () => {
    console.log('App running on http://localhost:' + port);
});" > app.js

