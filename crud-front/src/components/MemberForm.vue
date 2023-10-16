<script lang="js">
export default {
	name: "MemberForm",
	data() {
		return {
			firstname: 'Parfait',
			lastname: 'AHOUANTO',
			phone: '66301160',
			email: 'parfaitsv@gmail.com',
			errors_messages: []
		}
	},
	methods: {
		saveMember() {
			const payload = new FormData()
			payload.append('firstname', this.firstname)
			payload.append('lastname', this.lastname)
			payload.append('email', this.email)
			payload.append('phone', this.phone)

			this.axios.post('member/', payload).then((result) => {
				console.log(result)
			}).catch((error) => {
				console.log(error)
			})
			console.log('ezez')

		}
	},
	watch: {
	}


}
</script>

<template>
	<div class="card bg-white mx-auto md:w-8/12 w-full p-4 shadow-md rounded">
		<h4 class="text-gray-600 text-2xl font-bold"> Formulaire de creation de membre</h4>
		<form method="POST" class="p-2">
			<span v-if="errors_messages"> {{ errors_messages }}</span>
			<div class="mb-2">
				<label for="firstname" class="block mb-1"> Prénom</label>
				<input v-model="firstname" type="text" name="firstname"
					class="rounded p-2 border w-full border-gray-500 focus:outline-none focus:shadow-outline">
			</div>
			<div class="mb-2">
				<label for="lastname" class="block mb-1"> Nom</label>
				<input v-model="lastname" type="text" name="lastname"
					class="rounded w-full  p-2 border border-gray-500 focus:outline-none focus:shadow-outline">
			</div>
			<div class="mb-2">
				<label for="email" class="block mb-1"> Email</label>
				<input v-model="email" type="email" name="email"
					class="rounded w-full p-2 border border-gray-500 focus:outline-none focus:shadow-outline">
			</div>
			<div class="mb-2">
				<label for="phone" class="block mb-1"> Téléphone</label>
				<input type="phone" v-model="phone" name="phone"
					class="rounded w-full p-2 border border-gray-500 focus:outline-none focus:shadow-outline">
			</div>
			<button @click="saveMember"
				class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
				type="button">
				Enregistrer
			</button>



		</form>

	</div>
</template>

<style scoped>
.read-the-docs {
	color: #888;
}
</style>
