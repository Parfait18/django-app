import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import axios from 'axios';


const axiosInstance = axios.create({
	baseURL: `http://localhost:8000/`,
	xstfCookieName: 'csrftoken',
	xsrfHeaderName: 'X-CSRFToken',
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json',

		//	'X-CSRFCOOKIE': 'django-vuejs-app',
		//	'X-CSRFTOKEN': '{{ csrf_token }}'
	},
	withCredentials: true
});
const app = createApp(App)

app.config.globalProperties.axios = { ...axiosInstance }
app.mount('#app')
