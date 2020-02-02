import {ActivityType} from "@/models/activity-event";
import {ActivityType} from "@/models/activity-event";
<template>
  <div id="app">
    <header>
      <h1>CHEQIN</h1>
    </header>
    <main>
      <section>
        <h2>On deck</h2>
        <div class="people-container">
          <PersonCard v-for="person in people" :person="person"></PersonCard>
        </div>
      </section>
      <aside>
        <h2>Activity</h2>
        <div class="activity-container">
          <ActivityCard v-for="event in activity" :event="event"></ActivityCard>
        </div>
      </aside>
    </main>
    <NotificationSnackbar :notification="notification"></NotificationSnackbar>
  </div>
</template>
<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator'
  import moment from 'moment'
  import { Person } from '@/models/person'
  import PersonCard from '@/components/PersonCard.vue'
  import { ActivityEvent, ActivityType } from '@/models/activity-event'
  import ActivityCard from '@/components/ActivityCard.vue'
  import NotificationSnackbar from '@/components/NotificationSnackbar.vue'
  import { Notification } from '@/models/notification'

  @Component({
    components: {NotificationSnackbar, ActivityCard, PersonCard}
  })
  export default class App extends Vue {
    private websocket!: WebSocket
    private people: Person[] = []
    private activity: ActivityEvent[] = []
    private notification: Notification | null = null

    created() {
      this.websocket = new WebSocket('ws://localhost:8080')

      this.websocket.onopen = (event) => {
        console.log('opened websocket connection')
      }

      this.websocket.onmessage = (event) => {
        console.log('Received message')
        const data = JSON.parse(event.data)
        console.log(data)

        if (this.personExists(data.name))
          this.depart(data.name, data.photo)
        else
          this.arrive(data.name, data.photo)
      }
    }

    personExists(name: string): boolean {
      return this.people.some(person => person.name === name)
    }

    arrive(name: string, photo: string) {
      this.people.push({
        name,
        photo,
        arrival: moment.utc().local()
      })

      this.activity.push({
        name,
        photo,
        time: moment.utc().local(),
        type: ActivityType.ARRIVAL
      })

      this.showNotification(name, photo, ActivityType.ARRIVAL)
    }

    depart(name: string, photo: string) {
      this.people = this.people.filter(person => person.name !== name)

      this.activity.push({
        name,
        photo,
        time: moment.utc().local(),
        type: ActivityType.DEPARTURE
      })

      this.showNotification(name, photo, ActivityType.DEPARTURE)
    }

    showNotification(name: string, photo: string, type: ActivityType) {
      this.notification = {
        name,
        photo,
        type
      }

      setTimeout(() => {
        this.notification = null
      }, 2000)
    }
  }
</script>
<style lang="scss">
  @import url('https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700|Roboto&display=swap');

  * {
    box-sizing: border-box;
  }

  header {
    h1 {
      font-family: 'Roboto', sans-serif;
      font-size: 54px;
      margin-left: 5rem;
    }
  }

  main {
    display: flex;
    width: 90%;
    margin-left: 5%;
    margin-right: 5%;
    margin-top: 4rem;
  }

  section {
    width: 70%;
  }

  .people-container {
    display: flex;
    flex-wrap: wrap;
  }

  .activity-container {
    display: flex;
    flex-direction: column;
  }

  aside {
    width: 30%;
  }

  h2 {
    font-family: 'Roboto', sans-serif;
  }
</style>
