const api = 'https://jsonplaceholder.typicode.com/users/1';

fetch(api)
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(err => console.log(err))

