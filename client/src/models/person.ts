import moment from 'moment'

export interface Person {
  name: string
  photo: string
  arrival: moment.Moment
}
