import axios from 'axios';
//import Vue from 'vue';


Vue.prototype.$http = axios

const api = axios.create({
	baseURL: `https://localhost:8000/`,
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
	}
});

export default {api}
