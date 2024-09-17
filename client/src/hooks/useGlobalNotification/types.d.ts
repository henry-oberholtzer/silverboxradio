interface GlobalNotification {
  sentiment: "neutral" | "ok" | "warning" | "error",
  message: string
}

type GlobalNoticationContext = {
  notification: GlobalNotification | null;
  set: (data: GlobalNotification) => void;
  dismiss: () => void;
}
