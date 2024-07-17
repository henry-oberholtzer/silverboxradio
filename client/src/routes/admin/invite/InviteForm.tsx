import { Alert, Button, Group, TextInput } from "@mantine/core"
import { useEffect, useState } from "react"
import { useFetcher } from "react-router-dom"
import { IconCheck, IconInfoCircle  } from "@tabler/icons-react"

const InviteForm = () => {
  const fetcher = useFetcher()
  const [emails, setEmails] = useState<string>("")
  const [alert, setAlert] = useState<AlertObject | null>(null)

  useEffect(() => {
    if (fetcher.data && fetcher.state === "idle") {
      if (fetcher.data["created"] && fetcher.data["email"]) {
        setAlert({
          color: "green",
          title: `Invited "${fetcher.data["email"]}"`,
          icon: <IconCheck/>
        })
        setEmails("")
      }
      else
      {
        const message = fetcher.data["errors"]["json"]["email"][0]
        if (message)
        setAlert({
          color: "red",
          title: message,
          icon: <IconInfoCircle/>
        })
      }
    }
  }, [fetcher])

  return (
    <fetcher.Form method="post" action="/admin/invite" autoComplete="off">
        <Group>
          <TextInput
            placeholder="Email"
            autoComplete="off" 
            aria-label="Email"
            name="email"
            value={emails}
            required
            onChange={(e) => setEmails(e.target.value)}/>
          <Button type="submit">
            Invite
          </Button>
          {alert &&
          <Alert variant="light" color={alert.color} title={alert.title} icon={alert.icon} onClose={() => setAlert(null)} withCloseButton/>}
        </Group>
      </fetcher.Form>
  )
}

export { InviteForm }
