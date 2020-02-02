import { ActivityType } from '@/models/activity-event'

export interface Notification {
  name: string
  photo: string
  type: ActivityType
}
