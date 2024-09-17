import { useState, PropsWithChildren, useMemo } from "react";
import { NotificationContext } from "./NotificationContext";

const GlobalNotificationProvider = (props: PropsWithChildren) => {
  const [notification, setNotification] = useState<GlobalNotification | null>(null)

  const value = useMemo(
    () => ({
      notification,
      set: (data: GlobalNotification) => setNotification(data),
      dismiss: () => setNotification(null)
    }
  ),
  [notification, setNotification]
  );
  return <NotificationContext.Provider value={value}>{props.children}</NotificationContext.Provider>
}

export { GlobalNotificationProvider }
