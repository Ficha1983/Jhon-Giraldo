const fetch = require('node-fetch');

fetch('http://localhost:8000/api/productos/')
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));
