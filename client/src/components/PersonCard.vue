<template>
  <div class="card">
    <img :src="person.photo" :alt="person.name + '\'s photo'">
    <div class="card-description">
      <h4>{{ person.name }}</h4>
      <p>{{ humanTime }}</p>
    </div>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator'
  import { Person } from '@/models/person'
  import moment from 'moment'

  @Component
  export default class PersonCard extends Vue {
    @Prop() person!: Person
    private humanTime: string = ''

    created() {
      this.humanTime = this.humanizeTime(this.person.arrival)

      setInterval(() => {
        this.humanTime = this.humanizeTime(this.person.arrival)
      }, 1000)
    }

    humanizeTime(time: moment.Moment): string {
      return 'hard at work for ' + time.fromNow(true)
    }
  }
</script>

<style lang="scss" scoped>
  .card {
    margin-right: 3rem;
    margin-bottom: 3rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    border-radius: 15px;

    img {
      height: 150px;
      width: 230px;
      border-top-left-radius: 15px;
      border-top-right-radius: 15px;
    }

    .card-description {
      margin-left: 1rem;
      margin-top: 0.25rem;
      margin-bottom: 0.5rem;

      font-family: 'Open Sans', sans-serif;

      h4 {
        margin-top: 0;
        margin-bottom: 0;
        font-weight: 600;
      }

      p {
        color: rgba(black, 0.5);
        font-style: normal;
        font-weight: 300;
        font-size: 14px;

        margin-top: 0.25rem;
        margin-bottom: 0.25rem;
      }
    }
  }
</style>
