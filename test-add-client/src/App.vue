<template>
  <div id="app">
    <h1>Raspberry pi data</h1>

    <button @click="send()">Send data</button>
  </div>
</template>
<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator'

  @Component
  export default class App extends Vue {
    private websocket!: WebSocket;

    created() {
      this.websocket = new WebSocket('ws://localhost:8080')

      this.websocket.onopen = (event) => {
        console.log('connected')
      }

      this.websocket.onmessage = (event) => {
        console.log('recieved message ')
        console.log(event)
      }
    }

    send() {
      this.websocket.send(JSON.stringify({
        name: 'Jimmy smith',
        photo: 'https://picsum.photos/200/300'
      }))
    }
  }
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
