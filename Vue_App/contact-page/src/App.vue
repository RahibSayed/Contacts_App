<template>
  <div class="container">
    <Header title="Contacts" @toggle-add-contact="toggleAddContact" :showAddContact="showAddContact"/>
    <Search @search-contact="searchContact"/>
    <div v-if="showAddContact">
      <AddContact @add-contact="addContact"/>
    </div>
    <Contacts @update= updateContact @delete-contact="deleteContact" :contacts="contacts" />
  </div>
</template>

<script>
import Header from './components/Header'
import Contacts from './components/Contacts'
import AddContact from './components/AddContact'
import Search from './components/Search'

export default {
  name: 'App',
  components: {
    Header,
    Contacts,
    AddContact,
    Search
  },
  data(){
    return {
      contacts: [],
      showAddContact: false
    }
  },
  methods: {
    async fetchContacts(){
      const result = await fetch('/contact')
      const data = await result.json()
      return data
    },
    async fetchContact(id){
      const result = await fetch(`/contact/${id}`)
      const data = await result.json()
      return data
    },
    async deleteContact(id){
      if(confirm('Are you sure?')){
        const result = await fetch(`/contact/${id}`,{method: 'DELETE'})
        result.status == 204 ? (this.contacts = this.contacts.filter((contact) => contact.id !== id)) : alert('Error deleting contact')
      }
    },
    async addContact(contact){
      const result = await fetch('/contact', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(contact)
      })

      const data = await result.json()
      const code = await result

      console.log(data)

      if(code.status !== 201){
        alert('Error creating contact')
        return
      }

      this.contacts = [...this.contacts, data]
    },
    toggleAddContact(){
      this.showAddContact = !this.showAddContact
    },
    async searchContact(search){
      const result = await fetch(`/contact/name?name=${search}`, {
        method: 'GET'
      })

      const data = await result.json()
      const code = await result

      if(code.status !== 200){
        alert('Error finding contact')
        return
      }

      this.contacts = data
    }
  },
  async created(){
    this.contacts = await this.fetchContacts()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: 'Poppins', sans-serif;
}
.container {
  max-width: 40%;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}
.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}
</style>