import axios from 'axios'

// Create an axios instance with a baseURL
const api = axios.create({
    baseURL: "http://localhost:8000"
})

export default api