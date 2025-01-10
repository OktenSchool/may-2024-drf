const baseURL = '/api'

const auth = '/auth'
const pizzas = '/pizzas'

const urls = {
    auth: {
        login: auth,
        socket: `${auth}/socket`
    },
    pizzas
}

export {
    baseURL,
    urls
}