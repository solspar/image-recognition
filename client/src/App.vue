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
          <div class="activity-card" v-for="event in activity">
            <img :src="event.photo" :alt="event.name + '\'s photo'">
            <div class="card-description">
              <h4>{{ event.name }}</h4>
              <p>
                <span v-if="isArrival(event)" class="arrival">arrived</span>
                <span v-if="!isArrival(event)" class="departure">departed</span>
                @
                {{ event.time.format('hh:mma') }}
              </p>
            </div>
          </div>
        </div>
      </aside>
    </main>
  </div>
</template>
<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator'
  import moment from 'moment'
  import { Person } from '@/models/person'
  import PersonCard from '@/components/PersonCard.vue'

  enum ActivityType {
    ARRIVAL,
    DEPARTURE
  }

  interface ActivityEvent {
    name: string
    photo: string
    time: moment.Moment
    type: ActivityType
  }

  @Component({
    components: {PersonCard}
  })
  export default class App extends Vue {
    private websocket!: WebSocket
    private people: Person[] = []
    private activity: ActivityEvent[] = []

    constructor() {
      super()
      // this.people = [
      //   {
      //     name: 'James Smith',
      //     photo: 'https://c8.alamy.com/comp/EDG6K4/handsome-young-man-opening-door-to-enter-into-a-room-looking-down-EDG6K4.jpg',
      //     arrival: moment.utc('10:00', 'hh:mm').local(),
      //   },
      //   {
      //     name: 'Jasmine Puri',
      //     photo: 'https://previews.123rf.com/images/lacheev/lacheev1908/lacheev190800150/129645964-cheerful-young-woman-inviting-people-to-enter-in-home-girl-blonde-opening-her-house-front-door.jpg',
      //     arrival: moment.utc('14:00', 'hh:mm').local()
      //   },
      //   {
      //     name: 'Evan Rupert',
      //     photo: 'https://www.seekpng.com/png/detail/133-1333195_man-walking-through-door-walk-through-clip-art.png',
      //     arrival: moment.utc('20:30', 'hh:mm')
      //   },
      //   {
      //     name: 'Varun Puri',
      //     photo: 'https://www.realitybasedleadership.com/wp-content/uploads/2016/07/Open-Door-Policy.jpg',
      //     arrival: moment.utc('21:43', 'hh:mm')
      //   }
      // ]

      // this.activity = [
      //   {
      //     name: 'James Smith',
      //     photo: 'https://c8.alamy.com/comp/EDG6K4/handsome-young-man-opening-door-to-enter-into-a-room-looking-down-EDG6K4.jpg',
      //     time: moment.utc('8:00', 'hh:mm'),
      //     type: ActivityType.ARRIVAL
      //   },
      //   {
      //     name: 'James Smith',
      //     photo: 'https://c8.alamy.com/comp/EDG6K4/handsome-young-man-opening-door-to-enter-into-a-room-looking-down-EDG6K4.jpg',
      //     time: moment.utc('8:20', 'hh:mm'),
      //     type: ActivityType.DEPARTURE
      //   },
      //   {
      //     name: 'James Smith',
      //     photo: 'https://c8.alamy.com/comp/EDG6K4/handsome-young-man-opening-door-to-enter-into-a-room-looking-down-EDG6K4.jpg',
      //     time: moment.utc('8:30', 'hh:mm'),
      //     type: ActivityType.ARRIVAL
      //   },
      //   {
      //     name: 'Jasmine Puri',
      //     photo: 'https://previews.123rf.com/images/lacheev/lacheev1908/lacheev190800150/129645964-cheerful-young-woman-inviting-people-to-enter-in-home-girl-blonde-opening-her-house-front-door.jpg',
      //     time: moment.utc('14:00', 'hh:mm'),
      //     type: ActivityType.ARRIVAL
      //   },
      //   {
      //     name: 'Evan Rupert',
      //     photo: 'https://www.seekpng.com/png/detail/133-1333195_man-walking-through-door-walk-through-clip-art.png',
      //     time: moment.utc('20:30', 'hh:mm'),
      //     type: ActivityType.ARRIVAL
      //   },
      //   {
      //     name: 'Varun Puri',
      //     photo: 'https://www.realitybasedleadership.com/wp-content/uploads/2016/07/Open-Door-Policy.jpg',
      //     time: moment.utc('22:03', 'hh:mm'),
      //     type: ActivityType.ARRIVAL
      //   }
      // ]
    }

    isArrival(event: ActivityEvent): boolean {
      return event.type === ActivityType.ARRIVAL
    }

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
    }

    depart(name: string, photo: string) {
      this.people = this.people.filter(person => person.name !== name)

      this.activity.push({
        name,
        photo,
        time: moment.utc().local(),
        type: ActivityType.DEPARTURE
      })
    }
  }
</script>
<style lang="scss">
  @import url('https://fonts.googleapis.com/css?family=Open+Sans|Roboto&display=swap');

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

  .activity-card {
    display: flex;

    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    border-radius: 15px;
    padding: 0.5rem 1rem;
    margin-bottom: 1rem;

    img {
      width: 50px;
      height: 50px;
      border-radius: 50px;
    }

    .card-description {
      display: flex;
      justify-content: space-evenly;
      flex-direction: column;
      margin-left: 1rem;

      font-family: 'Open Sans', sans-serif;

      h4 {
        /*margin-top: 0.5rem;*/
        margin-top: 0;
        margin-bottom: 0;
      }

      p {
        margin-top: 0;
        margin-bottom: 0;

        color: rgba(0, 0, 0, 0.5);

        span.arrival {
          color: #147D64;
        }

        span.departure {
          color: #D64545;
        }
      }
    }
  }

  aside {
    width: 30%;
  }

  h2 {
    font-family: 'Roboto', sans-serif;
  }
</style>
