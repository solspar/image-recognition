<template>
  <div id="app">
    <h1>Web client</h1>
    <div v-for="person in people">
      <h3>{{ person.name }}</h3>
      <img :src="person.photo" :alt="person.name + '\'s photo'">
    </div>
  </div>
</template>
<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator'

  interface Person {
    name: string
    photo: string
  }

  @Component
  export default class App extends Vue {
    private websocket!: WebSocket
    private people: Person[] = []

    created() {
      this.websocket = new WebSocket('ws://localhost:8080')

      this.websocket.onopen = (event) => {
        console.log('opened websocket connection')
      }

      this.websocket.onmessage = (event) => {
        console.log('Received message')
        const data = JSON.parse(event.data)
        console.log(data)

        this.people.push(data)
      }
    }
  }
</script>
<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
