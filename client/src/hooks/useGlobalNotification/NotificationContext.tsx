import { createContext } from "react";

const NotificationContext = createContext<GlobalNoticationContext>({
  notification: null,
  set: () => 200,
  dismiss: () => 200,
})

export { NotificationContext }
