<template>
  <transition name="slide-fade">
    <div v-if="notification !== null && isArrival" class="notification arrival">
      <img :src="notification.photo" :alt="notification.name + '\'s photo'">
      <div class="description">
        <h4>Welcome <strong>{{ notification.name }}</strong></h4>
        <p>We hope you have a productive time ❤️</p>
      </div>
    </div>
    <div v-if="notification !== null && !isArrival" class="notification departure">
      <img :src="notification.photo" :alt="notification.name + '\'s photo'">
      <div class="description">
        <h4>Goodbye <strong>{{ notification.name }}</strong></h4>
        <p>Have a great rest of your day 😀</p>
      </div>
    </div>
  </transition>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator'
  import { ActivityType } from '@/models/activity-event'
  import { Notification } from '@/models/notification'

  @Component
  export default class NotificationSnackbar extends Vue {
    @Prop() notification: Notification | null = null

    get isArrival(): boolean {
      return this.notification !== null && this.notification.type === ActivityType.ARRIVAL
    }
  }
</script>

<style lang="scss" scoped>

  .slide-fade-enter-active {
    transition: all .3s ease;
  }

  .slide-fade-leave-active {
    transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
  }

  .slide-fade-enter, .slide-fade-leave-to {
    transform: translateY(100px);
    opacity: 0;
  }

  .notification.arrival {
    border: 1px solid rgba(20, 125, 100, 0.6);
  }

  .notification.departure {
    border: 1px solid rgba(231, 124, 124, 0.6);
  }

  .notification {
    position: fixed;
    z-index: 1;
    width: 700px;
    margin-left: -350px;
    left: 50%;
    bottom: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);

    /*border: 1px solid rgba(20, 125, 100, 0.6);*/
    border-radius: 75px;

    padding: 1rem 1rem;

    display: flex;

    img {
      width: 90px;
      height: 90px;
      border-radius: 50px;
    }

    .description {
      display: flex;
      flex-direction: column;
      justify-content: space-evenly;

      margin-left: 1rem;

      font-family: 'Open Sans', sans-serif;

      h4 {
        font-size: 24px;
        margin-top: 0;
        margin-bottom: 0;
        font-weight: 300;

        strong {
          font-weight: 600;
        }
      }

      p {
        color: rgba(0, 0, 0, 0.8);
        font-size: 18px;
        font-weight: 300;
        margin-top: 0;
        margin-bottom: 0;
      }
    }
  }
</style>
