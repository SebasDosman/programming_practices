const api = 'https://jsonplaceholder.typicode.com/users/1';

axios.get(api)
    .then((response) => console.log(response.data))
    .catch(err => console.log(err));