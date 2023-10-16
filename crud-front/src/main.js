import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import axios from 'axios';


const baseURL = 'http://localhost:8000/'

const axiosInstance = axios.create({
	baseURL: `${baseURL}`,
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json',
		'Access-Control-Allow-Origin': '*',
		"Access-Control-Allow-Headers": "*", // this will allow all CORS requests
		"Access-Control-Allow-Methods": 'OPTIONS,POST,GET', // this states the allowed methods
		"Content-Type": "application/json" // this shows the expected content type

		//	'X-CSRFCOOKIE': 'django-vuejs-app',
		//	'X-CSRFTOKEN': '{{ csrf_token }}'
	},
	//	withCredentials: true
});
const app = createApp(App)

app.config.globalProperties.axios = { ...axiosInstance }
app.mount('#app')
