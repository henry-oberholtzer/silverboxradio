import { Alert } from "@mantine/core"
import { IconInfoCircle } from "@tabler/icons-react"
import { useGlobalNotification } from "../../hooks/useGlobalNotification"

const GlobalBannerNotification = () => {
  const { notification, dismiss } = useGlobalNotification();

  const icon = <IconInfoCircle/>

  return (
    notification ?
    <Alert styles={{
      root: {
        padding: 5,
      }
    }} icon={icon} withCloseButton onClose={dismiss}>
      {notification.message}
    </Alert>
    :
    <></>
  )
}

export { GlobalBannerNotification }
