import { useContext } from "react"
import { NotificationContext } from "./NotificationContext"

const useGlobalNotification = () => {
  return useContext(NotificationContext)
}

export { useGlobalNotification }
