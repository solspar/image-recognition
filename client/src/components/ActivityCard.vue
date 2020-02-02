<template>
  <div class="card">
    <img :src="event.photo" :alt="event.name + '\'s photo'">
    <div class="card-description">
      <h4>{{ event.name }}</h4>
      <p>
        <span v-if="isArrival" class="arrival">arrived</span>
        <span v-if="!isArrival" class="departure">departed</span>
        @
        {{ event.time.format('hh:mma') }}
      </p>
    </div>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator'
  import { ActivityEvent, ActivityType } from '@/models/activity-event'

  @Component
  export default class ActivityCard extends Vue {
    @Prop() event!: ActivityEvent

    get isArrival(): boolean {
      return this.event.type === ActivityType.ARRIVAL
    }

  }
</script>

<style lang="scss" scoped>
  .card {
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
</style>
