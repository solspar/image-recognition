import moment from 'moment'

export enum ActivityType {
  ARRIVAL,
  DEPARTURE
}

export interface ActivityEvent {
  name: string
  photo: string
  time: moment.Moment
  type: ActivityType
}
